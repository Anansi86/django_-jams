# Generated by Django 4.1.3 on 2022-11-18 00:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jamapp', '0004_playlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='genre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='jamapp.genre'),
        ),
    ]
