from django.contrib.auth.models import User, Group
from rest_framework import serializers
from core.models import Duvida


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class DuvidaSerializer(serializers.HyperlinkedModelSerializer):
    disciplina = serializers.StringRelatedField(many=False)

    class Meta:
        model = Duvida
        fields = ('url', 'autor','titulo','texto','imagem', \
        	'audio','video','like','deslike','disciplina','date_create','last_update')
	