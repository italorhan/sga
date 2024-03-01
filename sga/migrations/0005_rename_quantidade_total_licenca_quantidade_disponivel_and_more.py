# Generated by Django 5.0.2 on 2024-03-01 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sga', '0004_licenca_quantidade_total'),
    ]

    operations = [
        migrations.RenameField(
            model_name='licenca',
            old_name='quantidade_total',
            new_name='quantidade_disponivel',
        ),
        migrations.AddField(
            model_name='licenca',
            name='quantidade_utilizada',
            field=models.IntegerField(null=True),
        ),
    ]
