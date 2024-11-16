from rest_framework import serializers
from .models import Evento, Participante  # Certifique-se de que esses modelos existem

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento  # Ajuste com o nome do seu modelo
        fields = '__all__'

class ParticipanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participante  # Ajuste com o nome do seu modelo
        fields = '__all__'
