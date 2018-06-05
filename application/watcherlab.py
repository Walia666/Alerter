def search():
  
  es=Elasticsearch()
  WatcherClient.infect_client(es)

  
  doc = {
        'size' : 2000,
        'query': {
            'match_all' : {}
                },
        
       
        }
  res = es.search(index='alertingindex', doc_type='post', body=doc)
  count1=[]
  kibana_query1=[]
  index1=[]
  ipendpoint=[]
  host=[]
  port=[]
  kibana_query1=[]
  threshold1=[]
  conditionaloperator1=[]
  timeframe=[]
  #code to fetch fields from the index
  for row in res['hits']['hits']:
        
        ip= row["_source"]["ipendpoint"]
        ipendpoint.append(ip)
  for row in res['hits']['hits']:
        index=row["_source"]["index"]
        index1.append(index)
  for row in res['hits']['hits']:
        kibana_query=row["_source"]["kibana_query"]
        kibana_query1.append(kibana_query)
  for row in res['hits']['hits']:
        threshold=row["_source"]["count"]
        thresholdint=int(threshold)
        threshold1.append(thresholdint)
  for row in res['hits']['hits']:
        conditionaloperator=row["_source"]["conditional_operator"]
        conditionaloperator1.append(conditionaloperator)
  for row in res['hits']['hits']:
        time_frame=row["_source"]["time_frame"]
        
        timeframe.append(time_frame)

  #code to split port and host
  for i in ipendpoint:
    data=i.split(":")
    data1=data[0]
    host.append(data1)
    data2=data[1]
    port.append(data2)
    
  
#code to get hits
  
  for hostmain,portmain,indexmain in zip(host,port,index1):
    
      portint= int(portmain)
      client=Elasticsearch(host=hostmain, port=portint)
  for kibana,time,op1,thresh in zip(kibana_query1,timeframe,conditionaloperator1,threshold1):
      ops = {'==' : operator.eq,
       '!=' : operator.ne,
       '<=' : operator.le,
       '>=' : operator.ge,
       '>'  : operator.gt,
       '<'  : operator.lt}


      tme = {'24H' : "now-24h",
             '5m'  : "now-5m",
             '10m' : "now-10m",
             '15m' : "now-15m",
             '20m' : "now-20m",
             '25m' : "now-25m",
             '90m' : "now-90m",
             '30m' : "now-30m",
             '45m' : "now-45m",
             '1H'  : "now-1h",
             '2H'  : "now-2h",
             '4H'  : "now-4h",
             '6H'  : "now-6h",
             '9H'  : "now-9h",
             '12H' : "now-12h",
             '18H' : "now-18h",
             
                   }
      document = {
    "size": 10,
    "query": {
    "bool": {
      "must": [
        {
          "query_string": {
            "query":kibana,
            "analyze_wildcard": 'true'
          }
        },
        {
          "range": {
            "@timestamp": {
              "from": "now-1y",
              "to": "now"
            }
          }
        }
       ],
        "must_not": []
      }
      },


  "docvalue_fields": [
    "@timestamp"
  ]
      } 




      result= client.search(index=indexmain, body=document)
      count=result['hits']['total']
      countint=int(count)
      
      es.watcher.put_watch(
      id='error_500',
    
      body={

        

        # Run the watch every 30 seconds
        'trigger': { 'schedule': { 'interval': "30s"  } },

        
        'condition': {  'compare': { 100 :{"gt":50 } } },
         

        "actions": {
        "log" : {
       "logging" : {
         "text" : "alert was sent"
       }
     }
  }
} )
        