from django.conf.urls import url
from . import views

urlpatterns = [
				url(r'', views.index, name='index_login'),
				# url(r'^login/$' , views.returnlogin , name = 'login')
			
				]