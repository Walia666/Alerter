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
from .alerting import sendalert
import datetime
from .models import Dashboard,Tag,Log,Log_type,Alert
from .comparator import sendalert2
from HTMLParser import HTMLParser
import unicodedata
@periodic_task(run_every=(timedelta(seconds=30)), name="elast", ignore_result=True)
def elast():
  obje=Alert.objects.filter(cluster="systemlog")
  for obje1 in obje:
          ip=obje1.ip_endpoint
  es=Elasticsearch([ip])
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
    res = es.search(index="addalert3", doc_type='post', body=body)
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
      username=row["_source"]["username"]
      emp_id=row["_source"]["emp_id"]
      comp1_threshold_name=row["_source"]["comp1_threshold_name"]
      if comp1_threshold_name:
	comp1_threshold_nameint=int(comp1_threshold_name)
      comp1_time_series_name=row["_source"]["comp1_time_series_name"]
      comp2_time_series_name=row["_source"]["comp2_time_series_name"]
      comp2_threshold_name=row["_source"]["comp2_threshold_name"]
      if comp2_threshold_name:
	comp2_threshold_nameint=int(comp2_threshold_name)
      
      kibana=row["_source"]["kibana_query"]
      timeseries=row["_source"]["time_series"]
      
      indexmain=row["_source"]["index"]
      status=row["_source"]["notification_status"]
      timeframe=row["_source"]["time_frame"]
      ipendpoint=row["_source"]["ipendpoint"]
      lastalertsent=row["_source"]["last_alert_sent"]
      conditionaloperator=row["_source"]["conditional_operator"]
      threshold=row["_source"]["count"]
      #username=row["_source"]["username"]
      if threshold:
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
                
    
    Timeframename=mapping[timeframe] 
    Timeframenameint=int(Timeframename)
    
    
    if date_diff_sec >= Timeframenameint and status=="active" and timeseries=="time_series_disable":
        
      es.update(index="addalert3",doc_type="post",id=alertid1,
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
        })

        
        
        
      

  
      currentepoch=int(time.time())
      currentepoch1=currentepoch - 19800
      newepoch= currentepoch - Timeframenameint
      newepoch1= newepoch - 19800
      currentstrf=datetime.datetime.fromtimestamp(currentepoch1).strftime('%Y-%m-%dT%H:%M:%S.000Z')
      newstrf=datetime.datetime.fromtimestamp(newepoch1).strftime('%Y-%m-%dT%H:%M:%S.000Z')
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
              "query": kibana ,
              "analyze_wildcard": "true"
              }
            },
            {
              "range": {
                "@timestamp": {
                "gte": newstrf,
                "lte": currentstrf


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
      emailstr1=str(email1)
      emailstr2=str(email2)
      emailstr3=str(email3)
      emailstr4=str(email4)
      emailstr5=str(email5)
      smsstr1=str(sms1)
      smsstr2=str(sms2)
      smsstr3=str(sms3)
      smsstr4=str(sms4)
      smsstr5=str(sms5)
      if indexmain == "web_log-*" or indexmain == "admin_log-*":
          log_host = "http://weblog.shopclues.com"
      elif indexmain == "audit_log-*":
          log_host = "http://systemlogs.shopclues.net"
      else:
          log_host = "http://qalog.shopclues.net"
      matched_count_now=result['hits']['total']
      ops = {'==' : operator.eq,
       '!=' : operator.ne,
       '<=' : operator.le,
       '>=' : operator.ge,
       '>'  : operator.gt,
       '<'  : operator.lt}
      matched_count_nowint=int(matched_count_now)
      countstr=str(matched_count_now)
      lastalertsent1=int(time.time())
      last_alert=abs(lastalertsent - current_timestamp)
      if last_alert >= int(mapping[timeframe]):
          if ops[conditionaloperator](matched_count_nowint,thresholdint):
            sendalert(emailstr1,emailstr2,emailstr3,emailstr4,emailstr5,alert_name,countstr,log_host,currentstrf,newstrf,kibana,indexmain,threshold,conditionaloperator,smsstr1,smsstr2,smsstr3,smsstr4,smsstr5,lastalertsent1,username,emp_id)
            es.index(index='json21',doc_type='post',id=current_timestamp + 1,body={
          'timestamp':time1,
          'module':alert_name,
          'log_message':"sent_alert",
          'level':"info",
          'errorname':kibana,
              })
            es.update(index="addalert3",doc_type="post",id=alertid1,
          body={"doc":{"last_alert_sent":lastalertsent1}})
          else:
            print alert_name + " was not sent"
    
    elif date_diff_sec >= Timeframenameint and status=="active" and timeseries=="time_series_enable":
        if comp1_threshold_name and not comp2_threshold_name:
		es.update(index="addalert3",doc_type="post",id=alertid1,
          	body={"doc":{"last_alert_sent":lastalertsent,"last_condition_checked":current_timestamp}})
        	time1=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(current_timestamp))
       		emaillist=[email1,email2,email3,email4,email5]
        	smslist=[sms1,sms2,sms3,sms4,sms5]
        	client=Elasticsearch(host=hostmain, port=portint)
      		tme = {'1hr' : "3600",
             		'2hr': "7200",
             		'4hr' : "14400",
             		'6hr' : "21600",
             		'9hr' : "32400",
             		'12hr' : "43200",
             		'18hr' : "64800",
                        '24hr' : "86400"
                        }
                timeseriesname=tme[comp1_time_series_name]
                timeseriesnameint=int(timeseriesname)
                currentepochnew=int(time.time())
                currentepochnew1=currentepochnew - 19800
                time_series1=currentepochnew1 - timeseriesnameint
                time_series2= time_series1 - Timeframenameint
                current_time_series=datetime.datetime.fromtimestamp(time_series1).strftime('%Y-%m-%dT%H:%M:%S.000Z')
                old_time_series=datetime.datetime.fromtimestamp(time_series2).strftime('%Y-%m-%dT%H:%M:%S.000Z')
                client=Elasticsearch(host=hostmain, port=portint) 
                document = {
        		"size": 10,
        		"query": {
        		"bool": {
        		"must": [
          		{
            		 "query_string": {
              		   "query": kibana ,
                             "analyze_wildcard": "true"
                          }
                        },
                     {
                        "range": {
                         "@timestamp": {
                          "gte": old_time_series,
                           "lte": current_time_series
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
                comp1count=result['hits']['total']
                comp1_count=float(comp1count)
                currentepoch=int(time.time())
      		currentepoch1=currentepoch - 19800
     	        newepoch= currentepoch - Timeframenameint
                newepoch1= newepoch - 19800
                currentstrf=datetime.datetime.fromtimestamp(currentepoch1).strftime('%Y-%m-%dT%H:%M:%S.000Z')
                newstrf=datetime.datetime.fromtimestamp(newepoch1).strftime('%Y-%m-%dT%H:%M:%S.000Z')
                doc = {
                        "size": 10,
                        "query": {
                        "bool": {
                        "must": [
                        {
                         "query_string": {
                           "query": kibana ,
                             "analyze_wildcard": "true"
                          }
                        },
                     {
                        "range": {
                         "@timestamp": {
                          "gte": newstrf,
                           "lte": currentstrf
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
                res= client.search(index=indexmain, body=doc)
                basecount=res['hits']['total']
                base_count=float(basecount)
                print base_count
                print comp1_count
                diff_per=((base_count - comp1_count)/((base_count + comp1_count)/2.0))*100
                diff_per=round(diff_per,2)
                diff_per_str=str(diff_per)
                comp1_thresholdname=float(comp1_threshold_name)
                comp1_threshold_name_str=str(comp1_threshold_name)
                comp1_count_str=str(comp1count)
                base_count_str=str(basecount)
                uniup= u'\u2191'
                unidown= u'\u2193'
                perc = diff_per_str + " %"
                if diff_per < 0:
			ts=unidown+diff_per_str
                else:
                        ts=uniup+diff_per_str
             
                if abs(diff_per) > comp1_thresholdname:
                        uni= u'\u2191'.encode('utf-8')
                        print perc
			sendalert2(alert_name,kibana,comp1_time_series_name,comp1_threshold_name_str,base_count_str,comp1_count_str,diff_per_str,email1,email2,email3,email4,email5,timeframe,ts,perc)
                

        elif comp2_threshold_name and not comp1_threshold_name:              
		
                es.update(index="addalert3",doc_type="post",id=alertid1,
                body={"doc":{"last_alert_sent":lastalertsent,"last_condition_checked":current_timestamp}})
                time1=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(current_timestamp))
                emaillist=[email1,email2,email3,email4,email5]
                smslist=[sms1,sms2,sms3,sms4,sms5]
                client=Elasticsearch(host=hostmain, port=portint)
                tme = {'1d' : "86400",
                        '2d': "172800",
                        '3d' : "259200",
                        '4d' : "345600",
                        '5d' : "432000",
                        '6d' : "518400",
                        '7d' : "604800",
                        '8d' : "691200"
                        }
                timeseriesname=tme[comp2_time_series_name]
                timeseriesnameint=int(timeseriesname)
                currentepochnew=int(time.time())
                currentepochnew1=currentepochnew - 19800
                time_series1=currentepochnew1 - timeseriesnameint
                time_series2= time_series1 - Timeframenameint
                current_time_series=datetime.datetime.fromtimestamp(time_series1).strftime('%Y-%m-%dT%H:%M:%S.000Z')
                old_time_series=datetime.datetime.fromtimestamp(time_series2).strftime('%Y-%m-%dT%H:%M:%S.000Z')
                client=Elasticsearch(host=hostmain, port=portint)
                document = {
                        "size": 10,
                        "query": {
                        "bool": {
                        "must": [
                        {
                         "query_string": {
                           "query": kibana ,
                             "analyze_wildcard": "true"
                          }
                        },
                     {
                        "range": {
                         "@timestamp": {
                          "gte": old_time_series,
                           "lte": current_time_series
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
                comp2count=result['hits']['total']
                comp2_count=float(comp2count)
                currentepoch=int(time.time())
                currentepoch1=currentepoch - 19800
                newepoch= currentepoch - Timeframenameint
                newepoch1= newepoch - 19800
                currentstrf=datetime.datetime.fromtimestamp(currentepoch1).strftime('%Y-%m-%dT%H:%M:%S.000Z')
                newstrf=datetime.datetime.fromtimestamp(newepoch1).strftime('%Y-%m-%dT%H:%M:%S.000Z')
                doc = {
                        "size": 10,
                        "query": {
                        "bool": {
                        "must": [
                        {
                         "query_string": {
                           "query": kibana ,
                             "analyze_wildcard": "true"
                          }
                        },
                     {
                        "range": {
                         "@timestamp": {
                          "gte": newstrf,
                           "lte": currentstrf
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
                res= client.search(index=indexmain, body=doc)
                basecount=res['hits']['total']
                base_count=float(basecount)
                print base_count
                print comp2_count
                diff_per=((base_count - comp2_count)/((base_count + comp2_count)/2.0))*100
                diff_per=round(diff_per,2)
                diff_per_str=str(diff_per)
                comp2_thresholdname=float(comp2_threshold_name)
                comp2_threshold_name_str=str(comp2_threshold_name)
                comp2_count_str=str(com2count)
                base_count_str=str(basecount)
                uniup= u'\u2191'
                unidown= u'\u2193'
                perc = diff_per_str + " %"
                if diff_per < 0:
                        ts=unidown+diff_per_str
                else:
                        ts=uniup+diff_per_str

                if abs(diff_per) > comp2_thresholdname:
                        uni= u'\u2191'.encode('utf-8')
                        print perc
                        sendalert2(alert_name,kibana,comp2_time_series_name,comp2_threshold_name_str,base_count_str,comp2_count_str,diff_per_str,email1,email2,email3,email4,email5,timeframe,ts,perc)

