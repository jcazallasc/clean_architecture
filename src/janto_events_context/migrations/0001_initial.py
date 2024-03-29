# Generated by Django 3.2.15 on 2022-09-27 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JantoEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_event_id', models.IntegerField()),
                ('event_id', models.IntegerField()),
                ('title', models.CharField(max_length=500)),
                ('sell_mode', models.CharField(max_length=20)),
                ('event_start_date', models.DateTimeField()),
                ('event_end_date', models.DateTimeField(null=True)),
                ('sell_from', models.DateTimeField()),
                ('sell_to', models.DateTimeField()),
                ('sold_out', models.BooleanField()),
                ('zones', models.JSONField(default=dict)),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddIndex(
            model_name='jantoevent',
            index=models.Index(fields=['event_id'], name='janto_event_event_i_1b326b_idx'),
        ),
        migrations.AddIndex(
            model_name='jantoevent',
            index=models.Index(fields=['base_event_id'], name='janto_event_base_ev_eefa47_idx'),
        ),
    ]
