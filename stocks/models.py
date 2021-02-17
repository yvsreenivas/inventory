from django.db import models
from django.contrib.auth.models import User

sub_category_choice = (
		('Asset', 'Asset'),
		('Liability', 'Liability'),
	)

units = (
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

class Category(models.Model):
	name = models.CharField(max_length=50, blank=False, null=False)
	def __str__(self):
		return self.name


class Stock(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	sub_category = models.CharField(max_length=10,blank=False,null=False,
					choices=sub_category_choice)

	part_no = models.CharField(max_length=12, blank=False, null=False)
	item_no = models.CharField(max_length=25, blank=False, null=False)
	HSN_code = models.CharField(max_length=10, blank=True, null=True)
	item_name = models.CharField(max_length=50, blank=True, null=True)
	quantity = models.IntegerField(default='0', blank=True, null=True)
	stock_units = models.CharField(max_length=5,blank=False,null=False,
					choices=units)
	receive_quantity = models.IntegerField(default='0', blank=True, null=True)
	receive_by = models.CharField(max_length=50, blank=True, null=True)
	issue_quantity = models.IntegerField(default='0', blank=True, null=True)
	issue_by = models.CharField(max_length=50, blank=True, null=True)
	issue_to = models.CharField(max_length=50, blank=True, null=True)
	phone_number = models.CharField(max_length=50, blank=True, null=True)
	created_by = models.CharField(max_length=50, blank=True, null=True)
	reorder_level = models.IntegerField(default='0', blank=True, null=True)
	last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	export_to_CSV = models.BooleanField(default=False)
	updated_by = models.CharField(max_length=50, blank=False, null=False)

	def __str__(self):
		return self.item_name
