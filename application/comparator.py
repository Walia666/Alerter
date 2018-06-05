import tasks
import smtplib,os
from email.mime.text import MIMEText
from subprocess import Popen, PIPE
from email.mime.multipart import MIMEMultipart
import datetime
import time
from datetime import timedelta
import requests
from elasticsearch import Elasticsearch
from elasticsearch_dsl import MultiSearch, Search
from .models import Dashboard,Tag,Log,Log_type,Alert
import unicodedata
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def sendalert2(alert_name,kibana,timeseries1,comp1_threshold_name,base_count,comp1_count,diff_per1,diff_per2,email1,email2,email3,email4,email5,timeframe,ts,perc1,perc2,timeseries2,comp2_threshold_name,comp2_count,sms1,sms2,sms3,sms4,sms5,lastalertsent,username,emp_id):
        mapping = {'24H' : "24 hr(s)",
                 '5m'  : "5 min(s)",
                 '10m' : "10 min(s)",
                 '15m' : "15 min(s)",
                 '20m' : "20 min(s)",
                 '25m' : "25 min(s)",
                 '90m' : "1.5 hr(s)",
                 '30m' : "30 min(s)",
                 '45m' : "45 min(s)",
                 '1H'  : "1 hr",
                 '2H'  : "2 hr(s)",
                 '4H'  : "4 hr(s)",
                 '6H'  : "6 hr(s)",
                 '9H'  : "9 hr(s)",
                 '12H' : "12 hr(s)",
                 '18H' : "18 hr(s)",

                }

        tme = 	{	'1d' : "1 day",
                        '2d': " 2 day(s)",
                        '3d' : "3 day(s)",
                        '4d' : "4 day(s)",
                        '5d' : "5 day(s)",
                        '6d' : "6 day(s)",
                        '7d' : "7 day(s)",
                        '8d' : "8 day(s)"
                        }
        Thresh = {'10' : "10%",
                 '20'  : "20%",
                 '30' : "30%",
                 '40' : "40%",
                 '50' : "50%",
                 '60' : "60%",
                 '70' : "70%",
                 '80' : "80%",
                 '90' : "90%",
                 '100'  : "100%"
                }
        
        

 	SUBJECT = alert_name
        msg = MIMEMultipart()
        Timeframename=mapping[timeframe]
        recipients = [email1,email2,email3,email4,email5]
        if comp1_count and not comp2_count: 
                Threshold=Thresh[comp1_threshold_name]
		html = """\
       		<html>
        	<body>
        	<style>
        	table, th, td {
    		border: 1px solid black;
       			}
      			</style>
       		<table>
        	<tr>
       		<th> Alert Name </th>
       		<td> """ + alert_name + """ </td>
       		</tr>
       		<tr>
        	<th>Timeframe</th>
        	<td> """ + Timeframename  + """ </td>
        	</tr>
        	<tr>
        	<th>Filters</th>
        	<td> """ + kibana + """ </td>
        	</tr>
       
       		 </table>
         	<br>
         	Base Count is: """ + base_count + """
         	<br>
         	<table>
         	<br>
        	<tr><th>#</th><th>Timeseries</th> <th>Count</th><th>Threshold</th><th>Diff Percent with Base</th>
             	</tr>
        	<tr> <td>Comparison 1 </td> <td>""" + timeseries1 + """</td><td>"""+ comp1_count + """ </td> <td>""" + Threshold + """ </td><td>""" + perc1  + """ </td> </tr> 
        	</body>
       		</html>
       		""" 
        
        elif comp2_count and not comp1_count:
                tseries=tme[timeseries2]
                Threshold=Thresh[comp2_threshold_name]
		html = """\
                <html>
                <body>
                <style>
                table, th, td {
                border: 1px solid black;
                        }
                        </style>
                <table>
                <tr>    
                <th> Alert Name </th>
                <td> """ + alert_name + """ </td>
                </tr>
                <tr>    
                <th>Timeframe</th>
                <td> """ + Timeframename  + """ </td>
                </tr>
                <tr>
                <th>Filters</th>
                <td> """ + kibana + """ </td>
                </tr>

                 </table>
                <br>
                Base Count is: """ + base_count + """
                <br>
                <table>
                <br>
                <tr><th>#</th><th>Timeseries</th> <th>Count</th><th>Threshold</th><th>Diff Percent with Base</th>
                </tr>
                <tr> <td>Comparison 2 </td> <td>""" + tseries + """</td><td>"""+ comp2_count + """ </td> <td>""" + Threshold + """ </td><td>""" + perc2  + """ </td> </tr>
                </body>
                </html>
                """
             
	elif comp1_count and  comp2_count:
                tseries=tme[timeseries2]
                Threshold2=Thresh[comp2_threshold_name]
                Threshold1=Thresh[comp1_threshold_name]
                html = """\
                <html>
                <body>
                <style>
                table, th, td {
                border: 1px solid black;
                        }
                        </style>
                <table>
                <tr>    
                <th> Alert Name </th>
                <td> """ + alert_name + """ </td>
                </tr>
                <tr>    
                <th>Timeframe</th>
                <td> """ + Timeframename  + """ </td>
                </tr>
                <tr>
                <th>Filters</th>
                <td> """ + kibana + """ </td>
                </tr>

                 </table>
                <br>
                Base Count is: """ + base_count + """
                <br>
                <table>
                <br>
                <tr><th>#</th><th>Timeseries</th> <th>Count</th><th>Threshold</th><th>Diff Percent with Base</th>
                </tr>
                <tr> <td>Comparison 1 </td> <td>""" + timeseries1 + """</td><td>"""+ comp1_count + """ </td> <td>""" + Threshold1 + """ </td><td>""" + perc1  + """ </td> </tr>
                <tr> <td>Comparison 2 </td> <td>""" + tseries + """</td><td>"""+ comp2_count + """ </td> <td>""" + Threshold2 + """ </td><td>""" + perc2  + """ </td> </tr>
                </body>
                </html>
                """
        part1 = MIMEText(html, 'html')
        msg.attach(part1)
       
        msg["From"] = "shopcluesalerter@shopclues.com"
        if email1 and not email2:
             msg["To"] = email1
        else:
             msg["To"] = ", ".join(recipients)
        msg["Subject"] = SUBJECT
        sentmail="false"
        if html:
        	p = Popen(["/usr/sbin/sendmail", "-t", "-oi"], stdin=PIPE)
        	p.communicate(msg.as_string())
                sentmail="true"
        sms_api="http://shopclues.com/tools/sms.php"
        current_epoch = int(time.time())
        current_timestamp=datetime.datetime.fromtimestamp(lastalertsent).strftime('%Y-%m-%d_%H-%M-%S')
        if comp1_count and not comp2_count:
        	message_sms = "A Timeseries Alert: " + alert_name + " , Base count:" + base_count + " with Diff pct " + timeseries1 + " , " + perc1 + " has occured at " + current_timestamp + "!!" 
	elif comp2_count and not comp1_count:
		 message_sms = "A Timeseries Alert: " + alert_name + " , Base count:" + base_count + " with Diff pct " + tseries + " , " + perc2 + " has occured at " + current_timestamp + "!!"
        elif comp1_count and comp2_count:
		 message_sms = "A Timeseries Alert: " + alert_name + " , Base count:" + base_count + " with Diff1 pct" + timeseries1 + " , " + perc1 + " and diff2 pct "  + tseries + " , " + perc2 + " has occured at " + current_timestamp + "!!"
        message_sms1=message_sms.replace('%','pct')
        sentsms="false" 
        smslist=[sms1,sms2,sms3,sms4,sms5]
        smslist1=['','','','','']
        maillist1=['','','','','']
        if sms1:
           url = sms_api + "?mobile=" + sms1 + "&transaction_id=1&variable=" + message_sms1
           requests.get(url)
           sentsms="true"
           if sms2:
              url = sms_api + "?mobile=" + sms2 + "&transaction_id=1&variable=" + message_sms1
              requests.get(url)
              if sms3:
                url = sms_api + "?mobile=" + sms3 + "&transaction_id=1&variable=" + message_sms1
                requests.get(url)
                if sms4:
                     url = sms_api + "?mobile=" + sms4 + "&transaction_id=1&variable=" + message_sms1
                     requests.get(url)
                     if sms5:
                        url = sms_api + "?mobile=" + sms5 + "&transaction_id=1&variable=" + message_sms1
                        requests.get(url)
        obje=Alert.objects.filter(cluster="systemlog")
        for obje1 in obje:
          ip=obje1.ip_endpoint
        es=Elasticsearch([ip])
        if sentmail == "true" and sentsms == "true":
                es.index(index='alertinfo',doc_type='post',id=lastalertsent,body={
                'alert_name':alert_name,
                'kibana_query':kibana,
                'conditional_operator':"none",
                'count':base_count,
                'sms':sentsms,
                'email':sentmail,
                'mail_sent':recipients,
                'sms_sent':smslist,
                'lastalertsent':lastalertsent,
                'username':username,
                'emp_id':emp_id

                })
        elif sentmail == "true" and sentsms == "false":
                es.index(index='alertinfo',doc_type='post',id=lastalertsent,body={
                'alert_name':alert_name,
                'kibana_query':kibana,
                'conditional_operator':"none",
                'count':base_count,
                'sms':sentsms,
                'email':sentmail,
                'mail_sent':recipients,
                'sms_sent':smslist1,
                'lastalertsent':lastalertsent,
                'username':username,
                'emp_id':emp_id

                })

        elif sentmail == "false" and sentsms == "true":
                es.index(index='alertinfo',doc_type='post',id=lastalertsent,body={
                'alert_name':alert_name,
                'kibana_query':kibana,
                'conditional_operator':"none",
                'count':base_count,
                'sms':sentsms,
                'email':sentmail,
                'mail_sent':maillist1,
                'sms_sent':smslist,
                'lastalertsent':lastalertsent,
                'username':username,
                'emp_id':emp_id

                })
        elif sentmail == "false" and sentsms == "false":
                es.index(index='alertinfo',doc_type='post',id=lastalertsent,body={
                'alert_name':alert_name,
                'kibana_query':kibana,
                'conditional_operator':"none",
                'count':base_count,
                'sms':sentsms,
                'email':sentmail,
                'mail_sent':maillist1,
                'sms_sent':smslist1,
                'lastalertsent':lastalertsent,
                'username':username,
                'emp_id':emp_id

                })

       
      
