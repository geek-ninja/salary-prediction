# Generated by Django 3.1.2 on 2021-04-14 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SalaryRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience', models.FloatField()),
                ('salary', models.FloatField()),
            ],
        ),
    ]
