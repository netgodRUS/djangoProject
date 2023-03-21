# Create a top-level menu item
from djangoProject.main_menu import MenuItem

top_item = MenuItem.objects.create(name='Home', url='/')

# Create a child menu item
child_item = MenuItem.objects.create(name='About', url='/about/', parent=top_item)

# Create a named URL menu item
named_url_item = MenuItem.objects.create(name='Contact', named_url='contact', parent=top_item)
