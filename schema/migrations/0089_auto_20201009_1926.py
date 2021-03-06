# Generated by Django 2.2.16 on 2020-10-09 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0088_auto_20201012_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='cameramodel',
            name='image_attribution',
            field=models.CharField(blank=True, help_text='Author of this image', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='cameramodel',
            name='image_attribution_url',
            field=models.URLField(blank=True, help_text='Attribution URL for this image', null=True),
        ),
        migrations.AddField(
            model_name='historicalcameramodel',
            name='image_attribution',
            field=models.CharField(blank=True, help_text='Author of this image', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='historicalcameramodel',
            name='image_attribution_url',
            field=models.URLField(blank=True, help_text='Attribution URL for this image', null=True),
        ),
        migrations.AddField(
            model_name='historicallensmodel',
            name='diagram_attribution',
            field=models.CharField(blank=True, help_text='Author of this diagram', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='historicallensmodel',
            name='diagram_attribution_url',
            field=models.URLField(blank=True, help_text='Attribution URL for this diagram', null=True),
        ),
        migrations.AddField(
            model_name='historicallensmodel',
            name='image_attribution',
            field=models.CharField(blank=True, help_text='Author of this image', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='historicallensmodel',
            name='image_attribution_url',
            field=models.URLField(blank=True, help_text='Attribution URL for this image', null=True),
        ),
        migrations.AddField(
            model_name='lensmodel',
            name='diagram_attribution',
            field=models.CharField(blank=True, help_text='Author of this diagram', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='lensmodel',
            name='diagram_attribution_url',
            field=models.URLField(blank=True, help_text='Attribution URL for this diagram', null=True),
        ),
        migrations.AddField(
            model_name='lensmodel',
            name='image_attribution',
            field=models.CharField(blank=True, help_text='Author of this image', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='lensmodel',
            name='image_attribution_url',
            field=models.URLField(blank=True, help_text='Attribution URL for this image', null=True),
        ),
    ]
