# Generated by Django 5.1 on 2024-08-20 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventActorsApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizator',
            name='telephone',
            field=models.CharField(max_length=15),
        ),
    ]
