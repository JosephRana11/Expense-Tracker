# Generated by Django 4.2.2 on 2023-07-28 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_main_wallet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='main_wallet',
        ),
    ]
