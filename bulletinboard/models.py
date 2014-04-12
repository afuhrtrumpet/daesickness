from django.db import models

class BulletinBoard(models.Model):
	condition = models.CharField(max_length=50)

	def __unicode__(self):
		return '{0}'.format(self.condition)

class Message(models.Model):
	container = models.ForeignKey(BulletinBoard)
	message = models.CharField(max_length=200)

	def __unicode__(self):
		return self.message
