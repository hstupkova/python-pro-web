# Generated by Django 3.2.9 on 2021-11-08 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_person_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='event_coordinator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='coordinator', to='courses.person'),
        ),
        migrations.AddField(
            model_name='course',
            name='lecturer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lecturer', to='courses.person'),
        ),
    ]