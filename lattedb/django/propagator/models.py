from django.db import models
from django.contrib.postgres.fields import JSONField

from lattedb.django.base.models import Base

class Propagator(Base):
    """ Base table for application
    """

    misc = JSONField(
        null=True, blank=True, help_text="(Optional) JSON: {'anything': 'you want'}"
    )

class Hisq(Propagator):
    """
    """

    tag = models.CharField(
        max_length=20,
        null=False,
        blank=True,
        help_text="(Optional) Char(20): User defined tag for easy searches",
    )

    gaugeconfig = models.ForeignKey(
        "gaugeconfig.GaugeConfig",
        on_delete=models.CASCADE,
        related_name="+",
        help_text="ForeignKey pointing to gauge field",
    )
    gaugesmear = models.ForeignKey(
        "gaugesmear.GaugeSmear",
        on_delete=models.CASCADE,
        related_name="+",
        help_text="ForeignKey pointing to gauge link smearing",
    )
    mval = models.DecimalField(
        max_digits=7,
        decimal_places=6,
        null=False,
        help_text="Decimal(7,6): Input valence quark mass",
    )
    naik = models.DecimalField(
        max_digits=7,
        decimal_places=6,
        null=False,
        help_text="Decimal(7,6): Coefficient of Naik term. If Naik term is not included, explicitly set to 0",
    )

    origin = models.TextField(
        null=False, blank=False, help_text="Text: Origin location of the propagator"
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["gaugeconfig", "gaugesmear", "mval", "naik", "origin"],
                name="unique_propagator_hisq",
            )
        ]

class MobiusDWF(Propagator):
    """
    """

    tag = models.CharField(
        max_length=20,
        null=False,
        blank=True,
        help_text="(Optional) Char(20): User defined tag for easy searches",
    )
    gaugeconfig = models.ForeignKey(
        "gaugeconfig.GaugeConfig",
        on_delete=models.CASCADE,
        help_text="ForeignKey pointing to gauge field",
    )
    gaugesmear = models.ForeignKey(
        "gaugesmear.GaugeSmear",
        on_delete=models.CASCADE,
        help_text="ForeignKey pointing to gauge link smearing",
    )
    mval = models.DecimalField(
        max_digits=7,
        decimal_places=6,
        null=False,
        help_text="Decimal(7,6): Input valence quark mass",
    )
    l5 = models.PositiveSmallIntegerField(
        help_text="PositiveSmallInt: Length of 5th dimension"
    )
    m5 = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        null=False,
        help_text="Decimal(3,2): 5th dimensional mass",
    )
    alpha5 = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        null=False,
        help_text="Decimal(3,2): Mobius coefficient [D_mobius(M5) = alpha5 * D_Shamir(M5)]",
    )
    a5 = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        null=False,
        help_text="Decimal(3,2): Mobius kernel parameter [D_mobius = alpha5 * a5 * D_Wilson / (2 + a5 * D_Wilson)]",
    )
    b5 = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        null=False,
        help_text="Decimal(3,2): Mobius kernel parameter [a5 = b5 - c5, alpha5 * a5 = b5 + c5]",
    )
    c5 = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        null=False,
        help_text="Decimal(3,2): Mobius kernal perameter",
    )
    origin = models.TextField(
        null=False, blank=False, help_text="Text: Origin location of the propagator"
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    "gaugeconfig",
                    "gaugesmear",
                    "mval",
                    "l5",
                    "m5",
                    "alpha5",
                    "a5",
                    "b5",
                    "c5",
                    "origin",
                ],
                name="unique_propagator_mobiusdwf",
            )
        ]

class CoherentSeq(Propagator):
    """
    """

    tag = models.CharField(
        max_length=20,
        null=False,
        blank=True,
        help_text="(Optional) Char(20): User defined tag for easy searches",
    )
    propagator = models.ForeignKey(
        "propagator.Propagator",
        on_delete=models.CASCADE,
        related_name='+',
        help_text="ForeignKey that link to a coherent propagator",
    )
    groupsize = models.PositiveSmallIntegerField(
        help_text="PositiveSmallint: Total number of propagators sharing a coherent sink"
    )
    groupindex = models.PositiveSmallIntegerField(
        help_text="PositiveSmallInt: A group index indicating which coherent sink group the propagator belongs to"
    )
    sink = models.ForeignKey(
        "hadron.Hadron",
        on_delete=models.CASCADE,
        related_name="+",
        help_text="ForeignKey: Pointer to sink interpolating operator",
    )
    sinksep = models.SmallIntegerField(
        help_text="SmallInt: Source-sink separation time"
    )
    momentum = models.SmallIntegerField(
        help_text="SmallInt: Sink momentum in units of 2 pi / L"
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["propagator", "groupsize", "groupindex", "sink", "sinksep", "momentum"],
                name="unique_propagator_coherentseq",
            )
        ]


class FeynmanHellmann(Propagator):
    """
    """
    tag = models.CharField(
        max_length=20,
        null=False,
        blank=True,
        help_text="(Optional) Char(20): User defined tag for easy searches",
    )
    propagator0 = models.ForeignKey(
        "propagator.Propagator",
        on_delete=models.CASCADE,
        related_name="+",
        help_text="ForeignKey linking source side propagator"
    )
    current = models.ForeignKey(
        "current.Current",
        on_delete=models.CASCADE,
        related_name="+",
        help_text="ForeignKey linking current insertion operator"
    )
    propagator1 = models.ForeignKey(
        "propagator.Propagator",
        on_delete = models.CASCADE,
        related_name="+",
        help_text="ForeignKey linking sink side propagator"
    )
    momentum = models.SmallIntegerField(
        help_text="SmallInt: Current insertion momentum in units of 2 pi / L"
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["propagator0", "current", "propagator1", "momentum"],
                name="unique_propagator_feynmanhellmann"
            )
        ]