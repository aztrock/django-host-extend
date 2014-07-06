# vim: set expandtab ts=4 sw=4:
from django.conf import settings

class HostExtendMiddleware(object):
    def process_request(self, request):
        l = ['127.0.0.1', '127.0.0.2','127.0.0.3']
        settings.ALLOWED_HOSTS.extend(l)
        print (request.META['HTTP_HOST'])
        print (settings.ALLOWED_HOSTS)

