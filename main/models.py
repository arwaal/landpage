from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Landpage(models.Model):
    text = models.CharField(max_length=50, blank=True)
    img = models.ImageField(upload_to='amaakin', blank=True)

    def __unicode__(self):
        return unicode(self.text)

class Users(models.Model):
    # reg_user = models.OneToOneField(User)
    # first_name = models.CharField(max_length=250, null=True, blank=True)
    # last_name = models.CharField(max_length=250, null=True, blank=True)
    # mobile = models.CharField(max_length=255, null=True, blank=True)
    # date_of_birth = models.DateField(blank=True, null=True)
    email = models.CharField(null=True, blank=True, max_length=255)
    # MALE = 'male'
    # FEMALE = 'female'
    # GENDER_TYPE = ((MALE, 'male'), (FEMALE, 'female'))
    # gender = models.CharField(max_length=255, choices=GENDER_TYPE, default=MALE, null=True, blank=True)

    def __unicode__(self):
        return unicode(self.email)