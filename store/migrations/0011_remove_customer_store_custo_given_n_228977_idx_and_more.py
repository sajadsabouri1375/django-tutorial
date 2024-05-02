# Generated by Django 5.0.4 on 2024-05-02 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_rename_store_cusom_given_n_8dfeb9_idx_store_custo_given_n_228977_idx_and_more'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='customer',
            name='store_custo_given_n_228977_idx',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='given_name',
            new_name='first_name',
        ),
        migrations.AddIndex(
            model_name='customer',
            index=models.Index(fields=['first_name', 'last_name'], name='store_custo_first_n_8f83e0_idx'),
        ),
    ]
