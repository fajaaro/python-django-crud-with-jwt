from django.db import models

from api_auth.models import User

class Product(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, db_column='author_id')
    name = models.CharField(max_length=155, null=False)    
    slug = models.CharField(max_length=155, null=False, unique=True)
    price = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'products'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'slug': self.slug,
            'price': self.price,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'author': self.author_to_json()
        }

    def author_to_json(self):
        return {
            'id': self.author.id,
            'name': self.author.name,
            'role': self.author.role,
            'email': self.author.email, 
        }
