"""
Definition of the
:class:`~django_mri.serializers.input.scan_input.ScanInputSerializer`
class.
"""

from django_mri.models.inputs.scan_input import ScanInput
from django_mri.models.scan import Scan
from rest_framework import serializers


class ScanInputSerializer(serializers.ModelSerializer):
    """
    Serializer for the
    :class:`~django_mri.models.inputs.scan_input.ScanInput`
    model.
    """

    #: Primary key of the actual :class:`django_mri.models.scan.Scan` instance
    #: that was used.
    value = serializers.PrimaryKeyRelatedField(queryset=Scan.objects.all())

    class Meta:
        model = ScanInput
        fields = "id", "key", "value", "run", "definition"
