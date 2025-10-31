





from django.db import models
from django.utils import timezone

from django.contrib.auth import get_user_model 

# Get the User model dynamically
User = get_user_model()

# --- Model Definitions ---

class Course(models.Model):
    """Represents a major field of study (e.g., Computer Science, Mechanical)."""
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    
    def __str__(self):
        return self.title

class Topic(models.Model):
    """Represents a specific subject or class within a Course."""
    
    YEAR_CHOICES = [
        ('1st', '1st Year'),
        ('2nd', '2nd Year'),
        ('3rd', '3rd Year'),
        ('4th', '4th Year'),
    ]

    title = models.CharField(max_length=200)
   
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='topics') 
    year = models.CharField(max_length=3, choices=YEAR_CHOICES)
    
    class Meta:
        # Ensures topics are unique within a specific course and year
        unique_together = ('course', 'title', 'year')

    def __str__(self):
        return f"{self.title} ({self.year})"


class Resource(models.Model):
    """Represents a specific learning material (e.g., PDF, link, ebook)."""
    
    RESOURCE_TYPES = [
        ('FILE', 'File Upload (PDF, DOCX)'),
        ('LINK', 'External Link (Video, Article)'),
        ('TEXT', 'Short Text/Code Snippet'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    resource_type = models.CharField(max_length=4, choices=RESOURCE_TYPES)
    
    # Relationships
    # Use string reference 'Topic' since Topic is defined in the same file
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE, related_name='resources') 
    # Use string reference 'auth.User' for the default Django User model
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='uploaded_resources') 
    
    # Data Fields (mutually exclusive based on resource_type)
    file = models.FileField(upload_to='resources/files/', blank=True, null=True)
    external_url = models.URLField(max_length=500, blank=True, null=True)
    
    # Metadata
    uploaded_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title

    def get_resource_type_display(self):
        """Helper to get the human-readable resource type."""
        return dict(self.RESOURCE_TYPES).get(self.resource_type) 
