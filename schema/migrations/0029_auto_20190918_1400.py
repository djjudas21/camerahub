# Generated by Django 2.2.4 on 2019-09-18 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0028_auto_20190918_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='enlarger',
            name='light_source',
            field=models.CharField(blank=True, choices=[('Incandescent', 'Incandescent'), ('Cold cathode', 'Cold cathode'), ('LED', 'LED')], help_text='The type of light source used in the enlarger', max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='enlarger',
            name='type',
            field=models.CharField(blank=True, choices=[('Diffusion', 'Diffusion'), ('Condenser', 'Condenser')], help_text='The type of optical system in the enlarger', max_length=15, null=True),
        ),
    ]