# Generated by Django 2.0.4 on 2018-05-04 03:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0003_auto_20180502_1539'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='party',
            name='creator',
        ),
        migrations.AlterField(
            model_name='user',
            name='party',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='party', to='election.Party'),
        ),
        migrations.AlterField(
            model_name='user',
            name='position',
            field=models.SmallIntegerField(choices=[(0, 'N/A'), (1, 'President'), (2, 'Vice-President'), (3, 'Secretary'), (4, 'Assistant-Secretary'), (5, 'Treasurer'), (6, 'Assistant-Treasurer'), (7, 'PRO')], default=0),
        ),
        migrations.AddField(
            model_name='vote',
            name='candidate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='candidate', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='vote',
            name='party',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='election.Party'),
        ),
        migrations.AddField(
            model_name='vote',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]