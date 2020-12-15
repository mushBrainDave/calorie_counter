# Generated by Django 3.1.2 on 2020-10-24 00:47

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('calorie', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyIntake',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calories', models.PositiveIntegerField()),
                ('protein', models.PositiveIntegerField()),
                ('fat', models.PositiveIntegerField()),
                ('carbs', models.PositiveIntegerField()),
                ('intake_date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stocks', to='calorie.customer')),
            ],
        ),
        migrations.DeleteModel(
            name='Stock',
        ),
    ]
