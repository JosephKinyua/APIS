from django.urls import path
from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # APIViews
    path('<int:pk>/', PostDetail.as_view()),
    path('post', PostList.as_view()),

    path('<int:pk>/', CustomerDetail.as_view()),
    path('customer', CustomerList.as_view()),

    path('<int:pk>/', StaffDetail.as_view()),
    path('staff', StaffList.as_view()),

    path('<int:pk>/', OrderDetail.as_view()),
    path('order', OrderList.as_view()),

    path('<int:pk>/', FoodDetail.as_view()),
    path('food', FoodList.as_view()),

    path('<int:pk>/', CartDetail.as_view()),
    path('cart', CartList.as_view()),

    path('<int:pk>/', CommentDetail.as_view()),
    path('comment', CommentList.as_view()),

    path('<int:pk>/', DataDetail.as_view()),
    path('data', DataList.as_view()),


    path('<int:pk>/', OrderContentDetail.as_view()),
    path('ordercontent', OrderContentList.as_view()),

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

