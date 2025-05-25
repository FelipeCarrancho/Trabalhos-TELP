from datetime import datetime

digito = -1 

genero = 'none' 

tempoDeServico = datetime.now() - datetime.now()

print ('Todas as datas inseridas nesse programa devem ser no formato dd/mm/yyyy \n')

genero = (str (input ('Informe seu gênero: [F] - feminino ou [M] - masculino \n'))).strip().lower()

while genero != 'f' and genero != 'm': 

    print ('Entrada inválida! \n Tente Digitar \'f\' ou \'m\'\n')

    genero = (str (input ('Informe seu gênero: [F] ou [M]\n'))).strip().lower()

strNasc = input('\nDigite sua data de nascimento:\n')
dataNasc = datetime.strptime(strNasc, '%d/%m/%Y')
idade = datetime.now() - dataNasc


strAdmissao = input('\nDigite sua data de admissão:\n')
entrada = datetime.strptime(strAdmissao, '%d/%m/%Y')

while entrada < dataNasc: 

    print ('\nNão é possível ter começado a trabalhar antes de nascer, insira uma data valida para sua admissão!\n')

    strAdmissao = input('\nDigite sua data de admissão:\n')
    entrada = datetime.strptime(strAdmissao, '%d/%m/%Y')


strDemissao = input('\nDigite sua data de demissão:\n')
saida = datetime.strptime(strDemissao, '%d/%m/%Y')


while saida < entrada: 
    print ('\nNão é possível ter saido do emprego antes de ter começado a trabalhar, insira uma data valida para sua demissão!\n')

    strDemissao = input('\nDigite sua data de demissão:\n')
    saida = datetime.strptime(strDemissao, '%d/%m/%Y')


tempoDeServico += (saida-entrada)


while digito != 0:

    digito2 = str (input ('\nDeseja adicionar mais algum vínculo empregatício? \n[S]/[N]\n').strip().lower())

    if digito2 == 's':

        strAdmissao = input('\nDigite sua data de admissão:\n')
        entrada = datetime.strptime(strAdmissao, '%d/%m/%Y')

        while entrada < dataNasc:

            print ('\nNão é possível ter começado a trabalhar antes de nascer, insira uma data valida para sua admissão!\n')

            strAdmissao = input('\nDigite sua data de admissão:\n')
            entrada = datetime.strptime(strAdmissao, '%d/%m/%Y')

        strDemissao = input('\nDigite sua data de demissão:\n')
        saida = datetime.strptime(strDemissao, '%d/%m/%Y')


        while saida < entrada: 
        
            print ('\nNão é possível ter saido do emprego antes de ter começado a trabalhar, insira uma data valida para sua demissão!\n')

            strDemissao = input('\nDigite sua data de demissão:\n')
            saida = datetime.strptime(strDemissao, '%d/%m/%Y')


        tempoDeServico += (saida-entrada)
    
    elif digito2 == 'n':
        break

    else:
        print ('Entrada inválida! \n Tente Digitar \'s\' ou \'n\'')

print ('Tempo de serviço: %d anos\n'%(tempoDeServico.days/365))

if genero =='f':

    print ('Faltam %d anos de serviço para se aposentar'%((30 - (tempoDeServico.days/365))))
    
    if (idade.days/365) < 62:

        print ('E faltam %d anos para se aposentar\n'%((62 - (idade.days/365))))

if genero =='m':

    print ('Faltam %d anos de serviço para se aposentar'%((35 - (tempoDeServico.days/365))))

    if (idade.days/365) < 65:
        print ('E faltam %d anos para se aposentar\n'%((65 - (idade.days/365))))