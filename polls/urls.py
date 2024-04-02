from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_swagger.views import get_swagger_view
from .apiviews import (
    PollDetail,
    PollList,
    ChoiceList,
    CreateVote,
    LoginView,
    UserCreate,
    PollViewSet
    )

schema_view = get_swagger_view(title='polls API')
router = DefaultRouter()
router.register('polls', PollViewSet, basename='polls')

urlpatterns =[
    path("login/", views.obtain_auth_token, name="login"),
    path("login/", LoginView.as_view(), name="login"),
    path("polls/", PollList.as_view(), name="polls_list"),
    path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
    path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),
    path("users/", UserCreate.as_view(), name="user_create"),
    path(r'swagger-docs/', schema_view),
]