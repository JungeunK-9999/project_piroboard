# Generated by Django 2.2.4 on 2019-08-14 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20190814_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='group_open_status',
            field=models.CharField(choices=[('n', '비공개'), ('s', '검색만가능'), ('o', '공개')], default='o', max_length=1),
        ),
    ]
