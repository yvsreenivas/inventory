from django.test import TestCase
from django.contrib.auth.models import User
from stocks.models import Stock, SubCategory, Issues

class ModelTest(TestCase):

    @classmethod
    def setUpClass(cls):

        # below code will fix AttributeError: type object 'Model Test' has no attribute 'cls_atomics' error.
        super(ModelTest, cls).setUpClass()

        # create and save a Department object.
        sub = SubCategory(name="Furniture")
        sub.save()
        # create a User model object in temporary database.
        user = User(username='tom', password='tom')
        user.save()

        # get employee user.
        user = User.objects.get(username='tom')
        print('Added user data : ')
        print(user)
        print('')


        sub = SubCategory.objects.get(name='Furniture')
        print('Added Sub Category data : ')
        print(sub)
        print('')

        # create and save the Employee object.
        stk = Stock(
        category="Asset",
        subcategory=sub,
        part_no="90000000000",
        item_no="AIS1",
        item_name='testname',
        updated_by = user
        )
        stk.save()
        print('Added stock data : ')
        print(stk)

        # create and save the Employee object.
        iss = Issues(
        stock=stk,
        issue_quantity=10,
        updated_by = user
        )
        iss.save()
        print('Added issue : ')
        print(iss)


    def test_subcategory_models(self):
        sub = SubCategory.objects.get(name='Furniture')
        self.assertEqual(sub.name,'Furniture')

    def test_stock_models(self):
        stk = Stock.objects.get(item_name="testname")
        self.assertEqual(stk.updated_by, 'tom')
