from django.contrib import admin

# Register your models here.
from .models import Post, Comment, About, Volunteer, Video, Gallery

class PostAdmin(admin.ModelAdmin):
	list_display = ('post_title', 'pub_date', 'id', 'pk')
	list_filter = ['pub_date', 'professor_name']

class CommentAdmin(admin.ModelAdmin):
	list_display = ('comment_text', 'time_posted', 'verified')
	list_filter = ['verified', 'time_posted']
	
class AboutAdmin(admin.ModelAdmin):
	list_display = ('question', 'time_added')
	
class VolunteerAdmin(admin.ModelAdmin):
	list_display = ('Name', 'Lab_you_want_to_contribute_in', 'reviewed')
	list_filter = ['Time_applied', 'reviewed', 'Lab_you_want_to_contribute_in']

class VideoAdmin(admin.ModelAdmin):
	list_display = ('description', 'uploaded_by')
	list_filter = ['uploaded_by', 'time_uploaded']
	
admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Gallery)
