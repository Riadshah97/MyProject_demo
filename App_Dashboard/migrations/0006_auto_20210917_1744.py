# Generated by Django 2.1.11 on 2021-09-17 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App_Dashboard', '0005_taxicompany'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taxicompany',
            name='country',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='country_info', to='App_Dashboard.Country'),
        ),
    ]
