# Generated by Django 3.0.2 on 2022-01-12 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_alter_userdashboardmodule_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdashboardmodule',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
