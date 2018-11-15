from home.models import Message
from rest_framework import serializers


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('imei', 'momsn', 'transmit_time', 'iridium_latitude', 'iridium_longitude', 'iridium_cep', 'data')