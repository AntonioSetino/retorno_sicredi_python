from dao import TituloDAO


def criar_arquivo_retorno_sicredi():
    titulo_dao = TituloDAO()
    lista_numero_documento = titulo_dao.listar_numero_documento_sicredi()
    cont = 0
    with open('arquivo/retorno_sicredi.crt', 'w') as arquivo:
        for numero_documento in lista_numero_documento:
            cont += 1
            arquivo.write('1            A294J4000002                      {}0                                                    091002200031754011                    1502190000000006900         A000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000                          0000000000                                                                  {}\n'.format(numero_documento[0], str(cont).zfill(6)))
    print 'Arquivo criado'


if __name__ == '__main__':
    criar_arquivo_retorno_sicredi()
