# Generated by Django 3.2 on 2021-04-25 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv_show_app2', '0002_auto_20210425_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='desc',
            field=models.TextField(default=''),
        ),
    ]
