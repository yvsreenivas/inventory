from django import forms
from .models import Stock
from stocks.models import UserProfileInfo
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')


class UserProfileInfoForm(forms.ModelForm):
     class Meta():
         model = UserProfileInfo
         fields = ('portfolio_site','profile_pic')


class StockCreateForm(forms.ModelForm):
  class Meta:
    model = Stock
    fields = ['category', 'sub_category', 'part_no', 'item_no',
    'HSN_code', 'item_name', 'quantity', 'stock_units']

  def clean_category(self):
    category = self.cleaned_data.get('category')
    if not category:
      raise forms.ValidationError('This field is required')
    return category

  def clean_sub_category(self):
    sub_category = self.cleaned_data.get('sub_category')
    if not sub_category:
      raise forms.ValidationError('This field is required')
    return sub_category

  def clean_part_no(self):
    part_no = self.cleaned_data.get('part_no')
    if not part_no:
      raise forms.ValidationError('This field is required')

    stocks = Stock.objects.all()
    for instance in stocks:
        if instance.part_no == part_no:
            raise forms.ValidationError(part_no + " exists")
    return part_no

  def clean_item_no(self):
    item_no = self.cleaned_data.get('item_no')
    if not item_no:
      raise forms.ValidationError('This field is required')
    return item_no

  def clean_HSN_code(self):
    HSN_code = self.cleaned_data.get('HSN_code')
    if not HSN_code:
      raise forms.ValidationError('This field is required')
    return HSN_code

  def clean_stock_units(self):
    stock_units = self.cleaned_data.get('stock_units')
    if not stock_units:
      raise forms.ValidationError('This field is required')
    return stock_units

  def clean_item_name(self):
    item_name = self.cleaned_data.get('item_name')
    if not item_name:
      raise forms.ValidationError('This field is required')

    stocks = Stock.objects.all()
    for instance in stocks:
      if instance.item_name == item_name:
        raise forms.ValidationError(item_name + " exists")
    return item_name

  
class StockSearchForm(forms.ModelForm):
  class Meta:
    model = Stock
    fields = ['item_name']


class StockUpdateForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['category', 'sub_category', 'item_name', 'quantity']


class IssueForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['issue_quantity', 'issue_to']


class ReceiveForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['receive_quantity']
