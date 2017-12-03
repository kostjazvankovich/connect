from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken import views as authtoken_views
from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'coins', views.CoinViewSet)
router.register(r'portfolios', views.PortfolioViewSet)
router.register(r'mock_portfolios', views.MockPortfolioViewSet)
router.register(r'mock_positions', views.MockPositionViewSet)

app_name = 'api'
urlpatterns = [
    url(r'^account/authenticate/', authtoken_views.obtain_auth_token),
    url(r'^chart/', views.chart_view),
    url(r'^', include(router.urls, namespace='api'))
]
