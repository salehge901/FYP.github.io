# Generated by Django 3.2.3 on 2021-05-25 13:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company', '0006_alter_questionbank_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('schduele_time', models.DateTimeField(verbose_name='')),
                ('apply_date', models.DateTimeField(auto_now_add=True)),
                ('interview_status', models.BooleanField(default=False)),
                ('confirm_status', models.BooleanField(default=False)),
                ('video_link', models.CharField(max_length=200)),
                ('result', models.CharField(max_length=200)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.jobs')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]