# Generated by Django 2.2.6 on 2019-10-30 11:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0013_auto_20191029_0724'),
    ]

    operations = [
        migrations.AddField(
            model_name='loandetail',
            name='amountPaid',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='loandetail',
            name='returnedIN',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='loandetail',
            name='duration',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(30, 'you cannot avail loan for more than 30 days')]),
        ),
    ]
