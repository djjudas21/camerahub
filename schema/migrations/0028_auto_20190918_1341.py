# Generated by Django 2.2.4 on 2019-09-18 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0027_auto_20190918_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cameramodel',
            name='shutter_type',
            field=models.CharField(blank=True, choices=[('Focal plane cloth', 'Focal plane cloth'), ('Focal plane metal', 'Focal plane metal'), ('Leaf', 'Leaf'), ('Rotary', 'Rotary'), ('Sliding', 'Sliding'), ('Electronic', 'Electronic')], help_text='Type of shutter used on this camera model', max_length=25, null=True),
        ),
        migrations.DeleteModel(
            name='ShutterType',
        ),
    ]
