"""innovationHub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, re_path

from innovationApp import views
from innovationApp.views import ProjectsListView,ProjectDetailView

urlpatterns = [
    path('', views.acceuil, name='index'),
    path('login/', views.login_page, name='login'),
    path('authenticate/', views.authentificate_user, name='authenticate'),
    path('logout/', views.logout_view, name='logout'),
    path('projects/', ProjectsListView.as_view(), name='list'),
    re_path(r'^projects/(?P<pk>[0-9]+)/$', ProjectDetailView.as_view(), name='detail'),
    path('projects/submit', views.submit_project, name='submitProject'),
    path('projects/submit/<int:pid>', views.update_project, name='submitUpdatedProject'),
    path('projects/add', views.add_project, name='addProject'),
    path('projects/update/<int:pid>', views.update_project, name='updateProject'),

]
