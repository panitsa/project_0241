# Generated by Django 4.2.10 on 2024-02-27 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panitsa', '0006_alter_activity_news_image1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Useregister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('phoneNumber', models.CharField(max_length=15)),
            ],
        ),
    ]