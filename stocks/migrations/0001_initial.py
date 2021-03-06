# Generated by Django 2.1.15 on 2021-02-20 10:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Asset', 'Asset'), ('Consumables', 'Consumables')], max_length=15)),
                ('part_no', models.CharField(max_length=12)),
                ('item_no', models.CharField(blank=True, max_length=25, null=True)),
                ('HSN_code', models.CharField(blank=True, max_length=10, null=True)),
                ('item_name', models.CharField(blank=True, max_length=50, null=True)),
                ('manufacturer', models.CharField(blank=True, max_length=50, null=True)),
                ('quantity', models.IntegerField(blank=True, default='0', null=True)),
                ('units', models.CharField(choices=[('Kgs', 'Kgs'), ('Nos', 'Nos'), ('Ltrs', 'Ltrs')], max_length=5)),
                ('rate', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('receive_quantity', models.IntegerField(blank=True, default='0', null=True)),
                ('receive_rate', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('receive_by', models.CharField(blank=True, max_length=50, null=True)),
                ('issue_quantity', models.IntegerField(blank=True, default='0', null=True)),
                ('issue_by', models.CharField(blank=True, max_length=50, null=True)),
                ('issue_to', models.CharField(blank=True, max_length=50, null=True)),
                ('created_by', models.CharField(blank=True, max_length=50, null=True)),
                ('reorder_level', models.IntegerField(blank=True, default='0', null=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('export_to_CSV', models.BooleanField(default=False)),
                ('updated_by', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portfolio_site', models.URLField(blank=True)),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='stock',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stocks.SubCategory'),
        ),
    ]
