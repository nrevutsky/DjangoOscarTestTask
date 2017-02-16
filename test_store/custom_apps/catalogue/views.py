from oscar.apps.catalogue.views import ProductDetailView
from custom_apps.catalogue.models import Store
from custom_apps.catalogue.models import StoreProduct


class CustomProductDetailView(ProductDetailView):

    def get_context_data(self, **kwargs):
        ctx = super(ProductDetailView, self).get_context_data(**kwargs)
        ctx['alert_form'] = self.get_alert_form()
        ctx['has_active_alert'] = self.get_alert_status()
        ctx['store'] = Store.objects.get(product=self.object, store_admins=self.request.user)
        return ctx
