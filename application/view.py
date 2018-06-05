from django.shortcuts import render,redirect
from .models import Dashboard,Tag,UserLogin,Log,Elast,Alert
from .forms import UserLoginform,Logform
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
import ldap
import datetime
from elasticsearch_dsl import MultiSearch, Search
import redis
import unicodedata
from django.db import connection
from elasticsearch import Elasticsearch
import operator
import tasks
import sys
import json
import time
import smtplib
from .models import COD
import csv
from django.http import HttpResponse
import itertools
import urllib2
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt







# Create your views here.

def test(request):
  Value=Tag.objects.all()
  Dash=Dashboard.objects.all()
  
  return render(request,'application/calshopclues.html',{'all': Dash,'Value':Value,})

def general(request):
 # if 'emp_id' in request.session and 'Username' in request.session:
  
    
    if request.method == "POST":
        form = Logform(request.POST)
        if (form.is_valid()):
          return HttpResponseRedirect()
    else:
        form =Logform()


    

    return render(request, 'application/applogalert.html', {'form':form})  

def generate(request):
  if request.method == "POST":
        form = Logform(request.POST)
        if (form.is_valid()):
          return HttpResponseRedirect()
  else:
        form =Logform()
  
  



  return render(request, 'application/createcsv1.html', {'form':form})

        
def edit(request):
  obje=Alert.objects.filter(cluster="systemlog")
  for obje1 in obje:
    ip=obje1.ip_endpoint    
  es=Elasticsearch(ip)
  if request.method == 'POST':
        
        
        alert_name1 = request.POST['alert_name']
        time_frame = request.POST['time_frame_name']
        kibana_query= request.POST['kibana_query']
        conditional_operator=request.POST['conditional_operator']
        count=request.POST['match_field_count_name']
        email1=request.POST.get('email_name1',)
        email2=request.POST.get('email_name2',)
        email3=request.POST.get('email_name3',)
        email4=request.POST.get('email_name4',)
        email5=request.POST.get('email_name5',)
        SMS1=request.POST.get('contact_sms_name1',) 
        SMS2=request.POST.get('contact_sms_name2',) 
        SMS3=request.POST.get('contact_sms_name3',) 
        SMS4=request.POST.get('contact_sms_name4',) 
        SMS5=request.POST.get('contact_sms_name5',) 
        call1=request.POST.get('contact_call_name1',)
        severity=request.POST['severity']
        
        notification_status=request.POST['Notification_status']
        alertid=request.POST['alert_id']
  doc = {
        'size' : 2000,
        'query': {
            'match_all' : {}
                },
        
       
        }

  res = es.search(index="addalert3", doc_type='post', body=doc)
  for row in res['hits']['hits']:
      alertid1=row["_id"]
     
      es.update(index="addalert3",doc_type="post",id=alertid,
      body={"doc":{"time_frame":time_frame,"kibana_query":kibana_query,"conditional_operator":conditional_operator,
      "count":count,"email1":email1,"SMS1":SMS1,"call1":call1,"notification_status":notification_status,'alert_name':alert_name1, 
       "email2":email2,"email3":email3,"email4":email4,"email5":email5,"SMS2":SMS2,"SMS3":SMS3,"SMS4":SMS4,"SMS5":SMS5 ,"severity":severity}})






  return redirect('/application/modify')

def form1(request):
    if request.method == "POST":
        form = UserLoginform(request.POST)
        if (form.is_valid()):
          return HttpResponseRedirect()
          
    else:
        form =UserLoginform()
    
    return render(request,'application/base.html',{'form':form})

def form(request):
    
    return render(request,'application/form.html',{})













def logout(request):
  del request.session['emp_id']
  del request.session['Username']
  


  return redirect('/application/form/')



