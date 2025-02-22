# Generated by Django 3.2.23 on 2023-11-06 23:08

from django.db import migrations, models


from core_app.utils import DjangoMigrationLogger


class Migration(DjangoMigrationLogger, migrations.Migration):

    dependencies = [
        ('reversion', '0002_add_index_on_version_for_content_type_and_db'),
    ]
    operations = [
        migrations.AlterField(
            model_name='revision',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='version',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
