from django.db import models
from django.dispatch import receiver
import pysolr


class Document(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
#    pub_date = models.DateTimeField('date published')


@receiver(models.signals.post_save, sender=Document, dispatch_uid='unique')
def document_saved(sender, **kwargs):
    print("POST_SAVE")
    solr = pysolr.Solr('http://localhost:8983/solr/django', timeout=10)
    document = kwargs.get('instance')
    solr.add([
        {
            "id": document.id,
            "title": document.title,
            "author": document.author
        }
    ])


@receiver(models.signals.post_delete, sender=Document)
def document_deleted(sender, **kwargs):
    print("POST_DELETED")
    solr = pysolr.Solr('http://localhost:8983/solr/django', timeout=10)
    document = kwargs.get('instance')
    solr.delete(id=document.id)
