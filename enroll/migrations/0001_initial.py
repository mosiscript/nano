# Generated by Django 2.2.3 on 2019-09-16 05:57

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enroll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='نام')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('mobile', models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(message='شماره وارد شده صحیح نیست', regex='^(09)\\d{9,9}$')])),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'ثبت نام',
                'verbose_name_plural': 'ثبت نام ها',
            },
        ),
    ]
