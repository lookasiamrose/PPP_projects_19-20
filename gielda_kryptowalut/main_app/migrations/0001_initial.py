# Generated by Django 3.0 on 2019-12-07 14:56

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
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortname', models.CharField(max_length=3)),
                ('name', models.CharField(max_length=255)),
                ('logopath', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('funds', models.DecimalField(decimal_places=8, max_digits=20)),
                ('currencyid', models.ForeignKey(on_delete=models.SET(1), to='main_app.Currency')),
                ('userid', models.ForeignKey(on_delete=models.SET(1), to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('SELL', 'Sell'), ('BUY', 'Buy'), ('Undefined', 'N/A')], default='Undefined', max_length=10)),
                ('ratetobtc', models.DecimalField(decimal_places=8, max_digits=12)),
                ('quantity', models.DecimalField(decimal_places=8, max_digits=20)),
                ('status', models.CharField(choices=[('OPEN', 'Open'), ('CLOSED', 'Closed'), ('Undefined', 'N/A')], default='Undefined', max_length=10)),
                ('currencyid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Currency')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]