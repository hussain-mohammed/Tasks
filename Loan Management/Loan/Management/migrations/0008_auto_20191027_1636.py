# Generated by Django 2.2.6 on 2019-10-27 16:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0007_auto_20191027_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loandetail',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
