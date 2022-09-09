from django.contrib import admin

from projects.models import ProjectLogo, ProjectFile, CommentProjectFile

admin.site.register(ProjectLogo)
admin.site.register(ProjectFile)
admin.site.register(CommentProjectFile)
