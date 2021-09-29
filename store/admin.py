from django.contrib import admin
from .models import Product, Variation, ReviewRating, ProductGallery
import admin_thumbnails
from django.utils.html import format_html
# Register your models here.
@admin_thumbnails.thumbnail('image')
class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','price','stock','modified_date','is_available','firm_url')
    prepopulated_fields = {'slug':('product_name',)}
    inlines = [ProductGalleryInline]

    def show_firm_url(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.firm_url)

    show_firm_url.short_description = "Firm URL"    

class VariationAdmin(admin.ModelAdmin):
    list_display = ('product','variation_category','variation_value','is_active')
    list_editable = ('is_active',)
    list_filter = ('product','variation_category','variation_value')

admin.site.register(Product,ProductAdmin)
admin.site.register(Variation,VariationAdmin)
admin.site.register(ReviewRating)
admin.site.register(ProductGallery)
