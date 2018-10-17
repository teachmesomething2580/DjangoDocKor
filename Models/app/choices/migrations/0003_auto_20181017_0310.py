# Generated by Django 2.1.2 on 2018-10-17 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('choices', '0002_student_media_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='year_in_school',
            field=models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior')], db_column='class-', default='FR', max_length=2),
        ),
    ]
