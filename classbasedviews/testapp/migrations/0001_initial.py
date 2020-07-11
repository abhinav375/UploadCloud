# Generated by Django 3.0.3 on 2020-07-10 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('taste', models.CharField(max_length=80)),
                ('color', models.CharField(max_length=80)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