def login(request):
      if request.method == "POST":
        form = Logform(request.POST)
        if (form.is_valid()):
          return HttpResponseRedirect()
      else:
        form =Logform()
      if request.method == 'POST':
        
        Username = request.POST['Username']
        Password = request.POST['Password']
        emp_id = request.POST['emp_id']
        
        
        
        ldap_server = "192.168.11.67"
        ldap_port = "389"
       #  the following is the user_dn format provided by the ldap server
        user_dn = "cn=" + Username + ",ou=People,dc=shopclues,dc=com"
        # adjust this to your base dn for searching
        base_dn = "dc=shopclues,dc=com"
        connect = ldap.open(ldap_server)
        search_filter = "uid=" + emp_id
        try:
                # if authentication successful, get the full user data
                connect.bind_s(user_dn, Password)
                result = connect.search_s(base_dn, ldap.SCOPE_SUBTREE, search_filter)
                
                request.session['Username'] = Username
                request.session['emp_id']=emp_id 
                # return all user data results
                return redirect('/application/general/')
                connect.unbind_s()
                
                                        
        except ldap.LDAPError:
                connect.unbind_s()
                return render(request,'application/error.html',{'Username':Username,'Password':Password})
def modify(request):
 

# if 'emp_id' in request.session and 'Username' in request.session:
    obje=Alert.objects.filter(cluster="systemlog")
    for obje1 in obje:
      ip=obje1.ip_endpoint
    es=Elasticsearch(ip)

    doc = {
        'size' : 2000,
        'query': {
            'match_all' : {}
                },
        
       
        }
    res = es.search(index="addalert3", doc_type='post', body=doc)
    alertnamelist=[]
    alertidlist=[]
    logtypelist=[]
    lastalertsentlist=[]
    kibanaquerylist=[]
    conditionaloperatorlist=[]
    countlist=[]
    timeframelist=[]
    emaillist1=[]
    emaillist2=[]
    emaillist3=[]
    emaillist4=[]
    emaillist5=[]

    calllist1=[]
    smslist2=[]
    smslist3=[]
    smslist4=[]
    smslist1=[]
    smslist5=[]
   # emp_idsession=request.session['emp_id']
    notificationstatuslist=[]

     
    for row in res['hits']['hits']:
    #  emp_id1=row["_source"]["emp_id"]
     # if emp_idsession == emp_id1 :
        alertname=row["_source"]["alert_name"]
        alertid=row["_id"]
        logtype=row["_source"]["logtype"]
        lastalertsent=row["_source"]["last_alert_sent"]
        kibanaquery=row["_source"]["kibana_query"]
        count=row["_source"]["count"]
        timeframe=row["_source"]["time_frame"]
        conditionaloperator=row["_source"]["conditional_operator"]
        email1=row["_source"]["email1"]
        email2=row["_source"]["email2"]
        email3=row["_source"]["email3"]
        email4=row["_source"]["email4"]
        email5=row["_source"]["email5"]
        call1=row["_source"]["call1"]
        sms1=row["_source"]["SMS1"]
        sms2=row["_source"]["SMS2"]
        sms3=row["_source"]["SMS3"]
        sms4=row["_source"]["SMS4"]
        sms5=row["_source"]["SMS5"]
        notificationstatus=row["_source"]["notification_status"]
        

        lst=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(lastalertsent))
        email2string=str(email2)
        email3string=str(email3)
        email4string=str(email4)
        email5string=str(email5)
        sms2striing=str(sms2)
        sms3string=str(sms3)
        sms4string=str(sms4)
        sms5string=str(sms5) 
        
        alertnamelist.append(alertname)
        alertidlist.append(alertid)
        logtypelist.append(logtype)
        lastalertsentlist.append(lst)
        kibanaquerylist.append(kibanaquery)
        countlist.append(count)
        timeframelist.append(timeframe)
        conditionaloperatorlist.append(conditionaloperator)
        emaillist1.append(email1)
        calllist1.append(call1)
        smslist1.append(sms1)
        notificationstatuslist.append(notificationstatus)
        emaillist2.append(email2string)
        emaillist3.append(email3string)
        emaillist4.append(email4string)
        emaillist5.append(email5string)
        smslist2.append(sms2striing)
        smslist3.append(sms3string)
        smslist4.append(sms4string)
        smslist5.append(sms5string)
        
    zippedlist=zip(alertnamelist,logtypelist,lastalertsentlist,alertidlist,kibanaquerylist,countlist,timeframelist,conditionaloperatorlist,emaillist1,calllist1,smslist1,notificationstatuslist,emaillist2,emaillist3,emaillist4,emaillist5,smslist2,smslist3,smslist4,smslist5)    

    return render(request, 'application/modify.html', {'alertnamelist':alertnamelist,'alertidlist':alertidlist,'logtypelist':logtypelist,
       'zippedlist':zippedlist,'lastalertsentlist':lastalertsentlist,'countlist':countlist})


