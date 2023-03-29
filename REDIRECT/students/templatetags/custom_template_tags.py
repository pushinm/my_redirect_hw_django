from django import template
register = template.Library()

@register.simple_tag(takes_context=True)
def setvar(context, val=None):
  context['max_cols'] = val
  print(context)
  return context['max_cols']