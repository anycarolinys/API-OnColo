from django.contrib.auth.models import AbstractUser
from django.db import models
from instituicao.models import Instituicao

class InstituicaoUser(AbstractUser):
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE) 
    # Redefinir o campo relacionado com o grupo
    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name='instituicao_users',
        verbose_name='grupos'
    )

    # Redefinir o campo relacionado com as permissões
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='instituicao_users',
        verbose_name='permissões do usuário'
    )
