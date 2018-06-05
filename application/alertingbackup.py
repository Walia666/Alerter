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
from .models import Dashboard,Tag,UserLogin,Log,Log_type,Alert

def sendalert(email1,email2,email3,email4,email5,alert_name,count,log_host,currentstrf,newstrf,kibana,index,threshold,conditionaloperator,sms1,sms2,sms3,sms4,sms5,lastalertsent,username,emp_id):
        SUBJECT = "Alert"
        msg = MIMEMultipart('alternative')
        recipients = [email1,email2,email3,email4,email5]
        kibana_url=log_host + "/app/kibana#/discover?_g=(refreshInterval:(display:Off,pause:!f,value:0),time:(from:'"+ newstrf +"',mode:absolute,to:'" + currentstrf + "'))&_a=(columns:!(_source),index:'" + index + "',interval:auto,query:(query_string:(analyze_wildcard:!t,query:'" + kibana + "')),sort:!('@timestamp',desc))"
        kibana_url1=kibana_url.replace('"','%22')
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
        <th>Kibana Query</th>
        <td> """ + kibana + """ </td>
        </tr>
        <tr>
        <th>Count</th>
        <td> """ + count + """ </td>
        </tr>
        <tr>
        <th>Conditional operator </th>
        <td> """ + conditionaloperator +  """ </td>
        </tr>
        <tr>
        <th> Threshold </th>
        <td>  """ + threshold + """ </td>  
        </tr>
        <tr>
        <th>Kibana URL </th>
        <td> <a href=" """ + kibana_url1 + """ "> Kibana URL </a> </td>
        </th>      
        </table> 
        </body>
       </html>
       """
        part2 = MIMEText(html, 'html')
        msg.attach(part2) 
        msg["From"] = "shopcluesalerter@shopclues.com"
        msg["To"] = ", ".join(recipients)
        msg["Subject"] = SUBJECT
        sentmail="false"
        if html:
       	 	p = Popen(["/usr/sbin/sendmail", "-t", "-oi"], stdin=PIPE)
       		p.communicate(msg.as_string())
                sentmail = "true"
        sms_api="http://shopclues.com/tools/sms.php" 
        current_epoch = int(time.time())
        current_timestamp=datetime.datetime.fromtimestamp(lastalertsent).strftime('%Y-%m-%d_%H-%M-%S')
        
        message_sms = "A log event named " + alert_name + " with " + kibana + " with count " + conditionaloperator +" " + threshold +" (" + count + ") has occured at " + current_timestamp + "!!";
        sentsms="false"
        if sms1:
           url = sms_api + "?mobile=" + sms1 + "&transaction_id=1&variable=" + message_sms
           requests.get(url)
           sentsms= "true"
           if sms2: 
              url = sms_api + "?mobile=" + sms2 + "&transaction_id=1&variable=" + message_sms
              requests.get(url)
              if sms3:
                url = sms_api + "?mobile=" + sms3 + "&transaction_id=1&variable=" + message_sms
                requests.get(url)
                if sms4:
                     url = sms_api + "?mobile=" + sms4 + "&transaction_id=1&variable=" + message_sms
                     requests.get(url)
                     if sms5:
                        url = sms_api + "?mobile=" + sms5 + "&transaction_id=1&variable=" + message_sms
                        requests.get(url)
        smslist=[sms1,sms2,sms3,sms4,sms5]
        obje=Alert.objects.filter(cluster="systemlog")
        for obje1 in obje:
          ip=obje1.ip_endpoint
        es=Elasticsearch([ip])
        if sentmail == "true" and sentsms == "true":
                es.index(index='alertinfo',doc_type='post',body={
                'alert_name':alert_name,
                'kibana_query':kibana,
                'conditional_operator':conditionaloperator,
                'count':count,
                'sms':sentsms,
                'email':sentmail,
                'mail_sent':recipients,
                'sms_sent':smslist,
                'lastalertsent':lastalertsent,
                'username':username,
                'emp_id':emp_id

                })
        elif sentmail == "true" and sentsms == "false":
                es.index(index='alertinfo',doc_type='post',body={
                'alert_name':alert_name,
                'kibana_query':kibana,
                'conditional_operator':conditionaloperator,
                'count':count,
                'sms':sentsms,
                'email':sentmail,
                'mail_sent':recipients,
                'sms_sent':smslist,
                'lastalertsent':lastalertsent,
                'username':username,
                'emp_id':emp_id
        
                })
        elif sentmail == "false" and sentsms == "true":
                es.index(index='alertinfo',doc_type='post',body={
                'alert_name':alert_name,
                'kibana_query':kibana,
                'conditional_operator':conditionaloperator,
                'count':count,
                'sms':sentsms,
                'email':sentmail,
                'mail_sent':recipients,
                'sms_sent':smslist,
                'lastalertsent':lastalertsent, 
                'username':username,
                'emp_id':emp_id

                })
        elif sentmail == "false" and sentsms == "false":
                es.index(index='alertinfo',doc_type='post',body={
                'alert_name':alert_name,
                'kibana_query':kibana,
                'conditional_operator':conditionaloperator,
                'count':count,
                'sms':sentsms,
                'email':sentmail,
                'mail_sent':recipients,
                'sms_sent':smslist,
                'lastalertsent':lastalertsent,
                'username':username,
                'emp_id':emp_id

                })
 
       
                                  
