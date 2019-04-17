from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

class CompactInline(admin.options.InlineModelAdmin):
    template = 'admin/edit_inline/compact.html'
class DefaultInline(DjangoUserAdmin):
    change_form_template = 'admin/edit_inline/default.html'