from django.contrib import admin

from guiaTurismo.models import City, Category, Guide, Tour


class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')
    search_fields = ('description',)


class GuideAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',
                    'phrase',
                    'photo',
                    'facebook',
                    'instagram',
                    'phone',
                    'email',)


class TourAdmin(admin.ModelAdmin):
    list_display = ('id', 'guide',
                    'name',
                    'price',
                    'url_map_image',
                    'category')


admin.site.register(City, CityAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Guide, GuideAdmin)
admin.site.register(Tour, TourAdmin)
