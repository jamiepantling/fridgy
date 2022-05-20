# Generated by Django 4.0.4 on 2022-05-20 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('expiry', models.DateField()),
                ('count', models.IntegerField()),
                ('food_image', models.CharField(max_length=200)),
                ('shareable', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-expiry'],
            },
        ),
        migrations.CreateModel(
            name='Household',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]
