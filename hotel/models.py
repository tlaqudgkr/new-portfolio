from django.db import models


# Create your models here.

class Hotel(models.Model):
    name = models.CharField(max_length=50)
    text = models.TextField()
    lon = models.FloatField()
    lat = models.FloatField()
    zoom = models.PositiveSmallIntegerField(default=14)
    site = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):
    STANDARD_DOUBLE = 'SD'
    STANDARD_TWIN = 'ST'
    STANDARD_ONDOL = 'SO'
    DELUXE_DOUBLE = 'DD'
    DELUXE_TWIN = 'DT'
    DELUXE_ONDOL = 'DO'
    SUITE_ROOM = 'SR'
    ROOM_NAME_CHOICES = (
        (STANDARD_DOUBLE, 'Standard double'),
        (STANDARD_TWIN, 'Standard twin'),
        (STANDARD_ONDOL, 'Standard ondol'),
        (DELUXE_DOUBLE, 'Deluxe double'),
        (DELUXE_TWIN, 'Deluxe twin'),
        (DELUXE_ONDOL, 'Deluxe ondol'),
        (SUITE_ROOM, 'Suite room'),
    )
    roomname = models.CharField(max_length=2, choices=ROOM_NAME_CHOICES, null=True, blank=True,)
    hotel = models.ForeignKey(Hotel)

    def __str__(self):
        return self.roomname

class Facility(models.Model):
    RESTAURANT = 'RE'
    CAFE = 'CF'
    BANQUET_HALL = 'BH'
    SEMINAR_ROOM = 'SR'
    CONFERENCE_ROOM = 'CR'
    BUSINESS_CENTER = 'BC'
    FITNESS_CENTER = 'FC'
    MASSAGE = 'MA'
    SPA = 'SP'
    SAUNA = 'SN'
    SWIMMING_POOL = 'SW'
    FACILITY_NAME_CHOICES = (
        (RESTAURANT, 'Restaurant'),
        (CAFE, 'Cafe'),
        (BANQUET_HALL, 'Banquet hall'),
        (SEMINAR_ROOM, 'Seminar room'),
        (CONFERENCE_ROOM, 'Conference room'),
        (BUSINESS_CENTER, 'Business center'),
        (FITNESS_CENTER, 'Fitness center'),
        (MASSAGE, 'Massage'),
        (SPA, 'Spa'),
        (SAUNA, 'Sauna'),
        (SWIMMING_POOL, 'Swimming pool'),
    )
    facilityname = models.CharField(max_length=2, choices=FACILITY_NAME_CHOICES, null=True, blank=True,)
    hotel = models.ForeignKey(Hotel)

    def __str__(self):
        return self.facilityname

