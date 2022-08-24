from email.headerregistry import Address
from email.policy import default
from unicodedata import category
from django.db import models
from django.urls import reverse
from uuid import uuid4
from django.utils import timezone
import os

class Category(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("home")

class Place(models.Model):

    name = models.CharField(max_length=100)  #place 이름
    address = models.CharField(max_length=150, default="", blank=True)   #주소
    phone_number = models.CharField(max_length=30, default="", blank=True)   #전화번호
    business_hour = models.CharField(max_length=100, default="", blank=True)   #영업시간
    photo = models.ImageField(upload_to="place/photo", blank=True)   #place 이미지
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    @property
    def get_photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        else:
            return '/static/mainapp/images/notfoundimage.png'