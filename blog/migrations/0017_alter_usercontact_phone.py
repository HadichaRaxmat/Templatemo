# Generated by Django 5.1.4 on 2024-12-05 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercontact',
            name='phone',
            field=models.IntegerField(max_length=50),
        ),
    ]