from django.contrib import admin
from django.utils.html import format_html
from django.urls import path
from django.views.generic.detail import DetailView
from rest_framework.reverse import reverse
from applications.recognition.utils.model_to_dict import model_to_dict
from applications.core.models import BaseModel


class RelatedObjectLinkMixin(object):
    """
    Generate links to related links. Add this mixin to a Django admin model. Add a 'change_links' attribute to the admin
    containing a list of related model fields and then add the attribute name with a '_link' suffix to the list_display
    attribute. For Example a KingKong model with a 'original_field_name' attribute would have an Admin class like this:

    class KingKongAdmin(RelatedObjectLinkMixin, ...):
        change_links = ('original_field_name', )

        list_display = (
            ...
            'original_field_name_link',
            ...
        )
    """

    link_fields = []
    change_links = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.change_links:
            for field_name in self.change_links:
                func_name = field_name + '_link'
                setattr(self, func_name, self._generate_link_func(field_name))

    def _generate_link_func(self, field_name):
        def _func(obj, *args, **kwargs):
            related_obj = getattr(obj, field_name)
            if related_obj:
                url_name = 'admin:%s_%s_change' % (self.opts.app_label, related_obj._meta.model_name)
                url = reverse(url_name, args=[related_obj.pk])

                return format_html('<a href="{}" class="changelink">{}</a>', url, str(related_obj))
            else:
                return None

        _func.short_description = field_name

        return _func


class BooleanExistFilter(admin.FieldListFilter):
    def __init__(self, field, request, params, model, model_admin, field_path):
        self.lookup_kwarg = '%s__isnull' % field_path
        self.lookup_val = request.GET.get(self.lookup_kwarg)
        super().__init__(field, request, params, model, model_admin, field_path)
        self.title = 'Exist %s' % getattr(field, 'verbose_name', field_path)

        if (self.used_parameters and self.lookup_kwarg in self.used_parameters and
                self.used_parameters[self.lookup_kwarg] in ('1', '0')):
            self.used_parameters[self.lookup_kwarg] = bool(int(self.used_parameters[self.lookup_kwarg]))

    def expected_parameters(self):
        return [self.lookup_kwarg]

    def choices(self, changelist):
        for lookup, title in (
                (None, _('All')),
                ('0', _('Yes')),
                ('1', _('No'))):
            yield {
                'selected': self.lookup_val == lookup,
                'query_string': changelist.get_query_string({
                    self.lookup_kwarg: lookup,
                }),
                'display': title,
            }

