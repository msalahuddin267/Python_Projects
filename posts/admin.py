from django.contrib import admin
from.models import Post,Category,Rating
# Register your models here.

class PostAdmin(admin.ModelAdmin):
   # prepopulated_fields={'slug':('headline',)}

    list_display=['headline']


admin.site.register(Post,PostAdmin)



class CategoryAdmin(admin.ModelAdmin):
   # prepopulated_fields={'slug':('headline',)}
    list_display=['category_name']


admin.site.register(Category,CategoryAdmin)

class RatingAdmin(admin.ModelAdmin):
    pass
   # prepopulated_fields={'slug':('headline',)}
   # list_display=['category_name']


admin.site.register(Rating,RatingAdmin)