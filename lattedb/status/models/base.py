from django.db import models

from lattedb.base.models import Base

STATUS_CHOICES = (
    (0, ("Unknown")),
    (1, ("Does not exist")),
    (2, ("Exists")),
    (3, ("On tape")),
)


class FileStatus(Base):
    """ Base table for application
    """

    home = models.TextField(
        null=True,
        blank=True,
        help_text="(Optional) Text: Computing facility where the object resides at",
    )
    directory = models.TextField(
        null=True, blank=True, help_text="(Optional) Text: Directory path to result"
    )
    hdf5path = models.TextField(
        null=True, blank=True, help_text="(Optional) Text: Folder path in hdf5 file"
    )
    status = models.PositiveSmallIntegerField(
        help_text="PositiveSmallInt: Encode categorical status labels",
        choices=STATUS_CHOICES,
    )
    timestamp = models.DateTimeField(
        auto_now_add=True,
        auto_now=False,
        help_text="DateTime:Last time the field was updated.",
    )

    class Meta:
        abstract = True