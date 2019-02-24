# Generated by Django 2.1.5 on 2019-02-24 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cryptoserver', '0002_auto_20190224_0632'),
    ]

    operations = [
        migrations.AddField(
            model_name='bond',
            name='cleared',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='bond',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cryptoserver.Trader'),
        ),
    ]
