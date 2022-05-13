# Generated by Django 4.0.1 on 2022-03-24 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('omni', '0002_alter_pedigreenode_pigeon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedigreenode',
            name='pigeon',
        ),
        migrations.AddField(
            model_name='pigeon',
            name='pedigreeNodes',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pigeon', to='omni.pedigreenode'),
        ),
    ]