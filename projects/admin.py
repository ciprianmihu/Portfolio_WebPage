from django.contrib import admin

from projects.models import ProjectLogo, ProjectFile, ProjectFileComment, ProjectActivity, ProjectActivityMessage, \
    ProjectPayment

admin.site.register(ProjectLogo)
admin.site.register(ProjectFile)
admin.site.register(ProjectFileComment)
admin.site.register(ProjectActivity)
admin.site.register(ProjectActivityMessage)
admin.site.register(ProjectPayment)
