'''coretabs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
'''

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from hacks.views import logout_view, user_details_view, resend_confirmation_view, verify_email
from avatars.views import upload_avatar_view
from contact.views import contact_view
from discourse import views as discourse_views

import debug_toolbar


urlpatterns = [
    path('admin/', admin.site.urls),
    path('avatar/', include('avatar.urls')),

    path('api/v1/contact/', contact_view),

    path('api/v1/auth/logout/', logout_view),
    path('api/v1/auth/user/', user_details_view),
    path('api/v1/auth/user/notifications/',
         discourse_views.notifications),
    path('api/v1/auth/user/avatar/', upload_avatar_view),
    path('api/v1/auth/confirmation/', resend_confirmation_view),
    path('api/v1/auth/registration/verify-email/', verify_email),
    path('api/v1/auth/', include('rest_auth.urls')),
    path('api/v1/auth/registration/', include('rest_auth.registration.urls')),
    path('discourse/sso', discourse_views.sso),

    path('api/v1/', include('library.urls')),

    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    path('__debug__/', include(debug_toolbar.urls)),

]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
