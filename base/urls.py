from django.urls import path
from . import views, api_view
import os
from django.conf import settings
from django.http import HttpResponse

def mediaDownloader(request, file_path):
    full_path = os.path.join(settings.MEDIA_ROOT, file_path)
    print(file_path, full_path)

    if not os.path.exists(full_path):
        raise Http404
    print(full_path)
    with open(full_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename="{os.path.basename(full_path)}"'
    return response


urlpatterns = [
    path('', views.home, name='home'),
    path('icons/', views.icons, name='icons'),
    path('button/', views.buttons, name='button'),
    path('typography/', views.typography, name='typography'),
    path('form_element/', views.form_element, name='formElement'),
    path('tables/', views.tables, name='tables'),
    path('charts/', views.charts, name='charts'),
    path('apex_charts/', views.apex_charts, name='apex_charts'),
    path('create_shop/', views.create_shop, name='create_shop'),
    path('create_warehouse/', views.create_warehouse, name='create_warehouse'),
    path('create_product/', views.create_product, name='create_product'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('warehouse/<int:warehouse_id>/delete/', views.delete_warehouse, name='delete_warehouse'),
    path('shop/<int:shop_id>/delete/', views.delete_shop, name='delete_shop'),
    path('product/<int:product_id>/delete/', views.delete_product, name='delete_product'),
    path('error-404/', views.error404, name='error404'),
    path('error-500/', views.error500, name='error500'),

    # for student
    path('add_student/', views.add_student, name='add_student'),
    path('student/delete/', views.delete_student, name='delete_student'),
    path('student/<int:student_id>/update/', views.update_student, name='update_student'),

    # apiurls
    path('students/', api_view.get_students, name='get_students'),
    # Media file urls
    path('media/<path:file_path>/', mediaDownloader, name='mediaDownloader'),

]
