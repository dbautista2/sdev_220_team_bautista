from django.contrib import admin
from burgorders.models import (
    Order,
    Combo,
    Burger,
    Side,
    Drink,
    Bun,
    Patty,
    Cheese,
    Topping,
    Sauce,
)

admin.site.site_header = "Burg-Orders Console"
admin.site.site_title = "Welcome to Burg-Orders"
admin.site.index_title = "Welcome to Burg-Orders Developer Portal"


class ReadOnlyAdminMixin:
    """Disables all editing capabilities."""

    change_form_template = "admin/view.html"

    def __init__(self, *args, **kwargs):
        super(ReadOnlyAdminMixin, self).__init__(*args, **kwargs)
        self.readonly_fields = self.model._meta.get_all_field_names()

    def get_actions(self, request):
        actions = super(ReadOnlyAdminMixin, self).get_actions(request)
        del actions["delete_selected"]
        return actions

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        pass

    def delete_model(self, request, obj):
        pass

    def save_related(self, request, form, formsets, change):
        pass


# Register your models here.
class OrderAdmin(admin.ModelAdmin, ReadOnlyAdminMixin):
    class Meta:
        model = Order


class ComboAdmin(admin.ModelAdmin, ReadOnlyAdminMixin):
    class Meta:
        model = Order


admin.site.register(Order, OrderAdmin)
admin.site.register(Combo, ComboAdmin)
admin.site.register(Burger)
admin.site.register(Side)
admin.site.register(Drink)
admin.site.register(Bun)
admin.site.register(Patty)
admin.site.register(Cheese)
admin.site.register(Topping)
admin.site.register(Sauce)
