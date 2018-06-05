nq=[]
  def query(old_query):
    newquery=""
    for x in old_query:
            temp = x
            abc.append(x)
            if(x== '"'):
              temp=temp.replace('"','\\"')

              newquery +=temp
            elif(x=='\\'):
              temp=temp.replace('\\','\\\\')
              newquery +=temp
            else:
              newquery += x 
    return newquery
  nq.append(newquery)

  
  for i in range(len(kibana_query1)):
    query(kibana_query1[i])





 '''     doc = {
  "size": 10,
  "query": {
    "bool": {
      "must": [
        {
          "query_string": {
            "query": newquery,
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
"aggs" : {
     "level" : {
        "terms" : {
          "field" : "module.keyword",
          "size" : 300000
                  }
                }
  },
  "docvalue_fields": [
    "@timestamp"
  ]
} '''


for hostmain,portmain,indexmain in zip(host,port,index1):
    
      portint= int(portmain)
      client=Elasticsearch(host=hostmain, port=portint)
      res = Search(using=client, index=indexmain).filter("term", log_message="coresystem")
      response = res.execute()  

 #parser
    partA=[]
    partB=[]
    partC=[]
    field1=[]
    value1=[]
    field2=[]
    value2=[]
    for parse in kibana_query1:
      part=parse.split(" AND" or " OR")
      part1=part[0]
      partA.append(part1)
      part2=part[1]
      partB.append(part2)
      part3=part[2]
      partC.append(part3)

    for var in partA:
      Part=var.split(":")
      field=Part[0]
      field1.append(field)
      value=Part[1]
      value1.append(value)
    for var1 in partB:
      Part1=var1.split(":")
      field=Part1[0]
      field2.append(field)
      value=Part1[1]
      value2.append(value)





    
   # code to get the hits 
    for hostmain,portmain,indexmain in zip(host,port,index1):
    
      portint= int(portmain)
      client=Elasticsearch(host=hostmain, port=portint)
      res = Search(using=client, index=indexmain).filter("term",log_message=value1[0])

      response = res.execute()  
    #search
     s = Search().using(client).query("match", log_message="coresystem")
  response=s.execute()
  count=response.hits.total

      