from django.db import models
from django.template.defaultfilters import slugify


class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  email = models.EmailField()
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)
  slug = models.SlugField(unique=True, blank=True, null=True)


  def save(self, *args, **kwargs):
        # Generate slug only when field is empty
        if not self.slug:
            base_slug = slugify(f"{self.firstname} {self.lastname}")
            unique_slug = base_slug
            num = 1
            # Check unique ID for slug
            while Member.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{num}"
                num += 1
            self.slug = unique_slug
        super().save(*args, **kwargs)

  def __str__(self):
    return f"{self.firstname} {self.lastname}"