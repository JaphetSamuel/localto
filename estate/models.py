from django.db import models
from django.utils.translation import ugettext_lazy as _
from uuid import uuid4

# Create your models here.
#fonction utiles
def image_directory(instance, filename):
    mininame = filename[:6]
    return f"images/{instance.propriete.id}/{str(uuid4())}-{mininame}"

#fin de fonction utiles


class Agent(models.Model):
    nom = models.CharField(max_length=100, verbose_name=_("Nom"))
    prenom = models.CharField(max_length=100, verbose_name=_("Prénom"))
    telephone = models.CharField(max_length=100, verbose_name=_("Téléphone"))
    email = models.EmailField(max_length=100, verbose_name=_("Email"))
    photo = models.ImageField(upload_to='images/agents/', verbose_name=_("Photo"), blank=True)

    def __str__(self):
        return f"{self.nom} {self.prenom}"

class Propriete(models.Model):

    nom = models.CharField(max_length=100, verbose_name=_("Nom de la propriété"))
    prix_vente = models.IntegerField(blank=True, null=True, verbose_name=_("Prix de vente"))
    prix_location = models.IntegerField(blank=True, null=True, verbose_name=_("Prix de location"))
    enVente = models.BooleanField(default=True, verbose_name=_("En vente"))
    enLocation = models.BooleanField(default=True, verbose_name=_("En location"))
    adresse = models.CharField(max_length=100, verbose_name=_("Adresse"), )
    ville = models.CharField(max_length=100, verbose_name=_("Ville"))
    code_postal = models.CharField(max_length=100,blank=True, default="non disponible", verbose_name=_("Code postal"))
    superficie = models.IntegerField(verbose_name=_("Superficie"), blank=True, default=0, help_text="en m²")
    nb_pieces = models.IntegerField(verbose_name=_("Nombre de pièces"), blank=True, default=0)
    nb_chambres = models.IntegerField(verbose_name=_("Nombre de chambres"), blank=True, default=0)
    nb_salles_de_bain = models.IntegerField(verbose_name=_("Nombre de salles de bain"), blank=True, default=0)
    nb_salles_de_douche = models.IntegerField(verbose_name=_("Nombre de salles de douche"), blank=True, default=0)
    nb_toilettes = models.IntegerField(verbose_name=_("Nombre de toilettes"), blank=True, default=0)
    nb_garages = models.IntegerField(verbose_name=_("Nombre de garages"), blank=True, default=0)
    nb_etages = models.IntegerField(verbose_name=_("Nombre d'étages"), blank=True, default=0)
    nb_balcons = models.IntegerField(verbose_name=_("Nombre de balcons"), blank=True, default=0)
    nb_terrasses = models.IntegerField(verbose_name=_("Nombre de terrasses"), blank=True, default=0)

    poster = models.ImageField(upload_to=image_directory, blank=True, verbose_name=_("Galerie"))
    description = models.TextField(blank=True, verbose_name=_("Description"))
    video = models.URLField(blank=True, verbose_name=_("Video"), help_text=" ex : https://www.youtube.com/embed/")

    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, verbose_name=_("Agent"))

    def __str__(self):
        return f"{self.adresse} {self.nom} "
    

#marquer les etablissements proches de la propriete
class Proximite(models.Model):
    Propriete = models.ForeignKey(Propriete, on_delete=models.CASCADE, verbose_name=_("Propriete"))
    etablissement = models.CharField(max_length=100, verbose_name=_("Etablissement"))
    distance = models.IntegerField(verbose_name=_("Distance"))
    def __str__(self):
        return f"{self.etablissement} {self.distance} "

class ProprieteImage(models.Model):
    propriete = models.ForeignKey(Propriete, on_delete=models.CASCADE, verbose_name=_("Propriété"))
    image = models.ImageField(upload_to=image_directory,  verbose_name=_("Image"))

    def __str__(self):
        return f"{self.image}"
    
    class Meta:
        verbose_name = _("Image de la propriété")
        verbose_name_plural = _("Images de Propriété")


    



