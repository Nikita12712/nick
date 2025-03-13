from django import template
from datetime import datetime

register = template.Library()

@register.simple_tag
def current_date(format_string="%Y-%m-%d"):
    return datetime.now().strftime(format_string)

register = template.Library()

@register.simple_tag
def truncate_text(text, length=50):
    if len(text) > length:
        return text[:length] + "..."
    return text

register = template.Library()

@register.inclusion_tag('includes/user_profile.html')
def user_profile(user):
    return {'user': user}