import requests
import pprint
link = "https://servicodados.ibge.gov.br/api/v3/agregados/7832/periodos/202412/variaveis/109|216|35|36?localidades=N1[all]&classificacao=49[58756]|48[all]"
requisicao= requests.get(link)
info= requisicao.json()
cont = 0
for item in info:
    variavel = item.get('resultados')
    print(variavel)
    print("=============================================================================================")
