from django.contrib import admin
from django.utils.safestring import mark_safe

from movies.models import Category, Movie

admin.site.site_header = "IPBD Backoffice"
admin.site.site_title = admin.site.site_header
admin.site.register(Category)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):

    list_display = ('title', 'release_date', 'user_full_name', 'category', 'rating')
    list_filter = ('category', 'user')
    search_fields = ('title', 'director_name', 'category__name')

    def user_full_name(self, obj):
        return "{0} {1}".format(obj.user.first_name, obj.user.last_name)

    user_full_name.short_description = "Movie owner"
    user_full_name.admin_order_field = "user__first_name"

    def get_image_html(self, movie):
        return mark_safe('<img src="{0}" alt="{1}" height="100">'.format(movie.image, movie.title))
    get_image_html.short_description = "Movie poster"

    readonly_fields = ('created_at', 'modified_at', 'get_image_html')
    fieldsets = (
        (None, {
            'fields': ('title', 'summary')
        }),
        ("Category & Rating", {
            'fields': ('category', 'rating')
        }),
        ("Additional info", {
            'fields': ('director_name', 'release_date', 'get_image_html', 'image', 'user')
        }),
        ("Creation & modification dates", {
            'fields': ('created_at', 'modified_at'),
            'classes': ('collapse',),
            'description': 'This fields are auto-generated'
        })
    )