# Generated by Django 2.2.6 on 2019-10-10 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('bookname', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('author', models.CharField(max_length=50)),
                ('publisheddate', models.DateField()),
                ('Noofbooks', models.IntegerField()),
                ('rackno', models.IntegerField()),
            ],
        ),
    ]
