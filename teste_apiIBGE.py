import requests
import pprint
link = "https://servicodados.ibge.gov.br/api/v3/agregados/7832/periodos/202412/variaveis/109|216|35|36?localidades=N1[all]&classificacao=49[58756]|48[all]"
requisicao= requests.get(link)
info= requisicao.json()
cont = 0
rendMedio=info[3]['resultados']
print("RENDIMENTO MEDI0 PRODUTOS AGRO BRASIL safra 2024")
for i in rendMedio:
    rendProd=i['series'][0]['serie']['202412']
    nomeProd=list(i['classificacoes'][1]['categoria'].values())[0]

    print("| Produto: "+nomeProd+" |  Rendimento médio: \033[95m"+rendProd+"kg\033[0m")
    print("\033[92m============================================================\033[0m")



