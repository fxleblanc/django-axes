# Generated by Django 2.1.3 on 2018-11-28 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('axes', '0006_auto_20181121_2000'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='settings',
            options={'verbose_name': 'settings', 'verbose_name_plural': 'settings'},
        ),
        migrations.AddField(
            model_name='settings',
            name='cooloff_time',
            field=models.PositiveIntegerField(default=5, verbose_name='Time between failed logins'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='settings',
            name='failure_limit',
            field=models.PositiveIntegerField(verbose_name='Maximum number of failed logins'),
        ),
    ]
