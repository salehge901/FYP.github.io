# Generated by Django 3.1.7 on 2021-04-11 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vib', '0003_extend_company_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extend',
            name='company_name',
            field=models.CharField(max_length=50),
        ),
    ]
