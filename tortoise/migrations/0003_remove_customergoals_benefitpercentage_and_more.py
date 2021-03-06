# Generated by Django 4.0.5 on 2022-07-17 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tortoise', '0002_alter_promotions_planid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customergoals',
            name='benefitPercentage',
        ),
        migrations.RemoveField(
            model_name='customergoals',
            name='benifitType',
        ),
        migrations.RemoveField(
            model_name='customergoals',
            name='id',
        ),
        migrations.AddField(
            model_name='customergoals',
            name='goalId',
            field=models.AutoField(default=1, primary_key=True, serialize=False, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customergoals',
            name='planId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tortoise.plans'),
        ),
        migrations.AlterField(
            model_name='customergoals',
            name='startDate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
