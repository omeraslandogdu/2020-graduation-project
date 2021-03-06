# Generated by Django 2.2.4 on 2020-01-28 19:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EntityType',
            fields=[
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.IntegerField(choices=[(1, 'Active'), (0, 'Passive'), (-1, 'Deleted'), (2, 'Waiting')], default=1)),
                ('title', models.CharField(max_length=255)),
                ('key', models.CharField(db_index=True, max_length=255)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.IntegerField(choices=[(1, 'Active'), (0, 'Passive'), (-1, 'Deleted'), (2, 'Waiting')], default=1)),
                ('title', models.CharField(help_text='Title of user type for related entity_type.', max_length=255)),
                ('entity_type', models.ForeignKey(help_text='Entity type id for user type.', on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_type', to='recognition.EntityType')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='recognition.User')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='UserToken',
            fields=[
                ('key', models.CharField(max_length=40, primary_key=True, serialize=False, verbose_name='Key')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='auth_token', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name_plural': 'Tokens',
                'abstract': False,
                'db_table': 'client_token',
                'verbose_name': 'Token',
            },
        ),
        migrations.AddField(
            model_name='entitytype',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='recognition.User'),
        ),
        migrations.AlterUniqueTogether(
            name='entitytype',
            unique_together={('user', 'key')},
        ),
    ]
