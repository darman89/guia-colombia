# Generated by Django 2.2.4 on 2019-09-02 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guiaTurismo', '0003_auto_20190824_1839'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='activities',
            field=models.TextField(blank=True, null=True),
        ),
    ]
