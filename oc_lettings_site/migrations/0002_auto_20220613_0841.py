# Generated by Django 3.0 on 2022-06-13 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oc_lettings_site', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name': 'address', 'verbose_name_plural': 'addresses'},
        ),
        migrations.AlterModelOptions(
            name='letting',
            options={'verbose_name': 'letting', 'verbose_name_plural': 'lettings'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'profile', 'verbose_name_plural': 'profiles'},
        ),
    ]
