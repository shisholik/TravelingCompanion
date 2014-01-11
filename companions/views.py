from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.views.generic import CreateView, UpdateView
from companions.models import Route


class IndexView(generic.ListView):
    template_name = 'companions/index.html'
    context_object_name = 'latest_route_list'

    def get_queryset(self):
        """Return the last five published polls."""
        return Route.objects.order_by('-departureDate')[:5]


@login_required
def imGoing(request,route_id):
    p = get_object_or_404(Route, pk=route_id)

    if p.users.count() < p.maxCompanions:
        p.users.add(request.user)
        p.save()
    return redirect(reverse('detail', args=(route_id,)))

@login_required
def imNotGoing(request,route_id):
    p = get_object_or_404(Route, pk=route_id)
    if request.user in p.users.all():
        p.users.remove(request.user)
        p.save()
    return redirect(reverse('detail', args=(route_id,)))



class DetailView(generic.DetailView):
    model = Route
    template_name = 'companions/detail.html'

class EditView(UpdateView):
    model = Route
    fields = ['cityA','cityB','departureDate','maxCompanions','description']
    def get_success_url(self):
        return reverse('detail', args=(self.get_object().id,))
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.creator == request.user:
            return super(UpdateView, self).get(request, *args, **kwargs)
        else:
            return redirect(reverse('detail',args=(self.object.id,)))

    #template_name = 'companions/detail.html'


class CreateView(CreateView):
    model = Route
    success_url = '/'
    fields = ['cityA','cityB','departureDate','maxCompanions','description']
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.creator = self.request.user
        instance.save()
        return redirect(reverse('detail',args=(instance.id,)))
    #template_name = 'companions/detail.html'
