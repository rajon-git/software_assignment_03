# Generated by Django 5.0.6 on 2024-06-12 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('is_completed', models.BooleanField(default=False)),
                ('assign_date', models.DateField()),
                ('category', models.ManyToManyField(to='category.category')),
            ],
        ),
    ]
