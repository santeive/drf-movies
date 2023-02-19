# Generated by Django 4.1.7 on 2023-02-19 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title assgned to the movie', max_length=100)),
                ('description', models.CharField(help_text="Movie's description", max_length=250)),
                ('image', models.CharField(help_text='Image for the movie', max_length=250)),
                ('stock', models.IntegerField()),
                ('rental_price', models.FloatField()),
                ('sale_price', models.FloatField()),
                ('availability', models.BooleanField()),
            ],
        ),
    ]