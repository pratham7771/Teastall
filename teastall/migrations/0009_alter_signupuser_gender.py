# Generated by Django 3.2.9 on 2022-02-18 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teastall', '0008_paymentuser_cpay'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signupuser',
            name='gender',
            field=models.CharField(max_length=15),
        ),
    ]