from django.contrib import admin

from projects.models import ProjectLogo, ProjectFile, CommentProjectFile, ProjectActivity, ProjectActivityMessage

admin.site.register(ProjectLogo)
admin.site.register(ProjectFile)
admin.site.register(CommentProjectFile)
admin.site.register(ProjectActivity)
admin.site.register(ProjectActivityMessage)
