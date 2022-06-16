from django.db import models


class BookingStatus(models.TextChoices):
    PENDING = "PENDING",
    COMPLETED = "COMPLETED",
    CANCEL = "CANCEL"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


class Booking(models.Model):
    house_id = models.IntegerField()
    tenant_id = models.IntegerField()
    price = models.PositiveBigIntegerField()
    check_in_time = models.DateTimeField(null=True)
    check_out_time = models.DateTimeField(null=True)
    status = models.CharField(max_length=50, choices=BookingStatus.choices(), default=BookingStatus.PENDING)
    created_date = models.DateField()
    created_by = models.IntegerField()
    note = models.CharField(max_length=1500)
