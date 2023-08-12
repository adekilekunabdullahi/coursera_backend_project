# Generated by Django 4.2.3 on 2023-08-12 09:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='reservation_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='reservation_slot',
            field=models.SmallIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='menu',
            name='menu_item_description',
            field=models.TextField(default='', max_length=1000),
        ),
    ]
