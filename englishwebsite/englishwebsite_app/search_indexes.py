from haystack import indexes
from .models import *


class EjercicioIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title_exercise')
    author = indexes.CharField(model_attr='author' )
    description = indexes.CharField(model_attr='description_exercise')
    creation_date = indexes.DateTimeField(model_attr='creation_date')
    idPost = indexes.IntegerField(model_attr='id')

    def get_model(self):
        return Post

#    def index_queryset(self, using=None):
#        """Queremos que se indexen todas los ejercicios que tengan available=True"""
#        return self.get_model().objects.filter(available=True)