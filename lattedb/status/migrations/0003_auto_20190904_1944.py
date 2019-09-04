# Generated by Django 2.2.2 on 2019-09-04 19:44

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('correlator', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('status', '0002_auto_20190904_1822'),
    ]

    operations = [
        migrations.CreateModel(
            name='Baryon2pt',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.TextField(editable=False)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('tag', models.CharField(blank=True, help_text='(Optional) Char(20): User defined tag for easy searches', max_length=20, null=True)),
                ('misc', django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text="(Optional) JSON: {'anything': 'you want'}", null=True)),
                ('home', models.TextField(blank=True, help_text='(Optional) Text: Computing facility where the object resides at', null=True)),
                ('directory', models.TextField(blank=True, help_text='(Optional) Text: Directory path to result', null=True)),
                ('hdf5path', models.TextField(blank=True, help_text='(Optional) Text: Folder path in hdf5 file', null=True)),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Unknown'), (1, 'Does not exist'), (2, 'Exists'), (3, 'On tape')], help_text='PositiveSmallInt: Encode categorical status labels')),
                ('timestamp', models.DateTimeField(auto_now_add=True, help_text='DateTime:Last time the field was updated.')),
                ('source_group', models.PositiveSmallIntegerField(help_text='PositiveSmallInt: Index to the source group', null=True)),
                ('barryon2pt', models.ForeignKey(help_text='ForeignKey: Baryon two point correlation function', on_delete=django.db.models.deletion.CASCADE, to='correlator.Baryon2pt')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='baryon2pt',
            constraint=models.UniqueConstraint(fields=('barryon2pt', 'home'), name='unique_baryon2pt_file_status'),
        ),
    ]