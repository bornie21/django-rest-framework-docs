import markdown2
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
from rest_framework.utils.formatting import markup_description



register = template.Library()


@register.filter(name='markdown')
@stringfilter
def markdown(value):

    return mark_safe(markdown2.markdown(value))
