# Generated by Django 2.2.6 on 2019-10-30 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0014_auto_20191030_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loandetail',
            name='amountPaid',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='loandetail',
            name='returnedIN',
            field=models.IntegerField(default='0'),
        ),
    ]