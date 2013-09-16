from datetime import datetime, date
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from hotels.models import Hotel, Rate
from references.models import Room, Transfer, ExchangeRate

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

    def get_absolute_url(self, *args, **kwargs):
        return reverse('packages:table', args=[self.pk])

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

    def get_total(self, amount, persons=1, is_child=False):
        now = datetime.now()
        xrate = ExchangeRate.objects.filter(date_from__lte=now, date_to__gte=now)
        if xrate.count() == 0:
            raise Exception("No exchange rate for today, define exchange rate ranging within today")
        else:
            xrate = xrate[0]


        cut = float(2) if is_child else float(1)
        #total = float((float(float(self.package.markup_amount) / float(cut)) + float(float(amount)/float(persons))) / float(xrate.rate))
        total = amount + (float(self.package.markup_amount) / cut)
        total /= persons
        total /= float(xrate.rate)

        return "USD %s" % round(total,2)

    def get_hotels_total_rate(self, persons=1, extra_bed=False):
        total_rate = 0
        for h in self.package.package_hotels.all():
            hotel = h.hotel
            room = h.room
            rates = Rate.objects.filter(hotel=hotel, room=room)
            rate_found = False
            for r in rates:
                d1 = date(r.date_from_year, r.date_from_month, r.date_from_day)
                d2 = date(r.date_to_year, r.date_to_month, r.date_to_day)
                if self.date_from >= d1 and self.date_to <= d2:
                    if not rate_found:
                        rate_found = True
                        rate = r.rate

                        rate *= h.number_of_nights


                        if persons < 3:
                            rate += 0 * h.number_of_bonus_nights
                        else:
                            rate += hotel.adult_extra_bed_rate * h.number_of_nights
                            rate += hotel.adult_extra_bed_rate * h.number_of_bonus_nights

                        rate += hotel.adult_breakfast_rate * persons * h.number_of_bonus_nights

                        total_rate += rate


        return round(total_rate,2)

    def get_hotels_total_child_rate(self, with_bed=True):
        total_rate = 0
        for h in self.package.package_hotels.all():
            hotel = h.hotel
            if with_bed:
                rate = hotel.child_with_bed_rate
                rate *= h.number_of_nights
                rate += hotel.child_with_bed_rate * h.number_of_bonus_nights
            else:
                rate = hotel.child_breakfast_rate * h.number_of_nights
                rate += hotel.child_breakfast_rate * h.number_of_bonus_nights

            total_rate += rate
        return round(total_rate, 2)

    def get_transfer_rate(self, persons=1, with_child=False):
        total_rate = 0
        for h in self.package.package_hotels.all():
            rate = h.transfer.rate * 2
            rate /= 4 if with_child else 1
            total_rate += rate
        return round(total_rate, 2)

    def get_single(self): return self.get_total(self.get_hotels_total_rate() + self.get_transfer_rate())

    def get_double(self): return self.get_total(self.get_hotels_total_rate(persons=2) + self.get_transfer_rate(persons=2), persons=2)

    def get_triple(self): return self.get_total(self.get_hotels_total_rate(persons=3, extra_bed=True) + self.get_transfer_rate(persons=3), persons=3)

    def get_child_with_bed(self): return self.get_total(self.get_hotels_total_child_rate() + self.get_transfer_rate(with_child=True))

    def get_child_without_bed(self): return self.get_total(self.get_hotels_total_child_rate(with_bed=False) + self.get_transfer_rate(with_child=True))

    def get_hotel_single(self): return self.get_total(self.get_hotels_total_rate())

    def get_hotel_double(self): return self.get_total(self.get_hotels_total_rate(persons=2))

    def get_hotel_triple(self): return self.get_total(self.get_hotels_total_rate(persons=3, extra_bed=True))

    def get_hotel_child_with_bed(self): return self.get_total(self.get_hotels_total_child_rate())

    def get_hotel_child_without_bed(self): return self.get_total(self.get_hotels_total_child_rate(with_bed=False))

    def get_transfer_single(self): return self.get_total(self.get_transfer_rate())

    def get_transfer_double(self): return self.get_total(self.get_transfer_rate(persons=2))

    def get_transfer_triple(self): return self.get_total(self.get_transfer_rate(persons=3))

    def get_transfer_child_with_bed(self): return self.get_total(self.get_transfer_rate(with_child=True))

    def get_transfer_child_without_bed(self): return self.get_total(self.get_transfer_rate(with_child=True))

    class Meta:
        ordering = ('id',)

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
    number_of_nights = models.IntegerField()
    number_of_bonus_nights = models.IntegerField()
    transfer = models.ForeignKey(Transfer, blank=True, null=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name="package_hotel_created")
    modified_by = models.ForeignKey(User, related_name="package_hotel_modified")
