# vim: set expandtab ts=4 sw=4:
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.http import HttpResponseRedirect
from django_host_extend.models import HostExtendModel

class HostExtendMiddleware(object):

    def process_request(self, request):
        host = cache.get("host_list")
        if not host:
            host = list(
                HostExtendModel.objects.filter(is_active=True).values_list('host', flat=True)
            )
            cache.set("host_list", host)
            settings.ALLOWED_HOSTS = ["127.0.0.1"]
        #settings.ALLOWED_HOSTS.extend(set(host).difference(settings.ALLOWED_HOSTS))
        if request.META['HTTP_HOST'].split(':')[0] not in host:
            return HttpResponseRedirect(settings.HE_REDIRECT)
        settings.ALLOWED_HOSTS.extend(host)

    def process_view(self, request, view_func, view_args, view_kwargs):
        http_host = request.META['HTTP_HOST'].split(':')
        host = cache.get("HostExtend:" + http_host[0])
        if not host:
            try:
                HostExtendModel.objects.get(host=http_host[0], is_active=True)
                cache.set("HostExtend:" + http_host[0], True)
            except ObjectDoesNotExist:
                return HttpResponseRedirect(settings.HE_REDIRECT)
