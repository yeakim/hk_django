# blog app에서 사용할 url을 등록

from django.urls import path
from . import views

from . import views

urlpatterns = [
    # post detail 조회하기
    path("/<int:pk>/", views.PostDetail.as_view())

    # <ip L port>/blog : 블로그 메인 페이지
    path("/", views.PostList.as_view()),
    # <ip : port>/blog/글번호(pk)
    # /blog/1234 : 1234를 문자열로 받아들임
    path("<int:pk>/", views.single_post_page)
]