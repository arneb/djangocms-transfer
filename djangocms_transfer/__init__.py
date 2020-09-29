# -*- coding: utf-8 -*-
__version__ = '0.3.0'

default_app_config = 'djangocms_transfer.apps.TranferConfig'

def get_serializer_name(default='python'):
    from django.conf import settings
    return getattr(settings, 'DJANGO_CMS_TRANSFER_SERIALIZER', default)
