# Generated by Django 3.0.3 on 2020-09-23 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200924_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voca',
            name='date',
            field=models.CharField(max_length=50),
        ),
    ]
