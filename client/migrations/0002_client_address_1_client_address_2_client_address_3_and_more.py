# Generated by Django 4.1.7 on 2023-05-21 14:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='address_1',
            field=models.CharField(default='Niet Bekend', max_length=255),
        ),
        migrations.AddField(
            model_name='client',
            name='address_2',
            field=models.CharField(default='Niet Bekend', max_length=255),
        ),
        migrations.AddField(
            model_name='client',
            name='address_3',
            field=models.CharField(default='Niet Bekend', max_length=255),
        ),
        migrations.AddField(
            model_name='client',
            name='belasting_nummer',
            field=models.CharField(default='Niet Bekend', max_length=255),
        ),
        migrations.AddField(
            model_name='client',
            name='contact_datum_1',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='contact_datum_2',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='contact_datum_3',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='contact_persoon',
            field=models.CharField(default='Contact Persoon', max_length=255),
        ),
        migrations.AddField(
            model_name='client',
            name='contact_persoon_email',
            field=models.EmailField(default='EmailHierInvullen@snel.nl', max_length=254),
        ),
        migrations.AddField(
            model_name='client',
            name='firma_type',
            field=models.CharField(choices=[('zzp', 'Zzp'), ('bv', 'Bv'), ('vog', 'Vof'), ('stichting', 'Stichting')], default='zzp', max_length=10),
        ),
        migrations.AddField(
            model_name='client',
            name='kvk',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='client',
            name='lead_datum',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='opmerkingen',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='pakket',
            field=models.CharField(choices=[('basic', 'Basic'), ('zilver', 'Zilver'), ('goud', 'Goud')], default='basic', max_length=10),
        ),
        migrations.AddField(
            model_name='client',
            name='priority',
            field=models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], default='medium', max_length=10),
        ),
        migrations.AddField(
            model_name='client',
            name='status',
            field=models.CharField(choices=[('new', 'New'), ('contacted', 'Contacted'), ('won', 'Won'), ('lost', 'Lost')], default='new', max_length=10),
        ),
        migrations.AddField(
            model_name='client',
            name='telefoon_nummer',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='client',
            name='vak_gebied',
            field=models.CharField(default='Vak Gebied', max_length=255),
        ),
        migrations.AddField(
            model_name='client',
            name='woon_plaats',
            field=models.CharField(default='Woonplaats', max_length=255),
        ),
    ]
