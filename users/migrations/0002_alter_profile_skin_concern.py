# Generated by Django 3.2.6 on 2021-08-10 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='skin_concern',
            field=models.CharField(choices=[('Dryness', 'Dryness'), ('Oily', 'Oily'), ('Acne', 'Acne'), ('Aging', 'Aging'), ('Rosacea', 'Rosacea'), ('None', 'None')], default='None', max_length=20),
        ),
    ]