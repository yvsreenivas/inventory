# Generated by Django 2.1.15 on 2021-02-24 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0002_auto_20210222_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='part_no',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
