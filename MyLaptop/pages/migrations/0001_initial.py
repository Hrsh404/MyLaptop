# Generated by Django 4.1.1 on 2023-06-06 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('monthlySales', models.IntegerField()),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('facebookLink', models.URLField(max_length=100)),
                ('twitterLink', models.URLField(max_length=100)),
                ('googleLink', models.URLField(max_length=100)),
                ('createdData', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
