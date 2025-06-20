from django.db import models

# Event model


class Event(models.Model):
    event_name = models.CharField(max_length=100)
    event_description = models.TextField()
    event_date = models.DateTimeField()
    event_location = models.CharField(max_length=255)
    event_organizer = models.CharField(max_length=100)
    event_capacity = models.PositiveIntegerField()
    event_created_at = models.DateTimeField(auto_now_add=True)
    event_status = models.CharField(
        max_length=20,
        choices=[
            ('upcoming', 'Upcoming'),
            ('ongoing', 'Ongoing'),
            ('completed', 'Completed'),
            ('cancelled', 'Cancelled')
        ],
        default='upcoming'
    )
