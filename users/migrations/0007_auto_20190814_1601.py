# Generated by Django 2.2.4 on 2019-08-14 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20190814_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='group',
            field=models.ManyToManyField(blank=True, null=True, related_name='groups', through='users.GroupMember', to='users.Group'),
        ),
    ]
