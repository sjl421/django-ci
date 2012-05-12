from datetime import datetime
from celery.task import task
from ci.models import Build
from ci.plugins import BUILDERS

@task
def execute_build(build_id, builder):
    build = Build.objects.get(id=build_id)
    build.started = datetime.now()
    build.save()
    Builder = BUILDERS[builder]
    try:
        Builder(build).execute_build()
    finally:
        build.finished = datetime.now()
        build.save()
