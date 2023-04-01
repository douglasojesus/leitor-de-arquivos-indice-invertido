#ATENÇÃO: QUANDO APAGAR O ARQUIVO DE UMA PALAVRA, É INTERESSANTE APAGAR A APALVRA DO DICIONARIO TAMBEM####


#abrindo arquivo para leitura
import ast
import os
import sys

#ler argumentos predefinidos
def objetivo():
    entrada = sys.argv[1::]
    return entrada

#abrir diretório
def abrirDiretorio(caminho):
    arquivos = []
    os.chdir(r'{}'.format(caminho))
    print('Esse diretório tem os seguintes arquivos em txt:')
    for i in range(len(os.listdir('.'))):
        if os.listdir('.')[i][-3:] == 'txt' and os.listdir('.')[i] != 'indiceInvertido.txt':
            print(f"{i+1}. {os.listdir('.')[i]}")
            arquivos.append(os.listdir('.')[i])
    return arquivos #retorna uma lista de arquivos txt no diretório

#abrir o arquivo e retornar o texto incluso
def abrirArquivo(chave):
    with open(chave, 'r', encoding='utf-8') as arquivo:
        texto = arquivo.read()
    return texto

#busca da palavra dentro do dicionario
def buscaIndice(dicionario, busca):
    if busca in dicionario.keys():
        return dicionario[busca] #retorna um dicionário com a quantidade de ocorrencias em cada arquivo

#retornar os dados do indice
def lerIndice(enderecodoindice):
    try:
        with open(r'{}'.format(enderecodoindice), 'r', encoding='utf-8') as arquivodic: #ATENÇÃO AO R+
            lista_arquivos_salvos = ast.literal_eval(arquivodic.readline()[:-1])
            dicionario=ast.literal_eval(arquivodic.readline()[:-1])

        return lista_arquivos_salvos, dicionario
    except FileNotFoundError:
        arquivodic = open(r'{}'.format(enderecodoindice), 'w')
        chaves='{}'
        arquivodic.write(f'[]\n{chaves}\n')
        lista_arquivos_salvos=[]
        dicionario={}
        arquivodic.close()
        return lista_arquivos_salvos, dicionario

#salvar dicionario atualizado e a lista_arquivos_salvos atualizado
def salvarIndice(dicionario, lista_arquivos_salvos, enderecodoindice):
    with open(r'{}'.format(enderecodoindice), 'w', encoding='utf-8') as arquivodic:
        arquivodic.write(f'{lista_arquivos_salvos}\n')
        arquivodic.write(f'{str(dicionario)}\n')

#funcao que registra todas as stopWords
def stopWords():
    palavras=['de', 'a', 'o', 'que', 'e', 'do', 'da', 'em', 'um', 'para', 'é', 'com', 'não', 'uma', 
'os', 'no', 'se', 'na', 'por', 'mais', 'as', 'dos', 'como', 'mas', 'foi', 'ao', 'ele', 'das', 'tem', 'à', 
'seu', 'sua', 'ou', 'ser', 'quando', 'muito', 'há', 'nos', 'já', 'está', 'eu', 'também', 'só', 'pelo', 
'pela', 'até', 'isso', 'ela', 'entre', 'era', 'depois', 'sem', 'mesmo', 'aos', 'ter', 'seus', 'quem', 
'nas', 'me', 'esse', 'eles', 'estão', 'você', 'tinha', 'foram', 'essa', 'num', 'nem', 'suas', 'meu', 'às', 
'minha', 'têm', 'numa', 'pelos', 'elas', 'havia', 'seja', 'qual', 'será', 'nós', 'tenho', 'lhe', 'deles', 
'essas', 'esses', 'pelas', 'este', 'fosse', 'dele', 'tu', 'te', 'vocês', 'vos', 'lhes', 'meus', 'minhas', 
'teu', 'tua', 'teus', 'tuas', 'nosso', 'nossa', 'nossos', 'nossas', 'dela', 'delas', 'esta', 'estes', 'estas', 
'aquele', 'aquela', 'aqueles', 'aquelas', 'isto', 'aquilo', 'estou', 'está', 'estamos', 'estão', 'estive', 
'esteve', 'estivemos', 'estiveram', 'estava', 'estávamos', 'estavam', 'estivera', 'estivéramos', 'esteja', 
'estejamos', 'estejam', 'estivesse', 'estivéssemos', 'estivessem', 'estiver', 'estivermos', 'estiverem', 
'hei', 'há', 'havemos', 'hão', 'houve', 'houvemos', 'houveram', 'houvera', 'houvéramos', 'haja', 'hajamos', 
'hajam', 'houvesse', 'houvéssemos', 'houvessem', 'houver', 'houvermos', 'houverem', 'houverei', 'houverá', 
'houveremos', 'houverão', 'houveria', 'houveríamos', 'houveriam', 'sou', 'somos', 'são', 'era', 'éramos', 
'eram', 'fui', 'foi', 'fomos', 'foram', 'fora', 'fôramos', 'seja', 'sejamos', 'sejam', 'fosse', 'fôssemos', 
'fossem', 'for', 'formos', 'forem', 'serei', 'será', 'seremos', 'serão', 'seria', 'seríamos', 'seriam', 'tenho', 
'tem', 'temos', 'tém', 'tinha', 'tínhamos', 'tinham', 'tive', 'teve', 'tivemos', 'tiveram', 'tivera', 'tivéramos', 
'tenha', 'tenhamos', 'tenham', 'tivesse', 'tivéssemos', 'tivessem', 'tiver', 'tivermos', 'tiverem', 'terei', 'terá', 
'teremos', 'terão', 'teria', 'teríamos', 'teriam']
    return palavras

