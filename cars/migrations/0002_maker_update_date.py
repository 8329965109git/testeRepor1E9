# Generated by Django 3.2 on 2023-10-22 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='maker',
            name='update_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
