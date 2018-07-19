from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
#from phonenumber_field.modelfields import PhoneNumberField

class Imarts(models.Model):
	user = models.OneToOneField(User,on_delete = models.CASCADE)
	student_name = models.CharField(max_length = 50)
	email = models.EmailField(max_length=254)
	#phone_number = PhoneNumberField(max_length=15)
	phone_number = models.CharField(max_length = 15)
	def __str__(self):
		return self.student_name

