from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

class Plugin(models.Model):
    name = models.CharField(_("Name"), max_length=80)
    author = models.CharField(_("Author"), max_length=80)
    description = models.TextField(_("description"), blank=True, null=True)
    category = models.CharField(_("Category"),max_length=80)
    installed = models.BooleanField(default=False, blank=True, null=True)
    installable = models.BooleanField(default=False, blank=True, null=True)
    color = models.CharField(_("Color"), blank=True, null=True, max_length=20)
    icon = models.CharField(_("Icon"), blank=True, null=True, max_length=20)
    version = models.CharField(_("Version"), blank=True, null=True, max_length=20)


    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ['pk']
        verbose_name = _("Plugin")
        verbose_name_plural = _("Plugin")