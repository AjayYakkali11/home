# Generated by Django 4.2.3 on 2023-08-07 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_finepage_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='finepage',
            name='emg',
            field=models.CharField(default='no', max_length=5),
            preserve_default=False,
        ),
    ]
