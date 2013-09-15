from django.db import models
from django.contrib.auth.models import User

from hotels.models import Hotel
from references.models import Room, Transfer

# Create your models here.
class Package(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)

    markup_amount = models.DecimalField(max_digits=30, decimal_places=2)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name="package_created")
    modified_by = models.ForeignKey(User, related_name="package_modified")

    def __unicode__(self, *args, **kwargs):
        return self.name

class PackageBatch(models.Model):
    package = models.ForeignKey(Package, related_name='batches')
    date_from = models.DateField()
    date_to = models.DateField()

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name="batches_created")
    modified_by = models.ForeignKey(User, related_name="batches_modified")

class Remark(models.Model):
    package = models.ForeignKey(Package, related_name='remarks')
    remarks = models.CharField(max_length=2048)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name="remarks_created")
    modified_by = models.ForeignKey(User, related_name="remarks_modified")

class PackageHotel(models.Model):
    package = models.ForeignKey(Package, related_name='package_hotels')
    hotel = models.ForeignKey(Hotel, related_name='package_hotels')
    room = models.ForeignKey(Room, related_name='package_hotels')
    length_of_stay = models.IntegerField()
    transfer = models.ForeignKey(Transfer)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name="package_hotel_created")
    modified_by = models.ForeignKey(User, related_name="package_hotel_modified")