def valid(request):

    
    SMS2=""
    SMS3=""
    SMS4=""
    SMS5=""
    email2=""
    email3=""
    email4=""
    email5=""
    call2=""
    call3=""
    call4=""
    call5=""
    now=datetime.datetime.now()
    
    
    
    if request.method == 'POST':
        log_field=request.POST['log_field']
        
        alert_name = request.POST['alert_name']
        time_frame = request.POST['time_frame_name']
        kibana_query= request.POST['kibana_query']
        conditional_operator=request.POST['conditional_operator']
        count=request.POST['match_field_count_name']
        email1=request.POST.get('email_name1',)
        email2=request.POST.get('email_name2',)
        email3=request.POST.get('email_name3',)
        email4=request.POST.get('email_name4',)
        email5=request.POST.get('email_name5',)
        SMS1=request.POST.get('contact_sms_name1',) 
        SMS2=request.POST.get('contact_sms_name2',)
        SMS3=request.POST.get('contact_sms_name3',)
        SMS4=request.POST.get('contact_sms_name4',)
        SMS5=request.POST.get('contact_sms_name5',)        
        call1=request.POST.get('contact_call_name1',)
        call2=request.POST.get('contact_call_name2',)
        call3=request.POST.get('contact_call_name3',)
        call4=request.POST.get('contact_call_name4',)
        call5=request.POST.get('contact_call_name5',)
        
        severity=request.POST['severity']

    ob1=Elast.objects.filter(id=log_field)
    for ob in ob1:
       logfield=ob.log_field
    objs=Log.objects.filter(log_field_id=log_field)
    
    for obj in objs:
      index=obj.index
      ipendpoint=obj.ip_endpoint
    ts = time.time()
    obje=Alert.objects.filter(cluster="systemlog")
    for obje1 in obje:
      ip=obje1.ip_endpoint
    es=Elasticsearch(ip)
    doc = {
        'size' : 2000,
        'query': {
            'match_all' : {}
                },
        
       
        }

    

    active="active"




    
    es.index(index='addalert3',doc_type='post',body={
        'alert_name':alert_name,
        'time_frame':time_frame,
        'kibana_query':kibana_query,
        'conditional_operator':conditional_operator,
        'count':count,
        'email1':email1,
        'email2':email2,
        'email3':email3,
        'email4':email4,
        'email5':email5,
        'SMS1':SMS1,
        'SMS2':SMS2,
        'SMS3':SMS3,
        'SMS4':SMS4,
        'SMS5':SMS5,
        'call1':call1,
        'call2':call2,
        'call3':call3,
        'call4':call4,
        'call5':call5,
        'severity':severity,
        'index':index,
        'ipendpoint':ipendpoint,
        'last_condition_checked':ts,
        'last_alert_sent':0,
        'logtype':logfield,
        'notification_status':active,
    #    'emp_id':request.session['emp_id'],
    #   'username':request.session['Username']

        
        
        })  

    
    return redirect('/application/general/')  

      

 




