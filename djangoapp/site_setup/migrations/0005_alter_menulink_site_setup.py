# Generated by Django 4.2.7 on 2023-11-13 18:45

from django.db import migrations, models
import django.db.models.deletion
import utils.model_validators


class Migration(migrations.Migration):

    dependencies = [
        ('site_setup', '0004_sitesetup_favicon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menulink',
            name='site_setup',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='site_setup.sitesetup', validators=[utils.model_validators.validate_png]),
        ),
    ]