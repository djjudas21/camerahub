# Generated by Django 2.2.16 on 2020-10-23 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0094_auto_20201022_1314'),
    ]

    operations = [
        migrations.RenameField(
            model_name='film',
            old_name='dev_uses',
            new_name='developer_previous_uses',
        ),
        migrations.RenameField(
            model_name='film',
            old_name='dev_n',
            new_name='development_compensation',
        ),
        migrations.RenameField(
            model_name='film',
            old_name='dev_temp',
            new_name='development_temperature',
        ),
        migrations.RenameField(
            model_name='film',
            old_name='dev_time',
            new_name='development_time',
        ),
    ]
