# Generated by Django 3.0 on 2022-06-13 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oc_lettings_site', '0003_auto_20220615_1930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='letting',
            name='address',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='Letting',
        ),
    ]
