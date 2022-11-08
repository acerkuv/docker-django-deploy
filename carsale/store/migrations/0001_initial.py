# Generated by Django 4.1.3 on 2022-11-07 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sold_Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
                ('equipment', models.TextField(max_length=300)),
                ('picture', models.ImageField(upload_to='static/')),
            ],
        ),
    ]