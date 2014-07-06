# vim: set expandtab ts=4 sw=4:
from django.db import models

class HostExtendModel(models.Model):
    host = models.URLField()
    is_active = models.BooleanField(defualt=True)
    image = models.ImageField(upload_to="/host-extend/")

    def __str__(self):
        return "%s" % self.host

    class Meta:
        db_table = 'django_host_extend'

