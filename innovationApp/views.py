from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.views.generic import DetailView

from innovationApp.forms import ProjectForm
from .models import *;
# Create your views here.
def acceuil(request):
    return render(request, 'index.html')
def login_page(request):
    return render(request, 'login.html')
"""def projects(request):
    projects_list = Project.objects.all()
    context = {'projects_list': projects_list}
    return render(request, 'projects.html', context)



def projectDetail(request, pid):
    project = get_object_or_404(Project, pk=pid)
    return render(request, 'project_details.html',{'project': project})"""

class ProjectsListView(generic.ListView):
    template_name = 'projects.html'
    context_object_name = 'projects_list'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                return Project.objects.all()
            else:
                return Project.objects.filter(est_valide=True)
        else:
            return None


class ProjectDetailView(DetailView):
    model = Project
    context_object_name = 'project'
    template_name = 'project_details.html'



def add_project(request):
        form = ProjectForm()
        return render(request, 'add_project.html', {'form': form})





def submit_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            postProject = form.save(commit=False)
            postProject.save()
            return HttpResponseRedirect(reverse('list'))
        else:
            print('form non valide')
            return render(request, 'add_project.html', {'msg_erreur': 'form non valide'})
    else:
        print('Erreur lors de la création de l’article')
        return render(request, 'add_project.html',{'msg_erreur': 'Erreur lors de la création de l’article'})

def update_project(request,pid):
    project = get_object_or_404(Project, pk=pid)
    if request.method == "GET":
        form = ProjectForm(instance=project)
        return render(request, 'update_project.html', {'form': form , 'pid': pid})
    if request.method == "POST":
        form = ProjectForm(request.POST or None, instance=project)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('list'))
        else:
            print('form non valide')
            return render(request, 'update_project.html', {'msg_erreur': 'form non valide'})
    else:
        print('Erreur lors de la création de projet')
        return render(request, 'update_project.html',{'msg_erreur': 'Erreur lors de update de projet'})

def authentificate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return HttpResponseForbidden()
    else:
        return HttpResponseForbidden()


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
