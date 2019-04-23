from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator,EmailValidator
from django.db.models import Sum

def email_esprit_validator(value):
    if str(value).endswith("@esprit.tn") == False:
        raise ValidationError('votre email doit etre esprit.tn', params={'value': value})

"""class User(models.Model):
    nom = models.CharField('Prenom', max_length=30)
    prenom = models.CharField('Nom',max_length=30)
    email = models.EmailField('Email', validators=[email_esprit_validator])

    def __str__(self):
        return self.nom"""

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE )

class Coach(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE )


class Project(models.Model):
    nom_du_projet = models.CharField('Titre du projet', max_length=30)
    duree_du_projet = models.IntegerField('Duree estimee', default=0 , validators=[MinValueValidator(1),MaxValueValidator(10)])
    temps_alloue_par_le_createur = models.IntegerField('Temps alloue')
    besoins = models.TextField(max_length=250)
    description = models.TextField(max_length=250)

    # Validation State of the project
    est_valide = models.BooleanField(default=False)

    createur = models.OneToOneField(
        Student,
        on_delete=models.CASCADE,
        related_name='project_owner'
    )

    superviseur = models.ForeignKey(
        Coach,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='project_coach'
    )

    membres = models.ManyToManyField(
        Student,
        through='MembershipInProject',
        # added to differ with the lead relation
        related_name='les_membres',
        blank=True,
    )

    def __str__(self):
        return self.nom_du_projet

    def Total_Time_Invest(self):
        return MembershipInProject.objects.filter(projet=self.id).aggregate(Sum('time_allocated_by_member'))['time_allocated_by_member__sum'] or 0


class MembershipInProject(models.Model):
    projet = models.ForeignKey(Project, on_delete=models.CASCADE)
    etudiant = models.ForeignKey(Student, on_delete=models.CASCADE)
    time_allocated_by_member = models.IntegerField('Temps alloué par le membre')

    def __str__(self):
        return 'Membre ' + self.etudiant.nom

    class Meta:
        unique_together = ("projet", "etudiant")

