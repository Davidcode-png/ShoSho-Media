# Generated by Django 4.0.6 on 2022-08-03 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shosho', '0014_alter_comment_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='threadmodel',
            old_name='receriver',
            new_name='receiver',
        ),
    ]