#função que realiza a limpa do texto e retorna uma lista com um texto útil
def limpandoTexto(texto):
    texto2=[]
    texto=texto.lower().split()
    palavras_a_retirar=stopWords()
    for i in range(len(texto)):
        if texto[i] not in palavras_a_retirar:
            for letra in texto[i]:
                if letra.isalpha() == False:
                    texto[i]=texto[i].replace(letra, '')
            texto2.append(texto[i])
    return texto2

#função que cria o índice invertido e retorna o dicionario
def criacaoIndice(texto, nomeDoArquivo, dicionario):
    for i in range(len(texto)):
        contadora=texto.count(texto[i])
        if texto[i] in dicionario.keys():
            dicionario[texto[i]][nomeDoArquivo]=contadora #já realiza atualização do índice
        else:
            dicionario[texto[i]]={nomeDoArquivo: contadora}
    return dicionario

#função que faz remoção de tudo, do arquivo ou da pasta
def remocao(comando, enderecodoindice, endereco):
    remove=[]
    if comando == 'all':
        os.remove(r'{}'.format(enderecodoindice))
        print('Índice removido com sucesso! ')
    elif comando == 'folder':
        lista_arquivos = abrirDiretorio(endereco)
        lista_arquivos_salvos, dicionario = lerIndice(enderecodoindice)
        for i in range(len(lista_arquivos)):
            for item in dicionario.keys():
                if lista_arquivos[i] in dicionario[item].keys():
                    dicionario[item].pop(lista_arquivos[i])
                    if dicionario[item] == {}:
                        remove.append(item)
            if lista_arquivos[i] in lista_arquivos_salvos:
                lista_arquivos_salvos.remove(lista_arquivos[i])
        for k in remove:
            del dicionario[k]
        print('Itens da pasta removidos do índice com sucesso!')
        return lista_arquivos_salvos, dicionario
    elif comando == 'file':
        lista_arquivos_salvos, dicionario = lerIndice(enderecodoindice)
        nomeArquivo = endereco.split('\\')[-1]
        for item in dicionario.keys():
            if nomeArquivo in dicionario[item].keys():
                dicionario[item].pop(nomeArquivo)
                if dicionario[item] == {}:
                    remove.append(item)
        for k in remove:
            del dicionario[k]
        if nomeArquivo in lista_arquivos_salvos:
            lista_arquivos_salvos.remove(nomeArquivo)
        print('Arquivo removido do índice com sucesso!')
        return lista_arquivos_salvos, dicionario

#função que atualiza a lista de arquivos do indice de acordo com a lista do diretório
def updateListaArquivos(listaDeArquivos, lista_arquivos_salvos):
    for i in range(len(listaDeArquivos)):
        if listaDeArquivos[i] not in lista_arquivos_salvos:
            lista_arquivos_salvos.append(listaDeArquivos[i])
    return lista_arquivos_salvos

#impresssão ordenada do dicionário
def impressaoArquivosBusca(dicDaPalavra):
    try:
        for i in sorted(dicDaPalavra, key = dicDaPalavra.get, reverse=True):
            print(f'{dicDaPalavra[i]} - {i}')
    except AttributeError:
        print('Palavra não encontrada no índice.')

