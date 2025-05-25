def isEmpty (fila):

    if len(fila) > 0:
        return False

    else:
        return True


def incluirCliente (fila, qtdClientes):

    qtdClientes = qtdClientes + 1

    nome = input('\nEscreva o nome do cliente: ')

    rg = input('Escreva o RG do cliente: ')

    cliente = {

        'nome': nome,

        'rg': rg

    }

    fila.append(cliente)

    return


def listarClientes (fila):

    for indice in range(0, len(fila)):

        print ('({} - {} - {})'.format (indice + 1, fila[indice]['rg'], fila[indice]['nome']))

    input('Aperte enter para voltar ao menu\n')

    return


def atenderCliente (fila):

    cliente = fila.pop(0)

    print ('Atendendo o cliente: {} - RG:{}\n'.format (cliente['nome'], cliente['rg']))

    print ('Sobraram {} clientes na fila.\n'.format (len(fila)))

    input('Aperte enter para voltar ao menu\n')

    return