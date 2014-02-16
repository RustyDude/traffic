from django.db import models

class Intersection(models.Model):
	description = models.CharField(max_length=200)
	location= models.CharField(max_length=200)
	equipment = models.IntegerField()
	accidentNum = models.IntegerField()
	remarks = models.CharField(max_length=200)
	
	def __unicode__(self):
		return u'%s' % self.description
	
class Accident(models.Model):
	description = models.CharField(max_length=200)
	roadID =  models.CharField(max_length=200)
	datetime = models.DateTimeField()
	remarks = models.CharField(max_length=200)

class Road(models.Model):
	description = models.CharField(max_length=200)
	intersection = models.ForeignKey(Intersection, null=True)
	datetime = models.DateTimeField()
	remarks = models.CharField(max_length=200)
	
class Device(models.Model):
	description = models.CharField(max_length=200)
	status = models.CharField(max_length=200)
	roadID = models.CharField(max_length=200)
	remarks = models.CharField(max_length=200)
	
	
# Create your models here.
