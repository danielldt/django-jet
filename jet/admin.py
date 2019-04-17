from django.contrib import admin


class CompactInline(admin.options.InlineModelAdmin):
    template = 'admin/edit_inline/compact.html'
class DefaultInline(admin.options.InlineModelAdmin):
    template = 'admin/edit_inline/default.html'