from django.db import models

class User(models.Model):
    name = models.CharField(max_length=155, null=False)
    role = models.CharField(max_length=35, default='member')    
    email = models.CharField(max_length=155, null=False, unique=True)    
    password = models.CharField(max_length=255, null=False)
    last_login = models.DateTimeField(null=True)    
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'role': self.role,
            'email': self.email,
            'last_login': str(self.last_login) if self.last_login is not None else self.last_login,
            'created_at': str(self.created_at) if self.created_at is not None else self.created_at,
            'updated_at': str(self.updated_at) if self.updated_at is not None else self.updated_at
        }
