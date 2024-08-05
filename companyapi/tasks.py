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
