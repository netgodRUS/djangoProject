from django import template
from django.urls import reverse

from myapp.models import MenuItem

register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    # Retrieve the menu items from the database
    menu_items = MenuItem.objects.filter(parent=None)

    # Determine which items should be expanded
    current_url = context['request'].path
    selected_item = None
    expanded_items = set()
    for item in menu_items:
        if item.url == current_url or item.named_url == current_url:
            selected_item = item
            expanded_items.add(item)
            parent = item.parent
            while parent is not None:
                expanded_items.add(parent)
                parent = parent.parent
            break

    # Render the HTML for the menu
    html = '<ul>'
    for item in menu_items:
        html += draw_menu_item(item, selected_item, expanded_items)
    html += '</ul>'

    return html

def draw_menu_item(item, selected_item, expanded_items):
    html = '<li>'
    if item == selected_item:
        html += '<a class="active" href="{}">{}</a>'.format(get_menu_item_url(item), item.name)
    else:
        html += '<a href="{}">{}</a>'.format(get_menu_item_url(item), item.name)

    if item in expanded_items:
        html += '<ul>'
        for child_item in item.children.all():
            html += draw_menu_item(child_item, selected_item, expanded_items)
        html += '</ul>'

    html += '</li>'
    return html

def get_menu_item_url(item):
    if item.url:
        return item.url
    elif item.named_url:
        return reverse(item.named_url)
    else:
        return '#'
