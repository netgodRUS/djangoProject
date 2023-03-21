from django.forms import models


class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')
    url = models.CharField(max_length=255, null=True, blank=True)
    named_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name