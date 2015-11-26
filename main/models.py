from django.db import models

# Create your models here.

class Amaakin(models.Model):
    text = models.CharField( max_length=50)
    img = models.ImageField(upload_to='amaakin', blank=True)

    def __unicode__(self):
        return unicode(self.text)