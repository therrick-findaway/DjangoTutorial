from polls.models import Question
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Shows all questions and their respective questions currently in the database"

    def handle(self, *args, **options):
        try:
            for num, question in enumerate(Question.objects.all()):
                print("Question " + str(num + 1) + ": " + question.question_text)
                for choice in question.choice_set.all():
                    print("\t - " + choice.choice_text)
        except Question.DoesNotExist:
            raise CommandError("There aren't any questions.")
