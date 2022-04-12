from django.contrib import admin
from .models import Video, Illustration, Review, News, IllustrationLike, NewsLike, VideoLike, ReviewLike


@admin.register(Video)
@admin.register(Illustration)
@admin.register(Review)
@admin.register(News)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'game_title', 'author')


@admin.register(VideoLike)
@admin.register(IllustrationLike)
@admin.register(ReviewLike)
@admin.register(NewsLike)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'post')
