# Generated by Django 5.1.4 on 2024-12-05 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_meeting'),
    ]

    operations = [
        migrations.CreateModel(
            name='Middle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('last', models.CharField(max_length=100)),
            ],
        ),
    ]
