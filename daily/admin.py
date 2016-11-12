from django.contrib import admin
from models import Ideas, IdeaComment,IdeaCategory

class IdeasAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'date',
        'description',
    )

admin.site.register(Ideas,IdeasAdmin)

class IdeasCommentAdmin(admin.ModelAdmin):
    list_display = (
        'idea',
        'created',
        'author',
        'comment',
    )

admin.site.register(IdeaComment, IdeasCommentAdmin)


class IdeasCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'idea',
        'created',
        'category',
    )

admin.site.register(IdeaCategory, IdeasCategoryAdmin)
