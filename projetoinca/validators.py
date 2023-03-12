from rest_framework import serializers
from validate_docbr import CNPJ, CPF
from django.utils import timezone


def cpf_valido(cpf):
    if len(cpf) != 11:
            raise serializers.ValidationError({'cpf':'O CPF deve ter 11 digitos'})
        
    numero_cpf = CPF()
    if not numero_cpf.validate(cpf):
        raise serializers.ValidationError({'cpf': 'Este numero de CPF nao e valido'})
    return cpf
    
def cnpj_valido(cnpj):
        if len(cnpj) != 14:
            raise serializers.ValidationError({'cnpj':'O CNPJ deve ter 14 digitos'})
        
        numero_cnpj = CNPJ()
        if not numero_cnpj.validate(cnpj):
            raise serializers.ValidationError({'cnpj': 'Este numero de CNPJ nao e valido'})
        return cnpj

def matricula_valida(matricula):
    if len(matricula) != 6:
        raise serializers.ValidationError({'matricula':'A matricula deve ter 6 digitos'})
    return matricula

def nome_valido(nome):
    if not all(caractere.isalpha() or caractere.isspace() for caractere in nome):
        raise serializers.ValidationError({'nome':'Nao inclua numeros neste campo'})
    return nome

def data_valida(data_retorno):
    if data_retorno is not None:
        if timezone.now().date() > data_retorno:
            raise serializers.ValidationError({'data_retorno':'Data de retorno não pode ser anterior a data atual'})
        return data_retorno

def data_nascimento_valida(data_nascimento):
    if data_nascimento is not None:
        if data_nascimento > timezone.now().date():
            raise serializers.ValidationError({'data_nascimento':'Data de nascimento apos data atual'})
        return data_nascimento
