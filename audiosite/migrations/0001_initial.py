# Generated by Django 3.0.3 on 2020-03-09 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sound',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wavetype', models.CharField(max_length=15, verbose_name='Wave Type')),
                ('frequency', models.IntegerField()),
            ],
        ),
    ]
