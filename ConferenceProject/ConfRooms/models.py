from django.db import models

# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=255, unique=True)
    capacity = models.SmallIntegerField()
    projector = models.BooleanField(default=True)


class Booking(models.Model):
    date = models.DateField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255, blank=True)

    class Meta:
        unique_together = ('date', 'room_id',)