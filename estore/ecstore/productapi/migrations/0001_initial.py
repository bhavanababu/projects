# Generated by Django 4.0.6 on 2022-07-26 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('category', models.CharField(max_length=120)),
                ('price', models.PositiveIntegerField()),
                ('rating', models.FloatField()),
            ],
        ),
    ]
