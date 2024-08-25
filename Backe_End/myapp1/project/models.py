


from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/', null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)


groups = models.ManyToManyField(
    Group,
    related_name='customuser_set',  # Измените на уникальное имя
    blank=True,
    help_text='The groups this user belongs to.',
    related_query_name='customuser',
)

user_permissions = models.ManyToManyField(
    Permission,
    related_name='customuser_set',  # Измените на уникальное имя
    blank=True,
    help_text='Specific permissions for this user.',
    related_query_name='customuser',
)
class Store(models.Model):
    CustomUser = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    price = models.IntegerField()
    count = models.IntegerField()

class Photo(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='photos')
    photo = models.ImageField(upload_to='photos')



# class Card (models.Model):
#     id = models.AutoField(primary_key=True)
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     date = models.DateField()
#     products = models.ManyToManyField(Store, through='CardProduct')
#


class CardProduct(models.Model):
    # card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='card_products')
    product = models.ForeignKey(Store, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    class Meta:
        unique_together = ['product']