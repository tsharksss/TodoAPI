from django.contrib.auth.models import User
from django.db import models


class DocumentType(models.Model):
    name = models.CharField(max_length=100)


class ModelsUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    doc_type = models.ForeignKey(DocumentType, on_delete=models.CASCADE)
    series = models.IntegerField()
    number = models.IntegerField()
    date_of_issue = models.DateField()
    issued = models.CharField(max_length=150)
    mobile = models.CharField(max_length=20)


class City(models.Model):
    name = models.CharField(max_length=120)


class Street(models.Model):
    name = models.CharField(max_length=120)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)


class Cargo(models.Model):
    name = models.CharField(max_length=120)
    value = models.FloatField(max_length=10)
    description = models.TextField(blank=True)


class Sending(models.Model):
    user = models.ForeignKey(ModelsUser, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    cargo = models.ManyToManyField(Cargo)
    street = models.ForeignKey(Street, on_delete=models.CASCADE)
    house = models.CharField(max_length=5, blank=True)
    description = models.TextField(blank=True)

    @property
    def address(self):
        return self.street.city.name + ' ' + self.street.name


class CarModel(models.Model):
    name = models.CharField(max_length=120)


class CarMark(models.Model):
    name = models.CharField(max_length=120)
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)

    @property
    def full_name(self):
        return self.car_model.name + ' ' + self.name

    def __str__(self):
        return self.full_name


class Delivery(models.Model):
    sending = models.ManyToManyField(Sending)
    user = models.ForeignKey(ModelsUser, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    car = models.ForeignKey(CarMark, on_delete=models.CASCADE)
    number_of_the_car = models.CharField(max_length=6)
    status_choice = (
        ('В ожидании', 'Awaiting'),
        ('В пути', 'In transit'),
        ('Доставлен', 'Delivered')
    )
    status = models.CharField(max_length=10, choices=status_choice)
