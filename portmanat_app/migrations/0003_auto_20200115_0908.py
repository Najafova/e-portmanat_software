# Generated by Django 3.0.1 on 2020-01-15 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portmanat_app', '0002_mobiledata'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='battery',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='mobiledata',
            name='battery',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
