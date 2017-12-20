from django.urls import path
from snippets import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('snippets/', views.snippet_list),

    path('snippets/<int:pk>/', views.snippet_detail),
]