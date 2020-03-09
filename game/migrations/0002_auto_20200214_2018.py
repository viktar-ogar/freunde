# Generated by Django 3.0.3 on 2020-02-14 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='date',
        ),
        migrations.RemoveField(
            model_name='game',
            name='end',
        ),
        migrations.RemoveField(
            model_name='game',
            name='start',
        ),
        migrations.RemoveField(
            model_name='players',
            name='effectivity',
        ),
        migrations.AlterField(
            model_name='game',
            name='number_players',
            field=models.IntegerField(verbose_name='Количество игроков'),
        ),
    ]