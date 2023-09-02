# Generated by Django 4.2.3 on 2023-08-30 22:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('billetera', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ahorro', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ahorro_deseado', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ahorros_van_bien', models.BooleanField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]