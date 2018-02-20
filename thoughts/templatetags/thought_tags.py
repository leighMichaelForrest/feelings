from django import template

from thoughts.forms import ThoughtForm
from thoughts.models import Thought

register = template.Library()

@register.inclusion_tag('thoughts/_form.html')
def thought_form(thought=None):
    form = ThoughtForm(instance=thought)
    return {'form': form}
