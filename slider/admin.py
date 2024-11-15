from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin

from slider.models import SliderImage


class SliderImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ("title", "image", "order")
    search_fields = ("title",)
    list_editable = ("image", "order")


admin.site.register(SliderImage, SliderImageAdmin)
