# Generated by Django 3.0.6 on 2020-07-14 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(blank=True, max_length=70, null=True, verbose_name='Producto')),
                ('calorias', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Calorias')),
                ('grasas', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Grasas')),
            ],
        ),
        migrations.AlterModelOptions(
            name='ingredientes',
            options={'verbose_name': 'Ingrediente', 'verbose_name_plural': 'Ingredientes'},
        ),
        migrations.AlterModelOptions(
            name='recetas',
            options={'verbose_name': 'Receta', 'verbose_name_plural': 'Recetas'},
        ),
        migrations.AlterField(
            model_name='ingredientes',
            name='nombre_ingrediente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recetas.Productos'),
        ),
    ]
