# Generated by Django 3.2.3 on 2021-05-25 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0007_interview'),
    ]

    operations = [
        migrations.AddField(
            model_name='interview',
            name='company',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]