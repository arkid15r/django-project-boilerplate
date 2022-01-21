"""Core models."""

import uuid

from django.db import models


class TimestampModel(models.Model):
  """Timestamp model."""

  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  class Meta:
    """Timestamp model meta."""

    abstract = True


class UIDModel(models.Model):
  """UID model."""

  uid = models.UUIDField(unique=True, blank=True, null=False)

  def save(self, *args, **kwargs):
    """Set uid on save."""

    if not self.uid:
      self.uid = uuid.uuid4()

    return super(UIDModel, self).save(*args, **kwargs)

  class Meta:
    """UID model meta."""

    abstract = True
