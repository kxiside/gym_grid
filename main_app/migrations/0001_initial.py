# Generated by Django 4.2.5 on 2023-09-19 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category', models.CharField(choices=[(1, 'Abs'), (2, 'Arms'), (3, 'Back'), (4, 'Calves'), (5, 'Cardio'), (6, 'Chest'), (7, 'Legs'), (8, 'Shoulders')], default=1, max_length=20)),
                ('equipment', models.CharField(max_length=20)),
                ('weights', models.IntegerField()),
                ('reps', models.IntegerField()),
                ('sets', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField(verbose_name='workout date')),
                ('duration', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=200)),
                ('exercises', models.ManyToManyField(related_name='workouts', to='main_app.exercise')),
            ],
        ),
    ]
