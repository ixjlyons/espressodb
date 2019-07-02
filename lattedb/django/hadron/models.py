from django.db import models
from django.contrib.postgres.fields import JSONField

from lattedb.django.base.models import Base

class Hadron(Base):
    """ Base table for application
    """

    misc = JSONField(
        null=True, blank=True, help_text="(Optional) JSON: {'anything': 'you want'}"
    )

class Basak(Hadron):
    """
    """

    tag = models.CharField(
        max_length=20,
        null=False,
        blank=True,
        help_text="(Optional) Char(20): User defined tag for easy searches",
    )

    hadron = models.CharField(
        max_length=20, null=False, blank=False, help_text="Char(20): Hadron name"
    )

    lambda_index = models.CharField(
        max_length=10,
        null=False,
        blank=False,
        help_text="Char(10): Irreducible representations of O^D_h (improper point group)",
    )

    k_index = models.CharField(
        max_length=1,
        null=False,
        blank=False,
        help_text="Char(1): k-th representation of O^D_h irrep.",
    )

    spin = models.CharField(
        max_length=3, null=False, blank=False, help_text="Char(3): Total spin"
    )

    spin_z = models.CharField(
        max_length=3, null=False, blank=False, help_text="Char(3): Spin in z-direction"
    )

    smearing = models.CharField(
        max_length=255,
        null=False,
        blank=True,
        help_text="(Optional) Char(255): Operator smearing",
    )

    description = models.TextField(
        null=False,
        blank=True,
        help_text="(Optional) Text: Description of the interpolating operator",
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    "hadron",
                    "lambda_index",
                    "k_index",
                    "spin",
                    "spin_z",
                    "smearing",
                ],
                name="unique_hadron_basak",
            )
        ]