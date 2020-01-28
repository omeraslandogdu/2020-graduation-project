from django.db import models


class SoftDeletableQuerySet(models.query.QuerySet):
    def delete(self, trash=True):
        """Overrides normal QuerySet delete to call explicitly object's
        delete() method.
        """
        if trash:
            for m in self:
                m.delete()
        # hard delete
        else:
            super(SoftDeletableQuerySet, self).delete()


class SoftDeletableManager(models.Manager):
    def get_query_set(self):
        query_set = SoftDeletableQuerySet(self.model, using=self._db)

        return query_set.filter(deleted_at__isnull=True)


class TrashedManager(models.Manager):
    def get_query_set(self):
        query_set = super(TrashedManager, self).get_query_set()

        return query_set.filter(deleted_at__isnull=False)
