# Generated by Django 3.1.7 on 2021-04-24 15:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='friends',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conn_user', models.CharField(max_length=50)),
                ('user_friend', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
