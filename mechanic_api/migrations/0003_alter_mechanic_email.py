# Generated by Django 3.2 on 2021-06-02 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mechanic_api', '0002_auto_20210602_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mechanic',
            name='email',
            field=models.CharField(max_length=50),
        ),
    ]
