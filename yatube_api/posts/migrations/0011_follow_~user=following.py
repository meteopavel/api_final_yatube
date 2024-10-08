# Generated by Django 3.2.16 on 2023-09-07 10:21

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_remove_follow_~user=following'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.CheckConstraint(check=models.Q(('user', django.db.models.expressions.F('following')), _negated=True), name='~user=following'),
        ),
    ]
