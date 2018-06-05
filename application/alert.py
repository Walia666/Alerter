import smtplib

def sendalert():
	sender = 'alerter@shopclues.com'
	receivers = ['Anshul.Walia@shopclues.com']

	message = """ alert
	"""

	try:
   		smtpObj = smtplib.SMTP('localhost')
   		smtpObj.sendmail(sender, receivers, message)         
   		print "Successfully sent email"
	except smtplib.SMTPException:
  		 print "Error: unable to send email"