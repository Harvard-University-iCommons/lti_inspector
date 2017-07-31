"""lti_inspector URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from inspector import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.tool_config, name='tool_config'),
    url(r'^launch[/]{0,1}(?P<placement>[a-z_]*)$', views.lti_launch, name='lti_launch'),
    url(r'^return_assignment_selection$', views.return_assignment_selection, name='return_assignment_selection'),
    url(r'^return_homework_submission/(?P<submission_id>[a-zA-Z0-9]+)$', views.return_homework_submission, name='return_homework_submission'),
    url(r'^view_assignment/(?P<assignment_id>[a-zA-Z0-9]+)$', views.view_assignment, name='view_assignment'),
    url(r'^view_homework_submission/(?P<submission_id>[a-zA-Z0-9]+)$', views.view_homework_submission, name='view_homework_submission'),


]
