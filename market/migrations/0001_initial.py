# Generated by Django 2.2.5 on 2019-10-18 16:07

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
            name='Deal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Denied', 'Denied'), ('Access', 'Access')], default='Saved', max_length=6)),
                ('currency_code', models.CharField(max_length=3)),
                ('currency_rate', models.DecimalField(decimal_places=4, max_digits=4)),
                ('write_off_account', models.CharField(max_length=30)),
                ('income_account', models.CharField(max_length=30)),
                ('amount', models.DecimalField(decimal_places=4, max_digits=10)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='deals', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
