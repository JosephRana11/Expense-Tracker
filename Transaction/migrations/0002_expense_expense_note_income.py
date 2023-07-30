# Generated by Django 4.2.2 on 2023-07-30 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Capital', '0004_alter_wallet_wallet_edited_date'),
        ('Transaction', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='expense_note',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('income_type', models.CharField(choices=[('Salary', 'Salary'), ('Commison', 'Commison'), ('Debt Collection', 'Debt Collection'), ('Gift', 'Gift'), ('Miscellaneous', 'Miscellaneous')], max_length=50)),
                ('income_date', models.DateField(auto_now_add=True)),
                ('income_note', models.CharField(max_length=200, null=True)),
                ('parent_wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Capital.wallet')),
            ],
        ),
    ]