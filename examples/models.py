
from django.db import models


class Book(models.Model):
    HARDCOVER = 1
    PAPERBACK = 2
    EBOOK = 3
    BOOK_TYPES = (
        (HARDCOVER, 'Hardcover'),
        (PAPERBACK, 'Paperback'),
        (EBOOK, 'E-book'),
    )
    title = models.CharField(max_length=50)
    publication_date = models.DateField(null=True)
    author = models.CharField(max_length=30, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    pages = models.IntegerField(blank=True, null=True)
    book_type = models.PositiveSmallIntegerField(choices=BOOK_TYPES)

    timestamp = models.DateField(auto_now_add=True, auto_now=False)



class Categorie(models.Model):
    """Model definition for Categorie."""
    nom = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Categorie."""

        verbose_name = 'Categorie'
        verbose_name_plural = 'Categories'

    def __str__(self):
        """Unicode representation of Categorie."""
        return self.nom.upper()

    

    def get_absolute_url(self):
        """Return absolute url for Categorie."""
        return ('')

    # TODO: Define custom methods here
############################################################
class Article(models.Model):
    nom = models.CharField(max_length=100)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name="article_cat")
    quantite  = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    """Model definition for Article."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for Article."""

        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        """Unicode representation of Article."""
        return self.nom.upper()

    def get_absolute_url(self):
        """Return absolute url for Article."""
        return ('')

    # TODO: Define custom methods here

    @property
    def arrivee(self):
        ps = ArrivageExistant.objects.filter(article_id=self.id)
        sortie = Sortie.objects.filter(article_id=self.id)
        dd = 0
        s = 0
        for c in ps:
            s = s + c.quantite 

        for i in sortie:
            dd = dd + i.quantite

        
        return ((s+ self.quantite) - dd)
##############################################################################"
class ArrivageExistant(models.Model):
    """Model definition for ArrivageExistant."""

    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="article_come")
    quantite  = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    

    # TODO: Define fields here

    class Meta:
        """Meta definition for ArrivageExistant."""

        verbose_name = 'Arrivage Existant'
        verbose_name_plural = 'Arrivage Existants'
        ordering = ["-created"]

    def __str__(self):
        """Unicode representation of ArrivageExistant."""
        return "{} ({})".format(self.article, self.quantite)


    def get_absolute_url(self):
        """Return absolute url for ArrivageExistant."""
        return ('')

    # TODO: Define custom methods here

class Sortie(models.Model):
    """Model definition for Sortie."""
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="article_sortie")
    quantite  = models.IntegerField(default=0)
    motif = models.TextField(blank=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Sortie."""

        verbose_name = 'Sortie'
        verbose_name_plural = 'Sorties'

    def __str__(self):
        """Unicode representation of Sortie."""
        return "{} ({})".format(self.article, self.quantite)
        

    def get_absolute_url(self):
        """Return absolute url for Sortie."""
        return ('')

    # TODO: Define custom methods here

