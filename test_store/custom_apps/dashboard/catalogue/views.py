from oscar.apps.dashboard.catalogue.views import ProductCreateUpdateView
from custom_apps.dashboard.catalogue.form import ProductStoreFormSet


class CustomProductCreateUpdateView(ProductCreateUpdateView):
    template_name = 'dashboard/catalogue/product_update.html'
    store_formset = ProductStoreFormSet

    def __init__(self, *args, **kwargs):
        super(CustomProductCreateUpdateView, self).__init__(*args, **kwargs)
        self.formsets = {'store_formset': self.store_formset,
                         'category_formset': self.category_formset,
                         'image_formset': self.image_formset,
                         'recommended_formset': self.recommendations_formset,
                         'stockrecord_formset': self.stockrecord_formset}
