from django import forms
from django.forms.models import inlineformset_factory
from django.utils.translation import ugettext_lazy as _
from custom_apps.catalogue.models import StoreProduct
from custom_apps.catalogue.models import Product


class ProductStoreForm(forms.ModelForm):

    class Meta:
        model = StoreProduct
        fields = ('store',)


BaseStoreProductFormSet = inlineformset_factory(Product,
                                                StoreProduct,
                                                form=ProductStoreForm,
                                                extra=1,
                                                fk_name='product')


class ProductStoreFormSet(BaseStoreProductFormSet):
    def __init__(self, product_class, user, *args, **kwargs):
        super(ProductStoreFormSet, self).__init__(*args, **kwargs)

    def clean(self):
        if not self.instance.is_child and self.get_num_stores() == 0:
            raise forms.ValidationError(
                _("Stand-alone and parent products "
                  "must have at least one store"))
        if self.instance.is_child and self.get_num_stores() > 0:
            raise forms.ValidationError(
                _("A child product should not have stores"))

    def get_num_stores(self):
        num_stores = 0
        for i in range(0, self.total_form_count()):
            form = self.forms[i]
            if (hasattr(form, 'cleaned_data')
                and form.cleaned_data.get('store', None)
                and not form.cleaned_data.get('DELETE', False)):
                num_stores += 1
        return num_stores
