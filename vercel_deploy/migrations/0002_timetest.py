# Generated by Django 5.0.7 on 2024-08-05 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vercel_deploy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('cons', models.CharField(max_length=200)),
            ],
        ),
    ]
