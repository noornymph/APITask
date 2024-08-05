"""
This module contains celery tasks.
"""

from celery import shared_task


@shared_task
def product(x, y):
    """
    A simple Celery task that adds two numbers.
    """
    return x * y


@shared_task
def periodic_task():
    """
    A periodic celery task.
    """
    print("This is a periodic task")
