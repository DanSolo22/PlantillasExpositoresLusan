# Generated by Django 4.0.5 on 2022-06-04 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expositor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alto', models.IntegerField(default=0)),
                ('ancho', models.IntegerField(default=0)),
                ('ganchosF', models.IntegerField(default=0)),
                ('ganchosC', models.IntegerField(default=0)),
                ('imagen_expositor', models.ImageField(default='False', upload_to='imagenes_expositor')),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Blister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referencia', models.CharField(max_length=50)),
                ('largo', models.IntegerField(default=0)),
                ('ancho', models.IntegerField(default=0)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='generador.material')),
            ],
        ),
    ]
