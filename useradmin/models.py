from django.db import models
from django.contrib.auth.models import AbstractUser
from instituicao.models import Instituicao
from fisioterapeuta.models import Fisioterapeuta
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission

class UserInstituicao(AbstractUser):
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)
    groups = models.ManyToManyField(
        Group,
        verbose_name='grupos',
        blank=True,
        related_name='instituicoes',
        help_text='Os grupos aos quais esta instituição pertence. '
                  'Um usuário será considerado membro de um grupo se for membro de qualquer um dos grupos.',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='permissões de usuário',
        blank=True,
        related_name='instituicao_user_permissions',
        help_text='As permissões específicas de usuário para esta instituição.',
    )

class UserFisioterapeuta(AbstractUser):
    fisioterapeuta = models.ForeignKey(Fisioterapeuta, on_delete=models.CASCADE)
    groups = models.ManyToManyField(
        Group,
        verbose_name='grupos',
        blank=True,
        related_name='fisioterapeutas',
        help_text='Os grupos aos quais este fisioterapeuta pertence. '
                  'Um usuário será considerado membro de um grupo se for membro de qualquer um dos grupos.',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='permissões de usuário',
        blank=True,
        related_name='fisioterapeuta_user_permissions',
        help_text='As permissões específicas de usuário para este fisioterapeuta.',
    )


