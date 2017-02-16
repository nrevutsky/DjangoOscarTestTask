from oscar.apps.catalogue.app import CatalogueApplication
from oscar.apps.catalogue.app import ReviewsApplication

from custom_apps.catalogue.views import CustomProductDetailView


class CustomCatalogueApplication(CatalogueApplication):
    detail_view = CustomProductDetailView


class CustomReviewsApplication(ReviewsApplication):
    pass


class CustomCatalogueApplication(CustomCatalogueApplication, CustomReviewsApplication):
    """
    Composite class combining Products with Reviews
    """


application = CustomCatalogueApplication()
