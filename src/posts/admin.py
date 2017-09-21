from django.contrib import admin

# Register your models here.

from .models import Post


class PostAdmin(admin.ModelAdmin):
	list_display  = ["title", "updated","timestamp"]
	list_display_links = ["updated"]
	search_fields = ["title", "content"]
	list_filter = ["updated", "timestamp"]
	#list_editable = ["title"]
	class Meta:
		model = Post






admin.site.register(Post, PostAdmin)