# Generated by Django 3.0.6 on 2020-07-09 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredientes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_ingrediente', models.CharField(blank=True, max_length=70, null=True, verbose_name='Ingrediente')),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Cantidad')),
            ],
        ),
        migrations.CreateModel(
            name='Recetas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=80, verbose_name='Titulo')),
                ('ingredientes', models.ManyToManyField(blank=True, null=True, to='recetas.Ingredientes')),
            ],
        ),
    ]
