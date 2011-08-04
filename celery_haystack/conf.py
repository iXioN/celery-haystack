from haystack import constants
from celery_haystack.utils import Setting

DEFAULT_ALIAS = Setting('CELERY_HAYSTACK_USING',
                        getattr(constants, 'DEFAULT_ALIAS', None))

RETRY_DELAY = Setting('CELERY_HAYSTACK_RETRY_DELAY', 5 * 60)

MAX_RETRIES = Setting('CELERY_HAYSTACK_MAX_RETRIES', 1)

DEFAULT_TASK = Setting('CELERY_HAYSTACK_DEFAULT_TASK',
                       'celery_haystack.tasks.CeleryHaystackSignalHandler')

COMMAND_BATCH_SIZE = Setting('CELERY_HAYSTACK_COMMAND_BATCH_SIZE', None)

COMMAND_AGE = Setting('CELERY_HAYSTACK_COMMAND_AGE', None)

COMMAND_REMOVE = Setting('CELERY_HAYSTACK_COMMAND_REMOVE', False)

COMMAND_WORKERS = Setting('CELERY_HAYSTACK_COMMAND_WORKERS', 0)

COMMAND_APPS = Setting('CELERY_HAYSTACK_COMMAND_APPS', [])

COMMAND_VERBOSITY = Setting('CELERY_HAYSTACK_COMMAND_VERBOSITY', 1)
