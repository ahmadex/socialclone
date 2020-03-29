from djano import render

from django.contrib.auth.mixin impoert(LoginRequiredMixinx, PermissionsMixins)
from django.views import generic

from django.models import Group,MemberGroup
from django.urls import reverse


class CreateGroup(LoginRequiredMixinx, generic.CreteView):
    fields = ('name','description')
    model = Group

class SingleGroup(generic.DetailView):
    model = Group

class ListGroups(generic.ListView):
    model = Group
