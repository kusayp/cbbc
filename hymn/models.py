from django.db import models

# Create your models here.

class Hymn(models.Model):

    """
     Model for Hymn

    """
    name = models.CharField(max_length=200)
    has_refrain =  models.BooleanField(default=False)
    refrain = models.CharField(max_length=1000, blank=None, null=True)

    class Meta:
        verbose_name_plural = 'Hymns'

    # def get_stanzas(self):
    #     return self.stanzas.all()

    def __str__(self):
        return self.name


class Category(models.Model):

    """
     Model for Category

    """
    name  = models.CharField(max_length=200)
    hymns = models.ManyToManyField(Hymn,
                                     related_name='categorys',
                                    blank=True,default=None)
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Stanza(models.Model):

    """
     Model for Stanza

    """
    content = models.TextField()
    hymn = models.ForeignKey(Hymn, related_name='stanzas')
    class Meta:
        verbose_name_plural = 'Stanzas'

    def __str__(self):
        return self.content
