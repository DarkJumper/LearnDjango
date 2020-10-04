from django.db import models


class poll(models.Model):
    name = models.CharField(max_length=256)  # Char feld länge für Datenbank
    slug = models.SlugField()

    def __str__(self):
        return "{0} (slug: {1})".format(self.name, self.slug)


class choice(models.Model):
    # Verbinden mit Poll class via Django
    # CASCADE damit werden alle werte gelöscht wenns sie nicht mehr genutzt werden
    poll = models.ForeignKey(to="poll", on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    votes = models.IntegerField(default=0)
    # Wenn ein feld leer bleiben soll in der Datenbank
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return "{0}: {1}".format(self.poll.name, self.name)
