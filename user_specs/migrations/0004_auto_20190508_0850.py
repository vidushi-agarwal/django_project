# Generated by Django 2.2 on 2019-05-08 03:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_specs', '0003_auto_20190508_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='my_user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
