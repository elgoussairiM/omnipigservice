# Generated by Django 4.0.1 on 2022-03-24 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('omni', '0004_alter_pigeon_pedigreenodes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pigeon',
            name='pedigreeNodes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pigeons', to='omni.pedigreenode'),
        ),
    ]
