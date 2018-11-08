from django.contrib import admin
from games_review.models import *

admin.site.register(Type)

class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'release_date', )
    search_fields = ('name', )
    list_filter = ('types', )

admin.site.register(Game, GameAdmin)
