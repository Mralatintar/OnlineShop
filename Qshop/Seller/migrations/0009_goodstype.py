# Generated by Django 2.1.8 on 2019-09-09 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seller', '0008_loginuser_user_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_label', models.CharField(max_length=32)),
                ('type_description', models.TextField()),
            ],
        ),
    ]
