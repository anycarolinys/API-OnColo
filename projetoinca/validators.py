from rest_framework import serializers
from validate_docbr import CNPJ


def cnpj_valido(cnpj):
        if len(cnpj) != 14:
            raise serializers.ValidationError({'cnpj':'O CNPJ deve ter 14 dígitos'})
        
        numero_cnpj = CNPJ()
        if not numero_cnpj.validate(cnpj):
            raise serializers.ValidationError({'cnpj': 'Este número de CNPJ não é válido'})
        return cnpj

def matricula_valida(matricula):
    if len(matricula) != 6:
        raise serializers.ValidationError({'matricula':'A matrícula deve ter 6 dígitos'})
    return matricula

def nome_valido(nome):
    #r'^[a-zA-Z]+\s[a-zA-Z]+$'
    if not nome.isalpha():
        raise serializers.ValidationError({'nome':'Não inclua números neste campo'})
    return nome
    
def sobrenome_valido(sobrenome):
    if not sobrenome.isalpha():
        raise serializers.ValidationError({'sobrenome':'Não inclua números neste campo'})
    return sobrenome