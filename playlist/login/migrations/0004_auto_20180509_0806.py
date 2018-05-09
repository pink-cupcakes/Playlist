# Generated by Django 2.0.5 on 2018-05-09 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20180509_0743'),
    ]

    operations = [
        migrations.RenameField(
            model_name='playlist',
            old_name='userid',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
