from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Prayer(MPTTModel):
    parent = TreeForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    publish = models.BooleanField(default=True)
    link = models.JSONField(default=dict)

    @classmethod
    def get_object(cls, pk):
        try:
            return cls.objects.get(pk=pk)
        except cls.DoesNotExist:
            return None

    @classmethod
    def _get_hierarchy_data(cls, node, data: dict):
        if node.get_children():
            for item in node.get_children():
                data['children'].append(
                    cls._get_hierarchy_data(item, {'description': item.name, 'children': [], 'id': item.id}))
        return data

    def get_hierarchy(self):
        data = []
        node_data = {'description': self.name, 'children': [], 'id': self.id}
        if self.get_children():
            node_data = Prayer._get_hierarchy_data(self, node_data)
            data.append(node_data)
        else:
            data.append(node_data)
        return data

    @classmethod
    def get_full_hierarchy(cls):
        data = []
        roots = cls.objects.filter(parent__isnull=True).prefetch_related('parent')
        for node in roots:
            node_data = {'description': node.name, 'children': [], 'id': node.id}
            data.append(cls._get_hierarchy_data(node, node_data))
        return data

    def update_links(self, links: list[int]):
        if not self.link.get("link"):
            self.link["link"] = []
        self.link["link"] = list(set(links))


class Category(MPTTModel):
    parent = TreeForeignKey('self', null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    prayer = models.ManyToManyField(Prayer)
    index = models.BooleanField(default=True)
    publish = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)

    @classmethod
    def _get_hierarchy_data(cls, node, data: dict):
        if node.get_children():
            for item in node.get_children():
                data['children'].append(
                    cls._get_hierarchy_data(item, {'description': item.title, 'children': [], 'id': item.id}))
        return data

    def get_hierarchy(self):
        data = []
        node_data = {'description': self.title, 'children': [], 'id': self.id}
        if self.get_children():
            node_data = Category._get_hierarchy_data(self, node_data)
            data.append(node_data)
        else:
            data.append(node_data)
        return data

    @classmethod
    def get_full_hierarchy(cls):
        data = []
        roots = cls.objects.filter(parent__isnull=True).prefetch_related('parent')
        for node in roots:
            node_data = {'description': node.title, 'children': [], 'id': node.id}
            data.append(cls._get_hierarchy_data(node, node_data))
        return data


class Phrase(models.Model):
    TYPE_CHOICES = [
        (1, 'توضیح دعا'),
        (2, 'متن دعا'),  # between "#"
        (3, 'متن قرآن')  # between "$"
    ]

    text = models.TextField()
    order = models.CharField(max_length=10, primary_key=True)
    type = models.PositiveSmallIntegerField(default=1, choices=TYPE_CHOICES)
    prayer = models.ForeignKey(Prayer, on_delete=models.CASCADE)
    deleted = models.BooleanField(default=False)
