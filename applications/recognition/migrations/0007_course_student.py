# Generated by Django 2.2.4 on 2020-02-19 22:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recognition', '0006_auto_20200129_1359'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.IntegerField(choices=[(1, 'Active'), (0, 'Passive'), (-1, 'Deleted'), (2, 'Waiting')], default=1)),
                ('student_id', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': 'Students',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.IntegerField(choices=[(1, 'Active'), (0, 'Passive'), (-1, 'Deleted'), (2, 'Waiting')], default=1)),
                ('title', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]