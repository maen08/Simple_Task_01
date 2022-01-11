from django.db import models


CATEGORIES = (
    ('OFFICE', 'Office'),
    ('MANUAL WORK', 'Manual work'),
    ('CODING', 'Coding')
)

class Task(models.Model):
    task_name = models.CharField(max_length=100)
    task_description = models.TextField()
    task_status = models.BooleanField(default=False)
    task_due_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=30, choices=CATEGORIES)

    def __str__(self) -> str:
        return self.task_name