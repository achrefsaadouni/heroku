from django.contrib import admin
from .models import *
# Register your models here.
from .models import Student
from .models import Coach
from .models import Project
"""class StudentAdmin(admin.ModelAdmin):
    list_display = ('last_name','first_name', 'email',)
    ordering = ['first_name']
    fields = (('last_name','first_name'), 'email',)
class MembershipInline(admin.StackedInline):
    model = MembershipInProject
    extra = 0

class ProjectAdmin(admin.ModelAdmin):
    actions = ['set_to_valid']
    inlines = (MembershipInline,)
    list_display = ('nom_du_projet', 'duree_du_projet', 'temps_alloue_par_le_createur','description','Total_Time_Invest')
    fieldsets = (
        ('Etat', {'fields': ('est_valide',)}),
        ('A propos', {
            'fields': ('nom_du_projet', ('createur', 'superviseur'), 'besoins', 'description',),
        }),
        ('Durées', {
            'fields': (('duree_du_projet', 'temps_alloue_par_le_createur'),)
        })
    )

    list_filter = ('createur',)
    search_fields = ['nom_du_projet', 'createur__nom']


    def set_to_valid(self, request, queryset):
        queryset.update(est_valide=True)
    set_to_valid.short_description = "Valider"""""

admin.site.register(Coach)
admin.site.register(Project)
admin.site.register(Student)