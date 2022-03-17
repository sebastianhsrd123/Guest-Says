# Generated by Django 3.2.12 on 2022-03-17 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Red_Social', '0002_auto_20220316_2336'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialcomment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='Red_Social.socialcomment'),
        ),
        migrations.AddField(
            model_name='socialcomment',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Red_Social.socialpost'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='socialpost',
            name='calification',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True),
        ),
    ]
