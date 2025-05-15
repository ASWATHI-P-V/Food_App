from django.db import models


class user_tb(models.Model):
	name=models.CharField(max_length=100,default='')
	address=models.CharField(max_length=100,default='')
	place=models.CharField(max_length=100,default='')
	email=models.CharField(max_length=100,default='')
	contact=models.CharField(max_length=100,default='')
	password=models.CharField(max_length=100,default='')


class add_products_tb(models.Model):
	Name=models.CharField(max_length=100,default='')
	Category=models.CharField(max_length=100,default='')
	Description=models.CharField(max_length=100,default='')
	Price=models.CharField(max_length=100,default='')
	Image=models.ImageField(upload_to='products')
	Availableqty=models.CharField(max_length=100,default='')
	status=models.CharField(max_length=100,default='')
		

class booking_tb(models.Model):	
	name=models.CharField(max_length=30,default='')
	time=models.CharField(max_length=30,default='')
	status=models.CharField(max_length=100,default='')
	pid=models.ForeignKey(add_products_tb, on_delete=models.CASCADE)
	uid=models.ForeignKey(user_tb, on_delete=models.CASCADE)

class adminlogin_tb(models.Model):
	email=models.CharField(max_length=100,default='')
	password=models.CharField(max_length=100,default='')