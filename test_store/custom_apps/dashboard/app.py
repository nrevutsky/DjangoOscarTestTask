from django.conf.urls import url
from oscar.apps.dashboard.app import DashboardApplication
from oscar.views.decorators import staff_member_required

from custom_apps.dashboard import views
from custom_apps.dashboard.catalogue.app import application as dashboard_catalogue_app


class StoresDashboardApplication(DashboardApplication):
    store_list_view = views.StoreListView
    store_create_view = views.StoreCreateView
    store_update_view = views.StoreUpdateView
    store_delete_view = views.StoreDeleteView
    catalogue_app = dashboard_catalogue_app

    def get_urls(self):
        urlpatterns = super(StoresDashboardApplication, self).get_urls()
        urlpatterns += [
            url(r'^stores/$', self.store_list_view.as_view(), name='store-list'),
            url(r'^create-store/$', self.store_create_view.as_view(), name='store-create'),
            url(r'^update-store/(?P<pk>[\d]+)/$', self.store_update_view.as_view(), name='store-update'),
            url(r'^delete-store/(?P<pk>[\d]+)/$', self.store_delete_view.as_view(), name='store-delete')
        ]
        return self.post_process_urls(urlpatterns)

    def get_url_decorator(self, url_name):
        return staff_member_required


application = StoresDashboardApplication()
