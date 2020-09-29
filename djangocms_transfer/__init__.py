from django.conf import settings

__version__ = '1.0.0'

default_app_config = 'djangocms_transfer.apps.TranferConfig'

def get_serializer_name(default='python'):
    return getattr(settings, 'DJANGO_CMS_TRANSFER_SERIALIZER', default)
