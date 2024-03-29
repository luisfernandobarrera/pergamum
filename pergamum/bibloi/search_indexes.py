import datetime
from haystack import indexes
from .models import Article


class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, model_attr='content')
    name = indexes.CharField(model_attr='name')
    # author = indexes.CharField(model_attr='author')
    date = indexes.CharField(model_attr='date')

    def get_model(self):
        return Article

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()

    # def prepare_author(self, obj):
    #     author = u''
    #
    #     if 'author' in self.prepared_data:
    #         author = self.prepared_data['author']
    #
    #     return author
