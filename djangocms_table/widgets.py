from django.conf import settings
from django.forms.widgets import Textarea
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.utils.translation.trans_real import get_language
from djangocms_table.utils import static_url


class TableWidget(Textarea):
    class Media:
        js = [static_url(path) for path in (
                'js/handsontable.full.min.js',
                'js/json2.js',
            )]
        css = {
            'all': [static_url(path) for path in (
                'css/handsontable.full.min.css',
            )],
        }

    def render_textarea(self, name, value, attrs=None, renderer=None):
        return super(TableWidget, self).render(name, value, attrs, renderer)

    def render_additions(self, name, value, attrs=None):
        language = get_language().split('-')[0]
        context = {
            'name': name,
            'language': language,
            'data': value,
            'STATIC_URL': settings.STATIC_URL,
        }
        return mark_safe(render_to_string(
            'cms/plugins/widgets/table.html', context))

    def render(self, name, value, attrs=None, renderer=None):
        return self.render_textarea(name, value, attrs, renderer) + \
            self.render_additions(name, value, attrs)
