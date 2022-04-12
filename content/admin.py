from django.contrib import admin
from .models import Video, Illustration, Review, New, IllustrationLike, NewLike, VideoLike, ReviewLike


@admin.register(Video)
@admin.register(Illustration)
@admin.register(Review)
@admin.register(New)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'game_title', 'author')


@admin.register(VideoLike)
@admin.register(IllustrationLike)
@admin.register(ReviewLike)
@admin.register(NewLike)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'post')
