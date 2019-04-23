from django.forms import ModelForm
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['nom_du_projet', 'duree_du_projet', 'temps_alloue_par_le_createur','createur' ,'besoins','description']
