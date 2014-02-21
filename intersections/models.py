from django.db import models

class Intersection(models.Model):
	description = models.CharField(max_length=200)
	location= models.CharField(max_length=200)
	equipment = models.IntegerField()
	accidentNum = models.IntegerField()
	remarks = models.CharField(max_length=200)
	
	def __unicode__(self):
		return u'%s' % self.description
	
class Road(models.Model):
	description = models.CharField(max_length=200)
	intersection = models.ForeignKey(Intersection, null=True)
	remarks = models.CharField(max_length=200)
	
	def __unicode__(self):
		return u'%s' % self.description
		
class Accident(models.Model):
	description = models.CharField(max_length=200)
	roadID =  models.ForeignKey(Road, null=True)
	datetime = models.DateTimeField()
	remarks = models.CharField(max_length=200)
	
	def __unicode__(self):
		return u'%s' % self.description
	
class Device(models.Model):
	description = models.CharField(max_length=200)
	
	STATUS = (
		('A','Active'),
		('IA', 'Inactive'),
	)
	TYPE = (
		('TL','Traffic Light'),
		('PC','Pedestrian Crossing'),
		('CC','CCTV'),
		('TC','Tranceiver'),
		('PS','Power Supply'),
		('AC','Accessories'),
		('ML','Miscellaneous'),
	)
	status = models.CharField(max_length=200, choices = STATUS)
	type = models.CharField(max_length=200, choices = TYPE)
	roadID =  models.ForeignKey(Road, null=True)
	remarks = models.CharField(max_length=200)
	
	def __unicode__(self):
		return u'%s' % self.description
	
# Create your models here.
