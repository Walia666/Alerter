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
    "size": 100,
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
  result= client.search(index=index, body=document,scroll='2m')
  sid = result['_scroll_id']
  scroll_size = result['hits']['total']
  scroll=[]
  result1=[]
  newlist=[]
  newlist1=[]
  keyarray1=[] 
  keyarray2=[]
  resultlist=[]
  list1=zip(keyarray,newlstvalues)
  for row in result['hits']['hits']:
      resultx=row["_source"]
      t1=resultx.keys()
  for c,d in list1:
      for e in t1:
        if c == e:
          newlist.append(c)
          newlist1.append(d)
  for c,d in zip(newlist,newlist1):
    if d != "None":
      keyarray1.append(c)
  l=len(keyarray1)
  for c,d in list1:
    if d != "None":
      keyarray2.append(c)
  keyarray3=list(set(keyarray2) - set(keyarray1))
  t3 = result['hits']['total']

 
  

  while (scroll_size > 0):
    result = client.scroll(scroll_id = sid, scroll = '2m')
    #zipped list that contains fields of index and its values
    for row in result['hits']['hits']:
     
    
     for x in keyarray1:
      result1=row["_source"][x]
      resultlist.append(result1)
    
    
  
    sid = result['_scroll_id']
  
    scroll_size = len(result['hits']['hits'])
    res=len(resultlist)
  def chunks(l, n):
   
    for i in range(0, len(l), n):
      
        yield l[i:i+n]
  splitlist=list(chunks(resultlist, l))
  #adding the field element at the end of the list
  keyarray1.extend(keyarray3)
  import csv
  with open("fields.csv", "wb") as myfile:
    writer = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    writer.writerow(keyarray1)
    for row in splitlist:
      writer.writerow(row)
  #code to read the csv file     
  with open('fields.csv', 'rb') as myfile:
    response = HttpResponse(myfile, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=fields.csv'
    return response

    return render(request, 'application/docs.html', {'res1':t3,'scroll':res})