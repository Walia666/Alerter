from django.db import models
from django import forms


# Create your models here.



class Tag(models.Model):
	slug= models.SlugField(max_length=200,unique=True)
	def __str__(self):
		return self.slug

class Dashboard(models.Model):
	
    
	feature_type=models.ManyToManyField(Tag)
	Dashboard_name=models.CharField(max_length=50,default='dash')
	Dashboard_url=models.URLField(max_length=100,default='url')
	owner_name=models.CharField(max_length=50,default='name')
	owner_email=models.EmailField(max_length=50,default='none')

class Log_type(models.Model):
	log_field= models.CharField(max_length=200,unique=True,default='Select Log')
	def __str__(self):
		return self.log_field
	
class Log(models.Model):
	
	log_field = models.ForeignKey(Log_type,default='Select Log')
 	
 	index= models.CharField(max_length=200)
	ip_endpoint= models.CharField(max_length=200)


class Alert(models.Model):
    cluster=models.CharField(max_length=100)
    ip_endpoint=models.CharField(max_length=100)