def ajuda():
    print('''
****PARA FAZER A LEITURA DOS ARQUIVOS DE UMA PASTA E ADICIONAR NO ÍNDICE:****
obs: caso o arquivo já esteja no índice, ele será atualizado.
obs2: para o endereço ser válido, ele precisa estar completo até a pasta a ser lida.
obs3: o comando faz a leitura dos arquivos que estão em uma pasta e não de um arquivo.
Comando: python HealthSearch.py read <endereço da pasta>

****PARA REMOVER O ÍNDICE, UM DIRETÓRIO OU UM ARQUIVO DO ÍNDICE:****
obs: se a remoção for de uma pasta, o endereço deve ser da pasta.
obs2: se a remoção for de um arquivo, o endereço deve ser do arquivo.
obs3: se a remoção for de todo o índice, não deve-se adicionar endereço.
Comando: python HealthSearch.py remove index <all/folder/file> <endereço da pasta ou do arquivo>

****PARA FAZER A BUSCA DE UMA PALAVRA:****
Comando: python HealthSearch.py search <palavra>

****PARA VER O ÍNDICE COMPLETO:****
obs: se não houver nenhum elemento no índice, não será impresso nenhum valor.
Comando: python HealthSearch.py see index

****PARA CONSEGUIR AJUDA:****
Comando: python HealthSearch.py help''')

#MAINNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
def main():
    enderecodoindice=os.getcwd()+'\\indiceInvertido.txt'
    dicionario={}
    comando = objetivo() #retorna a função de execução

    #LER DIRETÓRIO E SALVAR NO ÍNDICE
    try:
        if comando[0] == 'read': #ler todos os textos de um diretório e incrementa no índice, se já existir um arquivo igual salvo no diretorio, é feito atualização
            
                listaDeArquivos = abrirDiretorio(comando[1]) #retorna uma lista com todos os arquivos de um diretório
                for item in listaDeArquivos:
                    texto = abrirArquivo(item) #retorna o texto do arquivo
                    texto = limpandoTexto(texto) #retorna o texto util
                    lista_arquivos_salvos, dicionario = lerIndice(enderecodoindice) #retorna a lista de arquivos e o dicionario do indice atual
                    lista_arquivos_salvos = updateListaArquivos(listaDeArquivos, lista_arquivos_salvos)
                    dicionario = criacaoIndice(texto, item, dicionario) #cria todos os índices da lista de arquivos
                    salvarIndice(dicionario, lista_arquivos_salvos, enderecodoindice) #atualiza o indice com os dados adicionados
                if len(listaDeArquivos) > 0:
                    print('Todos os arquivos foram lidos e adicionados ao índice.')
                else:
                    print('Por não ter nenhum documento .txt nessa pasta, nenhum documento foi adicionado ao índice.')
        
        #REMOVER O ÍNDICE, A PASTA OU O ARQUIVO
        elif comando[0] == 'remove' and comando[1] == 'index': #remove index all/folder/file endereço
                if comando[2] == "all":
                    remocao(comando[2], enderecodoindice, 0)
                else:
                    lista_arquivos_salvos, dicionario = remocao(comando[2], enderecodoindice, comando[3])
                    salvarIndice(dicionario, lista_arquivos_salvos, enderecodoindice)
        
        #BUSCAR POR PALAVRA DENTRO DO ÍNDICE E IMPRIMIR EM ORDEM DECRESCENTE
        elif comando[0] == 'search': #comando[1] = palavra a ser buscada
            try:
                busca = comando[1]
                lista_arquivos_salvos, dicionario = lerIndice(enderecodoindice)
                dicDaPalavra = buscaIndice(dicionario, busca)
                impressaoArquivosBusca(dicDaPalavra)
            except:
                print('''Não foi possível realizar essa execução. 
Verifique se o índice existe. Caso não, faça a leitura do diretório com o comando "read".
Caso precise de mais ajuda: python HealthSearch.py help''')
        
        #VER O ÍNDICE INVERTIDO
        elif comando[0] == 'see' and comando[1] == 'index':
            try:
                lista_arquivos_salvos, dicionario = lerIndice(enderecodoindice)
                for item in dicionario.keys():
                    print(f'{item}: {dicionario[item]}')
            except:
                print('''Não foi possível realizar essa execução. 
Verifique se o índice existe. Caso não, faça a leitura do diretório com o comando "read".
Caso precise de mais ajuda: python HealthSearch.py help''')

        #CONSEGUIR AJUDA
        elif comando[0] == 'help':
            ajuda()

        else:
            ajuda()
            
    except FileNotFoundError:
        print('Endereço inválido ou não existe esse diretório na pasta selecionada.\nVerifique se o endereço foi escrito corretamente.\nCaso precise de mais ajuda: python HealthSearch.py help')

    
'''try:
    main()
except:
    ajuda()'''
main()
