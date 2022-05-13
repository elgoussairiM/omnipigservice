from django.db import models

# Create your models here.
class StatutPedigree(models.Model):
	statut_id=models.CharField(max_length=100,default="1")
class Pedigree(models.Model):
	pedigreeId = models.IntegerField(null=True, blank=True)
	generation = models.IntegerField()
	flagPedigree = models.BooleanField(default=True)
	statut = models.OneToOneField(StatutPedigree, related_name='pedigree',on_delete=models.CASCADE,null=True, blank=True)
class PedigreeNode(models.Model):
	noeudId = models.IntegerField(null=True, blank=True)
	nodeKey = models.CharField(max_length=100)
	noeudParent= models.CharField(max_length=100)
	isRoot = models.BooleanField(default=False,null=True, blank=True)
	pedigree = models.ForeignKey(Pedigree,related_name='pedigreeNodes',on_delete=models.CASCADE)
class Pigeon(models.Model):
	pigeonId = models.IntegerField(null=True, blank=True)
	pigeonName = models.CharField(max_length=100)
	numeroSerie = models.CharField(max_length=100)
	description = models.CharField(max_length=100)
	flagPigeon = models.BooleanField(default=True)
	pere= models.ForeignKey("self", related_name="pigeonPere",on_delete=models.CASCADE,null=True, blank=True)
	mere = models.ForeignKey("self",related_name="pigeonMere", on_delete=models.CASCADE,null=True, blank=True)
	pedigree = models.ForeignKey(Pedigree,related_name = "pedigree", on_delete=models.CASCADE)
	pedigreenode = models.OneToOneField(PedigreeNode, related_name="pigeon", on_delete=models.CASCADE,null=True, blank=True)

	

