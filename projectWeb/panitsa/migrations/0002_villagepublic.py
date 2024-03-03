# Generated by Django 4.2.7 on 2024-01-05 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panitsa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Villagepublic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Villagepublic_images/')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
            ],
        ),
    ]
