from django.contrib import admin
from .models import Video, Illustration, Review, New, IllustrationLike, NewLike, VideoLike, ReviewLike

admin.site.register(Video)
admin.site.register(VideoLike)
admin.site.register(Illustration)
admin.site.register(IllustrationLike)
admin.site.register(Review)
admin.site.register(ReviewLike)
admin.site.register(New)
admin.site.register(NewLike)
