from django.contrib import admin
from .models import Post, Category, Comment, PostCategory, Author

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(PostCategory)
admin.site.register(Comment)

