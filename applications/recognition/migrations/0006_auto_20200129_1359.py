# Generated by Django 2.2.4 on 2020-01-29 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recognition', '0005_user_fullname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='fullname',
            field=models.CharField(max_length=255),
        ),
    ]
