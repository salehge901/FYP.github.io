# Generated by Django 3.2.3 on 2021-05-23 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_alter_questionbank_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionbank',
            name='time',
            field=models.IntegerField(max_length=1),
        ),
    ]