def elast(request):
  es=Elasticsearch()

  doc = {
        'size' : 2000,
        'query': {
            'match_all' : {}
                },
        
       
        }

  res = es.search(index="addalert3", doc_type='post', body=doc)
  count=res['hits']['total']
  for counter in range(1,count+1):
    body={
    'query': {
      'match': {
        '_id': counter,
     } } }
    res = es.search(index="addalert4", doc_type='post', body=body)
    for row in res['hits']['hits']:
      current_timestamp=time.time()
     
      alertid1=row["_id"]

      lastchecked= row["_source"]["last_condition_checked"]
      lastcheckedint=int(lastchecked)
      
      time1=row["_source"]["time_frame"]
      email1=row["_source"]["email1"]
      email2=row["_source"]["email2"]
      email3=row["_source"]["email3"]
      email4=row["_source"]["email4"]
      email5=row["_source"]["email5"]
      call1=row["_source"]["call1"]
      call2=row["_source"]["call2"]
      call3=row["_source"]["call3"]
      call4=row["_source"]["call4"]
      call5=row["_source"]["call5"]
      sms1=row["_source"]["SMS1"]
      sms2=row["_source"]["SMS2"]
      sms3=row["_source"]["SMS3"]
      sms4=row["_source"]["SMS4"]
      sms5=row["_source"]["SMS5"]
      logtype=row["_source"]["logtype"]
      alert_name=row["_source"]["alert_name"]
      
      kibana=row["_source"]["kibana_query"]
      
      indexmain=row["_source"]["index"]
      status=row["_source"]["notification_status"]
      timeframe=row["_source"]["time_frame"]
      ipendpoint=row["_source"]["ipendpoint"]
      lastalertsent=row["_source"]["last_alert_sent"]
      conditionaloperator=row["_source"]["conditional_operator"]
      threshold=row["_source"]["count"]
      thresholdint=int(threshold)
      date_diff_sec=current_timestamp - lastchecked
      #code to split port and host
      
      data=ipendpoint.split(":")
      hostmain=data[0]
      portmain=data[1]
      portint=int(portmain)      

    mapping = {'24H' : "86400",
                 '5m'  : "300",
                 '10m' : "600",
                 '15m' : "900",
                 '20m' : "1200",
                 '25m' : "1500",
                 '90m' : "5400",
                 '30m' : "1800",
                 '45m' : "2700",
                 '1H'  : "3600",
                 '2H'  : "7200",
                 '4H'  : "14400",
                 '6H'  : "21600",
                 '9H'  : "32400",
                 '12H' : "43200",
                 '18H' : "64800",
             
                }
                
    matched_count_now=" "
    Timeframename=mapping[timeframe] 
    Timeframenameint=int(Timeframename)
    stmt1=""
    stmt2=""
    if date_diff_sec >= Timeframenameint and status=="active":
        
      es.update(index="addalert4",doc_type="post",id=alertid1,
          body={"doc":{"last_alert_sent":lastalertsent,"last_condition_checked":current_timestamp}})
        

      client=Elasticsearch(host=hostmain, port=portint)
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
        } ,


          "docvalue_fields": [
          "@timestamp"
        ]
            } 
      
      result= client.search(index=indexmain, body=document)
      matched_count_now=result['hits']['total']
      ops = {'==' : operator.eq,
       '!=' : operator.ne,
       '<=' : operator.le,
       '>=' : operator.ge,
       '>'  : operator.gt,
       '<'  : operator.lt}
      matched_count_nowint=int(matched_count_now)  
      last_alert=abs(lastalertsent - current_timestamp)
      if last_alert >= int(mapping[timeframe]):
          if ops[conditionaloperator](matched_count_now,thresholdint):
            stmt1="alert was sent"
          else:
            stmt2="alert was not sent"
      

#      result=sendalert()

  






              


        

    


  return render(request,'application/new.html',{'c1':count,'index':indexmain,'diff':date_diff_sec,'alertid':alertid1,'count':matched_count_now,'host':hostmain,'port':portmain,'kibana':kibana,'status':status,'timeframename':Timeframename,'stmt1':stmt1,'stmt2':stmt2})



