from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    active = models.BooleanField(max_length=255)

    date_created = models.DateTimeField(auto_now_add = True)
    date_modified = models.DateTimeField(auto_now = True)
    created_by = models.ForeignKey(User, related_name = "country_created")
    modified_by = models.ForeignKey(User, related_name = "country_modified")

    def __unicode__(self, *args, **kwargs):
        return self.name

class CountryDestination(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    active = models.BooleanField(max_length=255)
    country = models.ForeignKey(Country, related_name='destinations')

    date_created = models.DateTimeField(auto_now_add = True)
    date_modified = models.DateTimeField(auto_now = True)
    created_by = models.ForeignKey(User, related_name = "country_destination_created")
    modified_by = models.ForeignKey(User, related_name = "country_destination_modified")

    def __unicode__(self, *args, **kwargs):
        return self.name


