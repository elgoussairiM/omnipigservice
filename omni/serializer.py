from rest_framework.serializers import Serializer, FileField, ListField
from rest_framework import serializers
from omni.models import PedigreeNode, Pedigree,Pigeon,StatutPedigree
# Serializers define the API representation.
class UploadSerializer(Serializer):
	file_uploaded = FileField()
	class Meta:
		fields = ['file_uploaded']

# Serializer for multiple files upload.
class MultipleFilesUploadSerializer(Serializer):
	file_uploaded = ListField(child = FileField())
	class Meta:
		fields = ['file_uploaded']

class PigeonSerializer(serializers.ModelSerializer):
	class Meta:
		model = Pigeon
		fields=['pigeonId','pigeonName','numeroSerie','flagPigeon','description']
class PedigreeNodeSerializer(serializers.ModelSerializer):
	pigeon = PigeonSerializer(read_only = True)
	class Meta:
		model=PedigreeNode
		fields=['noeudId','nodeKey','noeudParent','isRoot','pigeon']
class PedigreeSerializer(serializers.ModelSerializer):
	pedigreeNodes= PedigreeNodeSerializer(many=True, read_only=True)
	class Meta:
		model=Pedigree
		fields=['pedigreeId','generation','flagPedigree','pedigreeNodes']
	
class statutSerializer(serializers.ModelSerializer):
	pedigree = PedigreeSerializer(read_only = True)
	class Meta:
		model = StatutPedigree
		fields = ['statut_id','pedigree']