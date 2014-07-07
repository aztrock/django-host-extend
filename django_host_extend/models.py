# vim: set expandtab ts=4 sw=4:
from django.db import models

class HostExtendModel(models.Model):
    host = models.CharField(max_length=200, help_text='https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts')
    is_active = models.BooleanField(default=True, blank=True)
    image = models.ImageField(upload_to="host-extend/", blank=True, null=True)

    def __str__(self):
        return "%s" % self.host

    class Meta:
        db_table = 'django_host_extend'

