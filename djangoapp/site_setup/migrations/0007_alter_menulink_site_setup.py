# Generated by Django 4.2.7 on 2023-11-16 02:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_setup', '0006_alter_menulink_site_setup_alter_sitesetup_favicon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menulink',
            name='site_setup',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='menu', to='site_setup.sitesetup'),
        ),
    ]
