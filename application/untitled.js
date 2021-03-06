def docsnew(request):
  client = Elasticsearch()
  values=[]
  
  if request.method == 'POST':
    log_field=request.POST['log_field']
    array=request.POST['data']
    kibanaquery=request.POST['kibana_query']
    datefrom = request.POST['datetime_from_name']
    dateto= request.POST['datetime_to_name']
    pattern = '%d-%m-%Y %H:%M:%S'
    datefromsec = int(time.mktime(time.strptime(datefrom, pattern)))
    datetosec=int(time.mktime(time.strptime(dateto, pattern)))
    keyarray=array.split(',')


    for item in keyarray:
      marked=request.POST.get(item,)
      values.append(marked)
  newlstvalues = [str(x) for x in values]
  current_timestamp=time.time()
  from_date=abs(current_timestamp - datefromsec)
  to_date=abs(current_timestamp- datetosec)
  from_date_int=int(from_date)
  to_date_int=int(to_date)

  objs = Log.objects.raw('SELECT * FROM application_log WHERE log_field = %s', [log_field])
  for obj in objs:
    index=obj.index
    ipendpoint=obj.ip_endpoint
    logfield=obj.log_field 
  data=ipendpoint.split(":")
  hostmain=data[0]
  portmain=data[1]
  portint=int(portmain) 
  client=Elasticsearch(host=hostmain, port=portint)
  
  document = {
    "size": 10000 ,
    "query": {
    "bool": {
      "must": [
        {
          "query_string": {
            "query":kibanaquery,
            "analyze_wildcard": 'true'
          }
        },
        {
          "range": {
            "@timestamp": {
              "from": "now-"+str(from_date_int)+"s",
              "to": "now-"+str(to_date_int)+"s"

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
  result= client.search(index=index, body=document)
  list1=zip(keyarray,newlstvalues)


  
  newlist=[]
  newlist1=[]
  for row in result['hits']['hits']:
     resultx=row["_source"]
     t1=resultx.keys()
  for c,d in list1:
      for e in t1:
        if c == e:
          newlist.append(c)
          newlist1.append(d)
    

 
  

  keyarray1=[]     
  for c,d in zip(newlist,newlist1):
    if d != "None":
      keyarray1.append(c)
  l=len(keyarray1)
  resultlist=[]
  for row in result['hits']['hits']:
     resultx=row["_source"]
     t1=resultx.keys()
     for x in keyarray1:
      result1=row["_source"][x]
      resultlist.append(result1)

  def chunks(l, n):
   
    for i in range(0, len(l), n):
      
        yield l[i:i+n]
  splitlist=list(chunks(resultlist, l))
  



  import csv
  with open("fields.csv", "wb") as myfile:
    writer = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    writer.writerow(keyarray1)
    for row in splitlist:
      writer.writerow(row) 
  with open('fields.csv', 'rb') as myfile:
    response = HttpResponse(myfile, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=fields.csv'
    return response