def search(request):
  es=Elasticsearch()

  
  doc = {
        'size' : 2000,
        'query': {
            'match_all' : {}
                },
        
       
        }
  res = es.search(index="addalert4", doc_type='post', body=doc)
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
  for kibana,time in zip(kibana_query1,timeframe):
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
      count1.append(countint)
  for c1,t1,op1 in zip(count1,threshold1,conditionaloperator1):  
  #mapping of operators
    ops = {'==' : operator.eq,
       '!=' : operator.ne,
       '<=' : operator.le,
       '>=' : operator.ge,
       '>'  : operator.gt,
       '<'  : operator.lt}
  
  
    if ops[op1](c1,t1):
      print "Alert is sent"
    else:
      print "Alert is not sent"
  
  
    return render(request,'application/search.html',{'index1':index1,'ipendpoint':ipendpoint,'host':host,'port':port,'kibana_query':kibana_query,'timeframe':time,'count1':count1,'conditionaloperator1':conditionaloperator1,'threshold1':threshold1,'count':count,'hostmain':hostmain,'portmain':portmain,'indexmain':indexmain,'result':result})

def docsnew(request):
  
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

  ob1=Elast.objects.filter(id=log_field)
  for ob in ob1:
      logfield=ob.log_field
  objs=Log.objects.filter(log_field_id=log_field)
  for obj in objs:
      index=obj.index
      ipendpoint=obj.ip_endpoint
  data=ipendpoint.split(":")
  hostmain=data[0]
  portmain=data[1]
  portint=int(portmain) 
  client=Elasticsearch(host=hostmain, port=portint)
  
  document = {
    "size": 1000,
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
  result= client.search(index=index, body=document,scroll='2m',request_timeout=500)
  sid = result['_scroll_id']
  scroll_size = result['hits']['total']
  c1 = result['hits']['total']
  scroll=[]
  result1=[]
  newlist=[]
  newlist1=[]
  keyarray1=[] 
  keyarray2=[]
  resultlist=[]
  keyrow=[]

  list1=zip(keyarray,newlstvalues)
  for row in result['hits']['hits']:
      resultx=row["_source"]
      keyrow=resultx.keys()
  if not keyrow:
    return render(request, 'application/docs.html', {'kibanaquery':kibanaquery})
  else:

   for c,d in list1:
      for e in keyrow:
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
  
    #zipped list that contains fields of index and its values
    for row in result['hits']['hits']:
     
    
     for x in keyarray1:
      result1=row["_source"][x]
      resultlist.append(result1)
    
    
    res=len(resultlist) 
    sid = result['_scroll_id']
  
    scroll_size = len(result['hits']['hits'])
    result = client.scroll(scroll_id = sid, scroll = '2m')
    res=len(resultlist)
   def chunks(l, n):
   
    for i in range(0, len(l), n):
      
        yield l[i:i+n]
   splitlist=list(chunks(resultlist, l))
   #adding the uncommon field element at the end of the list
   keyarray1.extend(keyarray3)
   

   ct=time.time()
 

   import csv
   with open("fields.csv", "wb") as myfile:
    writer = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    writer.writerow(keyarray2)
    for row in splitlist:
      writer.writerow(row)
    stat="true"
   if stat == "true":
    stmt="Csv file was downloaded"
   else:
    stmt="Error in downloading file"
   client.index(index='csvlogging',doc_type='post',id=ct+1,body={
        'kibanaquery':kibanaquery,
        'datefrom':datefrom,
        'dateto':dateto,
        'log_field':log_field,
        'fields_selected':keyarray1,
        'document count':res,
        'index':index,
        'status_csvfile':stmt
      })
   
 

  #code to read the csv file     
   with open('fields.csv', 'rb') as myfile:
    response = HttpResponse(myfile, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=fields.csv'
    return response

    return render(request, 'application/docs.html', {'res1':t3,'scroll':res})

@csrf_exempt
def crossdomainData(request):
    if request.is_ajax() and request.POST:
        log = request.POST['log']
        logint=int(log)  
      
    ob1=Elast.objects.filter(id=log)
    for ob in ob1:
       logfield=ob.log_field
    objs=Log.objects.filter(log_field_id=log)

    for obj in objs:
      index=obj.index
      ipendpoint=obj.ip_endpoint
    url="http://"+ipendpoint+"/"+index
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)

    return HttpResponse(response.read(), content_type="application/json")




   
