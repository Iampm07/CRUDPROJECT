# Generated by Django 5.1 on 2024-09-02 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentinfo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(max_length=30),
        ),
    ]
