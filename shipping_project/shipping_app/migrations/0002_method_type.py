# Generated by Django 2.1.7 on 2019-03-13 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='method',
            name='type',
            field=models.CharField(choices=[('Gratuito', 'Gratuito'), ('Precio Fijo', 'Precio Fijo'), ('Recogida Local', 'Recogida Local')], default='Precio Fijo', max_length=20, verbose_name='Tipo de Envío'),
        ),
    ]
