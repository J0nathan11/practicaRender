# Generated by Django 4.0.6 on 2024-07-09 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cartelera', '0010_remove_director_fotografia_director_foto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cine',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=50)),
            ],
        ),
    ]
