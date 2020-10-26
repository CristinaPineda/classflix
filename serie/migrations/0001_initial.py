# Generated by Django 3.1 on 2020-08-13 21:46
import django.db.models.deletion
from django.db import migrations, models



class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('genero', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('idGenero', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='genero.Genero')),
            ],
        ),
    ]