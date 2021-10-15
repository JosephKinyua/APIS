from django.urls import path
from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # APIViews
    path('<int:pk>/', PostDetail.as_view()),
    path('post/v1', PostList.as_view()),

    path('<int:pk>/', CustomerDetail.as_view()),
    path('customer/v1', CustomerList.as_view()),

    path('<int:pk>/', StaffDetail.as_view()),
    path('staff/v1', StaffList.as_view()),

    path('<int:pk>/', OrderDetail.as_view()),
    path('order/v1', OrderList.as_view()),

    path('<int:pk>/', FoodDetail.as_view()),
    path('food/v1', FoodList.as_view()),

    path('<int:pk>/', CartDetail.as_view()),
    path('cart/v1', CartList.as_view()),

    path('<int:pk>/', CommentDetail.as_view()),
    path('comment/v1', CommentList.as_view()),

    path('<int:pk>/', DataDetail.as_view()),
    path('data/v1', DataList.as_view()),

    path('<int:pk>/', DeliveryBoyDetail.as_view()),
    path('deliveryboy/v1', DeliveryBoyList.as_view()),

    path('<int:pk>/', OrderContentDetail.as_view()),
    path('ordercontent/v1', OrderContentList.as_view()),

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

