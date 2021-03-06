# Generated by Django 2.2.4 on 2019-12-17 23:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('schema', '0017_auto_20191108_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='accessory',
            name='id_owner',
            field=models.PositiveIntegerField(
                blank=True, help_text='Per-user incrementing number', null=True),
        ),
        migrations.AddField(
            model_name='archive',
            name='id_owner',
            field=models.PositiveIntegerField(
                blank=True, help_text='Per-user incrementing number', null=True),
        ),
        migrations.AddField(
            model_name='bulkfilm',
            name='id_owner',
            field=models.PositiveIntegerField(
                blank=True, help_text='Per-user incrementing number', null=True),
        ),
        migrations.AddField(
            model_name='camera',
            name='id_owner',
            field=models.PositiveIntegerField(
                blank=True, help_text='Per-user incrementing number', null=True),
        ),
        migrations.AddField(
            model_name='enlarger',
            name='id_owner',
            field=models.PositiveIntegerField(
                blank=True, help_text='Per-user incrementing number', null=True),
        ),
        migrations.AddField(
            model_name='film',
            name='id_owner',
            field=models.PositiveIntegerField(
                blank=True, help_text='Per-user incrementing number', null=True),
        ),
        migrations.AddField(
            model_name='filter',
            name='id_owner',
            field=models.PositiveIntegerField(
                blank=True, help_text='Per-user incrementing number', null=True),
        ),
        migrations.AddField(
            model_name='flash',
            name='id_owner',
            field=models.PositiveIntegerField(
                blank=True, help_text='Per-user incrementing number', null=True),
        ),
        migrations.AddField(
            model_name='lens',
            name='id_owner',
            field=models.PositiveIntegerField(
                blank=True, help_text='Per-user incrementing number', null=True),
        ),
        migrations.AddField(
            model_name='mountadapter',
            name='id_owner',
            field=models.PositiveIntegerField(
                blank=True, help_text='Per-user incrementing number', null=True),
        ),
        migrations.AddField(
            model_name='negative',
            name='id_owner',
            field=models.PositiveIntegerField(
                blank=True, help_text='Per-user incrementing number', null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='id_owner',
            field=models.PositiveIntegerField(
                blank=True, help_text='Per-user incrementing number', null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='id_owner',
            field=models.PositiveIntegerField(
                blank=True, help_text='Per-user incrementing number', null=True),
        ),
        migrations.AddField(
            model_name='print',
            name='id_owner',
            field=models.PositiveIntegerField(
                blank=True, help_text='Per-user incrementing number', null=True),
        ),
        migrations.AddField(
            model_name='repair',
            name='id_owner',
            field=models.PositiveIntegerField(
                blank=True, help_text='Per-user incrementing number', null=True),
        ),
        migrations.AddField(
            model_name='scan',
            name='id_owner',
            field=models.PositiveIntegerField(
                blank=True, help_text='Per-user incrementing number', null=True),
        ),
        migrations.AddField(
            model_name='series',
            name='id_owner',
            field=models.PositiveIntegerField(
                blank=True, help_text='Per-user incrementing number', null=True),
        ),
        migrations.AddField(
            model_name='teleconverter',
            name='id_owner',
            field=models.PositiveIntegerField(
                blank=True, help_text='Per-user incrementing number', null=True),
        ),
        migrations.AlterUniqueTogether(
            name='accessory',
            unique_together={('id_owner', 'owner')},
        ),
        migrations.AlterUniqueTogether(
            name='archive',
            unique_together={('id_owner', 'owner')},
        ),
        migrations.AlterUniqueTogether(
            name='bulkfilm',
            unique_together={('id_owner', 'owner')},
        ),
        migrations.AlterUniqueTogether(
            name='camera',
            unique_together={('id_owner', 'owner'), ('cameramodel', 'serial')},
        ),
        migrations.AlterUniqueTogether(
            name='enlarger',
            unique_together={('id_owner', 'owner')},
        ),
        migrations.AlterUniqueTogether(
            name='film',
            unique_together={('id_owner', 'owner')},
        ),
        migrations.AlterUniqueTogether(
            name='filter',
            unique_together={('id_owner', 'owner')},
        ),
        migrations.AlterUniqueTogether(
            name='flash',
            unique_together={('id_owner', 'owner')},
        ),
        migrations.AlterUniqueTogether(
            name='lens',
            unique_together={('id_owner', 'owner'), ('lensmodel', 'serial')},
        ),
        migrations.AlterUniqueTogether(
            name='mountadapter',
            unique_together={('id_owner', 'owner')},
        ),
        migrations.AlterUniqueTogether(
            name='negative',
            unique_together={('id_owner', 'owner'), ('film', 'frame')},
        ),
        migrations.AlterUniqueTogether(
            name='order',
            unique_together={('id_owner', 'owner')},
        ),
        migrations.AlterUniqueTogether(
            name='person',
            unique_together={('id_owner', 'owner')},
        ),
        migrations.AlterUniqueTogether(
            name='print',
            unique_together={('id_owner', 'owner')},
        ),
        migrations.AlterUniqueTogether(
            name='repair',
            unique_together={('id_owner', 'owner')},
        ),
        migrations.AlterUniqueTogether(
            name='scan',
            unique_together={('id_owner', 'owner')},
        ),
        migrations.AlterUniqueTogether(
            name='series',
            unique_together={('id_owner', 'owner')},
        ),
        migrations.AlterUniqueTogether(
            name='teleconverter',
            unique_together={('id_owner', 'owner')},
        ),
    ]
