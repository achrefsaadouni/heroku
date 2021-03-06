# Generated by Django 2.1.7 on 2019-04-23 13:39

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MembershipInProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_allocated_by_member', models.IntegerField(verbose_name='Temps alloué par le membre')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_du_projet', models.CharField(max_length=30, verbose_name='Titre du projet')),
                ('duree_du_projet', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='Duree estimee')),
                ('temps_alloue_par_le_createur', models.IntegerField(verbose_name='Temps alloue')),
                ('besoins', models.TextField(max_length=250)),
                ('description', models.TextField(max_length=250)),
                ('est_valide', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='createur',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='project_owner', to='innovationApp.Student'),
        ),
        migrations.AddField(
            model_name='project',
            name='membres',
            field=models.ManyToManyField(blank=True, related_name='les_membres', through='innovationApp.MembershipInProject', to='innovationApp.Student'),
        ),
        migrations.AddField(
            model_name='project',
            name='superviseur',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project_coach', to='innovationApp.Coach'),
        ),
        migrations.AddField(
            model_name='membershipinproject',
            name='etudiant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='innovationApp.Student'),
        ),
        migrations.AddField(
            model_name='membershipinproject',
            name='projet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='innovationApp.Project'),
        ),
        migrations.AlterUniqueTogether(
            name='membershipinproject',
            unique_together={('projet', 'etudiant')},
        ),
    ]
