try:
    nomearquivo = input('Digite o nome que você deseja inserir no arquivo texto: ')
    while nomearquivo == '':
        nomearquivo = input('Digite um nome válido: ')

    arquivo = open(f'{nomearquivo}.html', 'w')

    titulo = input('Digite um título para a sua página Web: ')

    while titulo == '':
        titulo = input('Digite um título válido! ')

    arquivo.write(f'<center>{titulo}<br><br></center>')

    conteudo = input('Digite o conteúdo que você deseja escrever no arquivo texto: ')
    while conteudo == '':
        conteudo = input('Digite um contéudo válido para o arquivo texto: ')
    arquivo.write(conteudo)

    arquivo.close()
except Exception as erro:
    print(f'Ocorreu erro {erro}')
else:
    print('Arquivo aberto com Sucesso')
finally:
    print('Fim do programa')