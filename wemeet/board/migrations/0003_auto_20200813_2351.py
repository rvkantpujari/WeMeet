# Generated by Django 3.0.8 on 2020-08-13 18:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('globaltables', '0003_auto_20200813_2305'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('board', '0002_auto_20200813_2248'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choices',
            fields=[
                ('choiceId', models.AutoField(primary_key=True, serialize=False)),
                ('choice', models.CharField(max_length=200)),
                ('count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('pollId', models.AutoField(primary_key=True, serialize=False)),
                ('pollQuestion', models.CharField(max_length=200)),
                ('createdOn', models.DateTimeField()),
                ('deadLine', models.DateTimeField()),
                ('isActive', models.BooleanField(default=1)),
                ('boardId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.Board')),
                ('createdBy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MemberPollChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choiceId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.Choices')),
                ('pollId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.Poll')),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='choices',
            name='pollId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.Poll'),
        ),
        migrations.CreateModel(
            name='BoardInvitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=20)),
                ('invitationTime', models.DateTimeField()),
                ('responseTime', models.DateTimeField(null=True)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.Board')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globaltables.Role')),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
