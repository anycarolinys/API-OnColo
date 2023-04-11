from .models import Instituicao
from .serializers import InstituicaoSerializer
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from useradmin.models import UserInstituicao
from rest_framework.response import Response


class InstituicaoViewSet(viewsets.ModelViewSet):
    queryset = Instituicao.objects.all()
    serializer_class = InstituicaoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome', 'cnpj']

    def create(self, request, *args, **kwargs):
        nome = request.data.get('nome')
        cnpj = request.data.get('cnpj')
        email = request.data.get('email')
        senha = request.data.get('senha')

        instituicao = Instituicao.objects.create(nome=nome, cnpj=cnpj, email=email, senha=senha)
        instituicao.save()

        id = instituicao.id
        UserInstituicao.objects.create_user(username=email, email=email, password=senha, instituicao_id=id)

        return Response({'detail': 'Cadastrado com sucesso'})

