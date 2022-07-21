from email.headerregistry import Address
from django.db import models

# Create your models here.

class Place(models.Model):
    name = models.CharField(max_length=100)  #place 이름
    address = models.CharField(max_length=150, default="", blank=True)   #주소
    phone_number = models.CharField(max_length=30, default="", blank=True)   #전화번호
    business_hour = models.CharField(max_length=100, default="", blank=True)   #영업시간

    def __str__(self):
        return self.name