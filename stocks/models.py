from django.db import models
from django.contrib.auth.models import User

category_choice = (
		('Asset', 'Asset'),
		('Consumables', 'Consumables'),
	)

units_choice = (
			('Kgs', 'Kgs'),
			('Nos', 'Nos'),
			('Ltrs', 'Ltrs'),
	)

class UserProfileInfo(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	portfolio_site = models.URLField(blank=True)
	profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
	def __str__(self):
	  return self.user.username

class SubCategory(models.Model):
	name = models.CharField(max_length=50, blank=False, null=False)
	def __str__(self):
		return self.name


class Stock(models.Model):
	category = models.CharField(max_length=15,blank=False,null=False,
					choices=category_choice)
	subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
	part_no = models.CharField(max_length=13, blank=False, null=False)
	item_no = models.CharField(max_length=25, blank=True, null=True)
	HSN_code = models.CharField(max_length=10, blank=True, null=True)
	item_name = models.CharField(max_length=50, blank=True, null=True)
	manufacturer = models.CharField(max_length=50, blank=True, null=True)
	quantity = models.IntegerField(default='0', blank=True, null=True)
	units = models.CharField(max_length=5,blank=False,null=False,
					choices=units_choice)
	rate = models.DecimalField(decimal_places=2,max_digits=12,default=0)
	receive_quantity = models.IntegerField(default='0', blank=True, null=True)
	receive_rate = models.DecimalField(decimal_places=2,max_digits=12,default=0)
	receive_by = models.CharField(max_length=50, blank=True, null=True)
	issue_quantity = models.IntegerField(default='0', blank=True, null=True)
	issue_by = models.CharField(max_length=50, blank=True, null=True)
	issue_to = models.CharField(max_length=50, blank=True, null=True)
	created_by = models.CharField(max_length=50, blank=True, null=True)
	reorder_level = models.IntegerField(default='0', blank=True, null=True)
	last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated_by = models.CharField(max_length=50, blank=False, null=False)

	def __str__(self):
		return self.item_name
