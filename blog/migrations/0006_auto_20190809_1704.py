# Generated by Django 2.2.4 on 2019-08-09 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190809_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='group_img',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]