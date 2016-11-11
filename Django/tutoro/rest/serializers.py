from django.contrib.auth.models import User, Group
from rest_framework import serializers
from core.models import Duvida, Comentario


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'password', 'first_name', 'last_name')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class DuvidaSerializer(serializers.HyperlinkedModelSerializer):
    disciplina = serializers.StringRelatedField(many=False)
    assuntos = serializers.StringRelatedField(many=True)

    class Meta:
        model = Duvida
        fields = ('url', 'autor','texto','imagem', \
        	'audio','video','like','deslike','disciplina','assuntos','respondida','date_create','last_update')

class ComentarioSerializer(serializers.HyperlinkedModelSerializer):
    duvida = serializers.StringRelatedField(many=False)

    class Meta:
        model = Comentario
        fields = ('url', 'duvida','autor','titulo','texto','imagem', \
        	'audio','video','like','deslike','date_create','last_update')
