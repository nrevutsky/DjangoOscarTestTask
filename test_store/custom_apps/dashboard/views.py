from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.translation import ugettext
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView

from custom_apps.catalogue.models import Store
from custom_apps.dashboard.form import DashboardStoreSearchForm


class StoreListView(ListView):
    model = Store
    context_object_name = "store_list"
    template_name = "stores/dashboard/store_list.html"
    paginate_by = 20
    filterform_class = DashboardStoreSearchForm

    def get_title(self):
        data = getattr(self.filterform, 'cleaned_data', {})
        name = data.get('name', None)
        admin = data.get('store_admin', None)
        if name and not admin:
            return ugettext('Stores matching store "%s"') % (name,)
        elif admin and not name:
            return ugettext('Stores matching admin "%s"') % (admin,)
        else:
            return ugettext('Stores')

    def get_context_data(self, **kwargs):
        data = super(StoreListView, self).get_context_data(**kwargs)
        data['filterform'] = self.filterform
        data['queryset_description'] = self.get_title()
        return data

    def get_queryset(self):
        qs = self.model.objects.all()
        self.filterform = self.filterform_class(self.request.GET)
        if self.filterform.is_valid():
            qs = self.filterform.apply_filters(qs)
        return qs


class StoreCreateView(CreateView):
    model = Store
    template_name = 'stores/dashboard/store_create.html'
    fields = ['name']
    success_url = reverse_lazy('dashboard:store-list')

    def get_form(self):
        form = super(StoreCreateView, self).get_form()
        form.instance.store_admins = self.request.user
        form.is_valid()
        return form

    def post(self, request, *args, **kwargs):
        return super(StoreCreateView, self).post(request)

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)


class StoreUpdateView(UpdateView):
    model = Store
    fields = ['name']
    template_name = 'stores/dashboard/store_create.html'
    success_url = reverse_lazy('dashboard:store-list')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)


class StoreDeleteView(DeleteView):
    model = Store
    template_name = 'stores/dashboard/store_delete.html'
    success_url = reverse_lazy('dashboard:store-list')
