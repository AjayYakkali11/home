# Generated by Django 4.2.3 on 2023-07-30 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_alter_finepage_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finepage',
            name='img',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
