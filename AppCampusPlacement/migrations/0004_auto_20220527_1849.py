# Generated by Django 3.1.3 on 2022-05-27 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCampusPlacement', '0003_studentapplication_select_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentapplication',
            name='Select_status',
            field=models.CharField(default='Not Updated', max_length=100, null=True),
        ),
    ]
