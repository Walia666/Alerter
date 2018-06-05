from __future__ import absolute_import, unicode_literals
from celery import Celery
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from elasticsearch import Elasticsearch
from elasticsearch_dsl import MultiSearch, Search
import operator
#from .celery import app
from django_celery_beat.models import PeriodicTask, IntervalSchedule
import time
from datetime import timedelta
import json




@periodic_task(run_every=(timedelta(seconds=30)), name="elast", ignore_result=True)
def elast():
  es=Elasticsearch()

  doc = {
        'size' : 2000,
        'query': {
            'match_all' : {}
                },
        
       
        }

  res = es.search(index="elastindexer999", doc_type='post', body=doc)
  count=res['hits']['total']
  for counter in range(1,count+1):
    body={
    'query': {
      'match': {
        '_id': counter,
     } } }
    res = es.search(index="elastindexer999", doc_type='post', body=body)
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
      username=row["_source"]["username"]
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
    
    
    if date_diff_sec >= Timeframenameint and status=="active":
        
      es.update(index="elastindexer999",doc_type="post",id=alertid1,
          body={"doc":{"last_alert_sent":lastalertsent,"last_condition_checked":current_timestamp}})
      time1=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(current_timestamp))
      emaillist=[email1,email2,email3,email4,email5]
      smslist=[sms1,sms2,sms3,sms4,sms5]
      es.index(index='json21',doc_type='post',id=current_timestamp,body={
        'timestamp':time1,
        'module':alert_name,
        'log_message':"checked_alert",
        'level':"info",
        'errorname':kibana,
        "otherdata":{"email":emaillist, "sms":smslist,"Username":username}
        })

        
        
        
      



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
            print alert_name + " was sent"
            es.index(index='json21',doc_type='post',id=current_timestamp + 1,body={
          'timestamp':time1,
          'module':alert_name,
          'log_message':"sent_alert",
          'level':"info",
          'errorname':kibana,
          "otherdata":{"email":emaillist, "sms":smslist,"Username":username}
              })
          else:
            print alert_name + " was not sent"