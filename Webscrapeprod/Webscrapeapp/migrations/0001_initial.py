# Generated by Django 5.0 on 2023-12-11 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scrap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
                ('sitename', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
    ]
