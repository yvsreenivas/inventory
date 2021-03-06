# Generated by Django 2.1.15 on 2021-02-25 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0004_auto_20210224_1300'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_quantity', models.DecimalField(blank=True, decimal_places=2, default='0', max_digits=10, null=True)),
                ('units', models.CharField(choices=[('Kgs', 'Kgs'), ('gms', 'Gms'), ('Nos', 'Nos'), ('Ltrs', 'Ltrs'), ('Mtrs', 'Mtrs')], max_length=5)),
                ('issue_to', models.CharField(blank=True, max_length=10, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='stock',
            name='units',
            field=models.CharField(choices=[('Kgs', 'Kgs'), ('gms', 'Gms'), ('Nos', 'Nos'), ('Ltrs', 'Ltrs'), ('Mtrs', 'Mtrs')], max_length=5),
        ),
        migrations.AddField(
            model_name='issues',
            name='stock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stocks.Stock'),
        ),
    ]
