# Generated by Django 5.1.4 on 2024-12-16 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Programmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('edad', models.PositiveSmallIntegerField()),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
