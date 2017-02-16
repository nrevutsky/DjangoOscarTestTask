from django import forms
from django.utils.translation import ugettext_lazy as _


class DashboardStoreSearchForm(forms.Form):
    name = forms.CharField(label=_('Store name'), required=False)
    admin = forms.CharField(label=_('Admin name'), required=False)

    def is_empty(self):
        d = getattr(self, 'cleaned_data', {})
        empty = lambda key: not d.get(key, None)
        return empty('name')

    def apply_name_filter(self, qs, value):
        return qs.filter(name__icontains=value)

    def apply_filters(self, qs):
        for key, value in self.cleaned_data.items():
            if value:
                qs = getattr(self, 'apply_%s_filter' % key)(qs, value)
        return qs
