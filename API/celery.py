"""
This module contains celery code.
"""

from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "API.settings")

app = Celery("API")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    """
    A debug task that prints the request information.
    """
    print(f"Request: {self.request!r}")
