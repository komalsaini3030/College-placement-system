# Generated by Django 3.1.3 on 2022-05-27 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCampusPlacement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companydetails11',
            name='File',
            field=models.FileField(default=None, null=True, upload_to='media'),
        ),
    ]
