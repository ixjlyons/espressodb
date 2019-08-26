# Generated by Django 2.2.2 on 2019-08-26 22:46

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Current',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.TextField(editable=False)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('tag', models.CharField(blank=True, help_text='(Optional) Char(20): User defined tag for easy searches', max_length=20, null=True)),
                ('misc', django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text="(Optional) JSON: {'anything': 'you want'}", null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('current_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='current.Current')),
                ('diracstruct', models.TextField(help_text='Text: Dirac structure of the current')),
                ('momentum', models.SmallIntegerField(help_text='SmallInt: Current insertion momentum in units of 2 pi / L')),
                ('description', models.TextField(blank=True, help_text='(Optional) Text: Description of current', null=True)),
            ],
            bases=('current.current',),
        ),
        migrations.CreateModel(
            name='Local4D',
            fields=[
                ('current_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='current.Current')),
                ('diracstruct', models.TextField(help_text='Text: Dirac structure of the current')),
                ('description', models.TextField(blank=True, help_text='(Optional) Text: Description of current', null=True)),
            ],
            bases=('current.current',),
        ),
        migrations.AddConstraint(
            model_name='local4d',
            constraint=models.UniqueConstraint(fields=('diracstruct',), name='unique_current_local4d'),
        ),
        migrations.AddConstraint(
            model_name='local',
            constraint=models.UniqueConstraint(fields=('diracstruct', 'momentum'), name='unique_current_local'),
        ),
    ]
