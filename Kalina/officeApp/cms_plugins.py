# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import OfficeItem, OfficeLink, OfficeFloorLink
from .forms import ItemsForm


class OfficePlugin(CMSPluginBase):
    model = OfficeItem
    name = _('Office')
    render_template = 'office.html'
    child_classes = ['']

    fieldsets = [
        (None, {
            'fields': (
                ('number', 'price',),
                ('floor', 'metres',),
                ('is_free', 'published',),
            )
        })
    ]

    # def get_render_template(self, context, instance, placeholder):
    #     return 'office/{}/map.html'.format(instance.template)

    def render(self, context, instance, placeholder):
        context['instance'] = instance
#         request = context['request']
#         context.update({
#             'instance': instance,
#             'placeholder': placeholder,
#             'form': ItemsForm(request=request),
#         })
        return context

plugin_pool.register_plugin(OfficePlugin)


class OfficeLinksPlugin(CMSPluginBase):
    model = OfficeLink
    name = _('OfficeLink')
    render_template = 'officelinks.html'
    child_classes = ['']

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(OfficeLinksPlugin)


class OfficeFloorPlugin(CMSPluginBase):
    model = OfficeFloorLink
    name = _('OfficeFloorLink')
    render_template = 'svg_base.html'
    child_classes = ['']

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(OfficeFloorPlugin)