import fila as queue

fila = [] 

qtdClientes = 0

digito = -1 

def limparTela ():
    print ('\n' * 100)

    return  

def menu (): 

    print('Menu \n')

    print('[1] Para incluir cliente na fila')

    print('[2] Para listar pessoas na fila')

    print('[3] Para atender o próximo cliente')

    print('[0] Para sair do programa\n')


    digito = int (input('Digite a opção desejada:\n'))

    return digito

    
    
while digito!=0:
    
    limparTela ()

    digito = menu ()

    while digito < 0 or digito > 3 : 

        limparTela ()

        print ('\nEntrada Inválida, insira apenas valores entre 0 e 3.\n')

        digito = menu ()

        limparTela ()

    if digito == 1: 

        limparTela ()

        print (' Inclusão de clientes \n')

        queue.incluirCliente (fila, qtdClientes )

        limparTela ()
    
    elif digito == 2: 

        limparTela ()

        print (' Lista de clientes \n')

        if not (queue.isEmpty (fila)):
            
            queue.listarClientes (fila)

            limparTela ()
        
        else:

            print('\nFila vazia!\n')

            input('Aperte enter para retornar ao menu\n')

    elif digito == 3:

        limparTela ()

        print (' Atendimento \n')

        if not(queue.isEmpty(fila)):

            queue.atenderCliente (fila)

            limparTela ()

        else:

            print('\nFila vazia!\n')

            input('Aperte enter para retornar ao menu\n')
        
print('\nPrograma encerrado.')