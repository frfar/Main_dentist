from django.contrib import admin, messages
from django.utils.translation import ngettext
from . models import Article, Category

admin.site.site_header = "(Dream family Dental) administration"

# Register your models here.
def make_published_category(modeladmin, request, queryset):
    updated = queryset.update(status=True)
    modeladmin.message_user(request, ngettext(
        'successfully published %d category.',
        'successfully published %d categories.',
        updated,
    ) % updated, messages.SUCCESS)
make_published_category.short_description = "Publish selected Categories"


def make_drafted_category(modeladmin, request, queryset):
    updated = queryset.update(status=False)
    modeladmin.message_user(request, ngettext(
        'successfully drafted %d category.',
        'successfully drafted %d categories.',
        updated,
    ) % updated, messages.SUCCESS)
make_drafted_category.short_description = "Drarf selected Categories"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position','title','slug', 'parent','status')
    list_filter = (['status'])
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    actions = [make_published_category , make_drafted_category]

admin.site.register(Category, CategoryAdmin)

def make_published(modeladmin, request, queryset):
    updated = queryset.update(status='p')
    modeladmin.message_user(request, ngettext(
        'successfully published %d article.',
        'successfully published %d articles.',
        updated,
    ) % updated, messages.SUCCESS)
make_published.short_description = "Publish selected Articles"


def make_drafted(modeladmin, request, queryset):
    updated = queryset.update(status='d')
    modeladmin.message_user(request, ngettext(
        'successfully drafted %d article.',
        'successfully drafted %d articles.',
        updated,
    ) % updated, messages.SUCCESS)
make_drafted.short_description = "Drarf selected Articles"

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','thumbnail_tag','slug','category_to_str','status', 'publish')
    list_filter = ('publish','status')
    search_fields = ('title','description')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['status', '-publish']
    actions = [make_published , make_drafted]

    def category_to_str(self, obj):
        return ", ".join([category.title for category in obj.category.all()])
    category_to_str.short_description = "category"

admin.site.register(Article, ArticleAdmin)
