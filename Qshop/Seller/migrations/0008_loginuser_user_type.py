# Generated by Django 2.1.8 on 2019-09-09 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seller', '0007_auto_20190909_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='loginuser',
            name='user_type',
            field=models.IntegerField(default=0),
        ),
    ]
