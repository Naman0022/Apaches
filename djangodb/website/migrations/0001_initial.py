# Generated by Django 4.0.2 on 2022-02-26 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200)),
                ('passwd', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
