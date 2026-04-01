from django.contrib import admin
from .models import Post  # Importuj svůj model (název se může lišit)

admin.site.register(Post)