# vim: set expandtab ts=4 sw=4:
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django_host_extend.models import HostExtendModel

class HostExtendMiddleware(object):
    def process_request(self, request):
        host = list(HostExtendModel.objects.filter(is_active=True).values_list('host', flat=True))
        settings.ALLOWED_HOSTS.extend(set(host).difference(settings.ALLOWED_HOSTS))
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        http_host = request.META['HTTP_HOST'].split(':')
        try:
            qs = HostExtendModel.objects.get(host=http_host[0])
        except ObjectDoesNotExist:
            return None
        print (qs.image.url)
