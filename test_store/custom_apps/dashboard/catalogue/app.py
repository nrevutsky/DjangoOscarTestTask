from oscar.apps.dashboard.catalogue.app import CatalogueApplication
from oscar.core.loading import get_class


class CustomCatalogueApplication(CatalogueApplication):
    product_createupdate_view = get_class('custom_apps.dashboard.catalogue.views',
                                          'CustomProductCreateUpdateView')

application = CustomCatalogueApplication()
