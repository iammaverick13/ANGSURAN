# Generated by Django 3.0.7 on 2020-06-12 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CUSTOMER', '0003_auto_20200612_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
