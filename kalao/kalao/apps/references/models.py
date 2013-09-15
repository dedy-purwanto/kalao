from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name="country_created")
    modified_by = models.ForeignKey(User, related_name="country_modified")

    def __unicode__(self, *args, **kwargs):
        return self.name

class CountryDestination(models.Model):
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=255)
    country = models.ForeignKey(Country, related_name='destinations')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name="country_destination_created")
    modified_by = models.ForeignKey(User, related_name="country_destination_modified")

    def __unicode__(self, *args, **kwargs):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=255, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name="room_created")
    modified_by = models.ForeignKey(User, related_name="room_modified")

    def __unicode__(self, *args, **kwargs):
        return self.name

class Transfer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    rate = models.DecimalField(max_digits=30, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name="transfer_created")
    modified_by = models.ForeignKey(User, related_name="transfer_modified")

    def __unicode__(self, *args, **kwargs):
        return self.name


class ExchangeRate(models.Model):
    rate = models.DecimalField(max_digits=30, decimal_places=2)
    date_from = models.DateField() 
    date_to = models.DateField() 

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name="exchange_rate_created")
    modified_by = models.ForeignKey(User, related_name="exchange_rate_modified")

    def __unicode__(self, *args, **kwargs):
        return "%s" % self.rate

    class Meta:
        unique_together = ('date_from', 'date_to')
