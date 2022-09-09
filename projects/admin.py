from django.contrib import admin

from projects.models import ProjectLogo, ProjectFile, CommentProjectFile, ProjectActivity

admin.site.register(ProjectLogo)
admin.site.register(ProjectFile)
admin.site.register(CommentProjectFile)
admin.site.register(ProjectActivity)
