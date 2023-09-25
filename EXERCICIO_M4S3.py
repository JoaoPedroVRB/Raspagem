from requests_html import HTMLSession

sessao = HTMLSession()

url = 'https://www.olx.com.br/eletronicos-e-celulares/estado-sp?q=iphone'

resposta = sessao.get(url)

links = resposta.html.find("a[class='olx-ad-card__link-wrapper']")

anuncios = []

for l in links:
    url_iphone = l.attrs['href']
    resposta_iphone = sessao.get(url_iphone)
    titulo = resposta_iphone.html.find("h1",first = True).text
    #OUTRAS FORMAS DE FAZER
    # titulo = resposta_iphone.html.find("h1[data-ds-component='DS-Text']")[0].text
    # titulo = resposta_iphone.html.find("h1[class='ad__sc-45jt43-0 htAiPK sc-jTzLTM iXcEhO']")[0].text
    preco = resposta_iphone.html.find("span[class='ad__sc-1wimjbb-1 hoHpcC sc-jTzLTM kNahTW']")[0].text
    iphone = {'url':url_iphone, 
              'titulo':titulo,
              'preco':preco
              }
    anuncios.append(iphone)

for anuncio in anuncios:
    print(f"URL: {anuncio['url']}")
    print(f"Título: {anuncio['titulo']}")
    if anuncio['preco'] == '':
        print('Preço: Não Informado')
    else :
        print(f"Preço: {anuncio['preco']}")
    print()