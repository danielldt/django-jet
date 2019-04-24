from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

class CompactInline(admin.options.InlineModelAdmin):
    template = 'admin/edit_inline/compact.html'
class DefaultUserInline(DjangoUserAdmin):
    change_form_template = 'admin/edit_inline/default.html'
    add_form_template = 'admin/edit_inline/default.html'
class DefaultInline(admin.ModelAdmin):
    change_form_template = 'admin/edit_inline/default.html'
    add_form_template = 'admin/edit_inline/default.html'