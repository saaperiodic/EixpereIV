# Generated by Django 4.1.3 on 2022-12-20 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('M14', '0002_alter_articlemodel_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='loginModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
