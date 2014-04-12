from django.db import models

class Buddy(models.Model):
    email = models.CharField(max_length=200)
    search_term = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)
    
    def save(self, *args, **kwargs):
        super(Buddy, self).save(*args, **kwargs)
    def __unicode__(self):
        return '{0} is a sponser for {1}'.format(self.first_name,self.search_term)
    

    

