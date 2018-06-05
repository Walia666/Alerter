def search(request):
  es=Elasticsearch()
  doc = {
        'size' : 2000,
        'query': {
            'match_all' : {}
                },
        
       
        }
  res = es.search(index='indexalert', doc_type='post', body=doc)
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
        threshold1.append(threshold)
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
    



  
  
  #Converting Query to kibana query using escapes starts here
    newquery=""
    for x in kibana_query1[0]:
            temp = x
            
            if(x== '"'):
              temp=temp.replace('"','\"')

              newquery +=temp
            elif(x=='\\'):
              temp=temp.replace('\\','\\\\')
              newquery +=temp
            else:
              newquery += x 
  
#code to get hits
  for hostmain,portmain,indexmain in zip(host,port,index1):
    
      portint= int(portmain)
      client=Elasticsearch(host=hostmain, port=portint)
  document = {
  "size": 10,
  "query": {
    "bool": {
      "must": [
        {
          "query_string": {
            "query":newquery,
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
  thresholdint=int(threshold[0])
  abc=type(conditionaloperator1[0])
  
  stmt1=""
  stmt=""
  if(countint ==thresholdint):
    stmt="Alert is sent"
  else:
    stmt1="Alert is not sent" 

       
  
  
  




    
  
    
      

  

        

  return render(request,'application/search.html',{'index1':index1,'ipendpoint':ipendpoint,'host':host,'port':port,'kibana_query':kibana_query1,'client':client,'indexmain':indexmain,'hostmain':hostmain,'portmain':portmain,'count':count,'res':res,'threshold':threshold1,'conditionaloperator1':conditionaloperator1,'timeframe':timeframe,'stmt':stmt,'stmt1':stmt1,'abc':abc})