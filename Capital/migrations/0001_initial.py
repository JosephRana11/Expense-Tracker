# Generated by Django 4.2.2 on 2023-07-28 16:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wallet_name', models.CharField(max_length=70)),
                ('wallet_capital', models.DecimalField(decimal_places=2, max_digits=12)),
                ('wallet_currency', models.CharField(choices=[('USD', 'USD'), ('NPR', 'NPR'), ('INR', 'INR'), ('YEN', 'YEN')], max_length=20)),
                ('wallet_creation_date', models.DateField(auto_now_add=True)),
                ('wallet_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]