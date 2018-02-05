# Generated by Django 2.0.1 on 2018-02-01 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mod', '0004_place_restaurant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='id',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='place_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mod.Place'),
            preserve_default=False,
        ),
    ]
