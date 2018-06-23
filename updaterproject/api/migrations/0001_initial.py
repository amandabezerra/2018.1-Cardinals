# Generated by Django 2.0.5 on 2018-06-23 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commit',
            fields=[
                ('sha', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('message', models.TextField(null=True)),
                ('paired', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ContributingWeek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.CharField(max_length=255)),
                ('line_add', models.IntegerField()),
                ('line_del', models.IntegerField()),
                ('commits', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('login', models.CharField(max_length=255)),
                ('commits', models.IntegerField(default=0, null=True)),
                ('line_code', models.IntegerField(default=0, null=True)),
                ('issues_created', models.IntegerField(default=0, null=True)),
                ('issues_closed', models.IntegerField(default=0, null=True)),
                ('score', models.DecimalField(decimal_places=2, max_digits=9, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('created_by', models.BigIntegerField()),
                ('closed_by', models.BigIntegerField(null=True)),
                ('state', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField()),
                ('closed_at', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('events_url', models.CharField(max_length=200, null=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('issues_db_updated', models.BooleanField(default=False)),
                ('commits_db_updated', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='issue',
            name='repository',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Repository'),
        ),
        migrations.AddField(
            model_name='contributor',
            name='repository',
            field=models.ManyToManyField(to='api.Repository'),
        ),
        migrations.AddField(
            model_name='contributingweek',
            name='contributor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Contributor'),
        ),
        migrations.AddField(
            model_name='commit',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Contributor'),
        ),
        migrations.AddField(
            model_name='commit',
            name='repository',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Repository'),
        ),
    ]