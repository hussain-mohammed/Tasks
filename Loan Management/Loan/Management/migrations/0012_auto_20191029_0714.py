# Generated by Django 2.2.6 on 2019-10-29 07:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0011_auto_20191029_0707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loandetail',
            name='duration',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(30, 'you cannot avail loan for more than 30 days')]),
        ),
    ]
