# Generated by Django 3.0.7 on 2020-06-12 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CUSTOMER', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]