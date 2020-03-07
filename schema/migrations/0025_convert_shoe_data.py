# Generated by Django 2.2.9 on 2020-03-05 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0024_cameramodel_shoe'),
    ]

    operations = [
        migrations.RunSQL("UPDATE schema_cameramodel set shoe = 'No shoe' where hotshoe = FALSE AND coldshoe = FALSE;"),
        migrations.RunSQL("UPDATE schema_cameramodel set shoe = 'Cold shoe' where coldshoe = TRUE;"),
        migrations.RunSQL("UPDATE schema_cameramodel set shoe = 'Hot shoe' where hotshoe = TRUE;")
    ]
