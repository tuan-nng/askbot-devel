"""
"""
from django.core.management.base import NoArgsCommand
from django.db.models import signals
from askbot import models

class Command(NoArgsCommand):
    """Command class for "fix_answer_counts" 
    """

    def remove_save_signals(self):
        """removes signals on model pre-save and
        post-save, so that there are no side-effects
        besides actually updating the answer counts
        """
        signals.pre_save.receivers = []
        signals.post_save.receivers = []

    def handle(self, *arguments, **options):
        """function that handles the command job
        """
        self.remove_save_signals()
        questions = models.Question.objects.all()
        for question in questions:
            question.update_answer_count()
