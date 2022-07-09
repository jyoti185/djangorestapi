from django.db import models


class EmployeeModels(models.Model):
    id = models.AutoField(primary_key=True, )
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_no = models.IntegerField(unique=True)
    gender = models.CharField(max_length=20)
    address = models.CharField(max_length=100)


