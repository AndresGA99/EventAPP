# Generated by Django 5.1 on 2024-08-23 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventActorsApp', '0003_attender'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
