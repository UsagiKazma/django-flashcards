from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from apps.cards.views import CreateCard, DetailsView

urlpatterns = {
    url(r'^cards/$', CreateCard.as_view(), name="card"),
    url(r'^cards/(?P<pk>\d+)/$',
        DetailsView.as_view(), name="card-id"),
}

urlpatterns = format_suffix_patterns(urlpatterns)