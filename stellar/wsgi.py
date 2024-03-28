"""
WSGI config for stellar project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
# from base.models import Student


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stellar.settings')

application = get_wsgi_application()


# how to create a new student
# add_student = Student.objects.create(
#     student_name='John Wick',
#     student_class='8-green',
#     profile_pic='static/media/student_profiles/https://lionsgate.brightspotcdn.com/1d/90/8fc75de5411e985f3a2def98358d/johnwick4-section-promo-double-home-03.jpg'
# )
