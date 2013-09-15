from django.contrib.auth.models import User
from django.db import models

from references.models import Country, Room, CountryDestination

# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, related_name='hotels')
    destination = models.ForeignKey(CountryDestination, related_name='hotels', blank=True, null=True)

    stars = models.IntegerField(blank=True, null=True)

    child_with_bed_rate = models.DecimalField(max_digits=30, decimal_places=2)
    child_without_bed_rate = models.DecimalField(max_digits=30, decimal_places=2)
    adult_breakfast_rate = models.DecimalField(max_digits=30, decimal_places=2, blank=True, null=True)
    child_breakfast_rate = models.DecimalField(max_digits=30, decimal_places=2, blank=True, null=True)
    adult_extra_bed_rate = models.DecimalField(max_digits=30, decimal_places=2)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name="hotel_created")
    modified_by = models.ForeignKey(User, related_name="hotel_modified")

    def __unicode__(self, *args, **kwargs):
        return self.name

    class Meta:
        unique_together = ('name', 'country')


class Rate(models.Model):
    hotel = models.ForeignKey(Hotel, related_name='rates')
    room = models.ForeignKey(Room, related_name='rates')
    date_from_day = models.IntegerField() 
    date_from_month = models.IntegerField() 
    date_from_year = models.IntegerField(default=2013) 
    date_to_day = models.IntegerField() 
    date_to_month = models.IntegerField() 
    date_to_year = models.IntegerField(default=2013) 
    rate = models.DecimalField(max_digits=30, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name="rate_created")
    modified_by = models.ForeignKey(User, related_name="rate_modified")

    def __unicode__(self, *args, **kwargs):
        return "Rate %s %s %s" % (self.hotel.name, self.room.name, self.rate)

    class Meta:
        unique_together = ('hotel', 'room', 'date_from_day', 'date_from_month', 'date_to_day', 'date_to_month')
