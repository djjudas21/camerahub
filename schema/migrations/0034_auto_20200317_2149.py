# Generated by Django 2.2 on 2020-03-17 21:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0033_auto_20200317_1416'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='filter',
            options={'ordering': ['type'], 'verbose_name_plural': 'filters'},
        ),
        migrations.RemoveField(
            model_name='filter',
            name='id_owner',
        ),
        migrations.RemoveField(
            model_name='filter',
            name='manufacturer',
        ),
        migrations.RemoveField(
            model_name='filter',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='filter',
            name='qty',
        ),
        migrations.RemoveField(
            model_name='filter',
            name='thread',
        ),
    ]