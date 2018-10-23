# Generated by Django 2.1.1 on 2018-10-23 13:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0005_auto_20181023_0041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='my_user',
        ),
        migrations.AddField(
            model_name='car',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
