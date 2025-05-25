from datetime import datetime

digito = -1 

tempoDetrabalho = datetime.now() - datetime.now()

print ('As datas inseridas nesse programa devem ser no formato dd/mm/yyyy \n')

strNasc = input('Digite a data de nascimento:\n')
dataNasc = datetime.strptime(strNasc, '%d/%m/%Y')

strAdmissao = input('\nDigite a data de > admissão <:\n')
entrada = datetime.strptime(strAdmissao, '%d/%m/%Y')

while entrada < dataNasc: 

    print ('\nInsira uma data valida para sua admissão! \n Não é possível ter começado a trabalhar antes de nascer\n')

    strAdmissao = input('\nDigite a data de > admissão <:\n')
    entrada = datetime.strptime(strAdmissao, '%d/%m/%Y')


strDemissao = input('\nDigite a data de > demissão <:\n')
saida = datetime.strptime(strDemissao, '%d/%m/%Y')


while saida < entrada: 
 
    print ('\nInsira uma data valida para sua demissão! \n Não é possível ter começado a trabalhar antes de nascer\n')

    strDemissao = input('\nDigite a data de > demissão <:\n')
    saida = datetime.strptime(strDemissao, '%d/%m/%Y')

tempoDetrabalho += (saida-entrada)

while digito != 0:

    digito2 = str (input ('\nDeseja adicionar mais algum vínculo empregatício? [S]/[N]\n').strip().lower())

    if digito2 == 's':
        
    

        strAdmissao = input('\nDigite a data de > admissão <:\n')
        entrada = datetime.strptime(strAdmissao, '%d/%m/%Y')

        while entrada < dataNasc: 

            print ('\nInsira uma data valida para sua admissão! \n Não é possível ter começado a trabalhar antes de nascer\n')

            strAdmissao = input('\nDigite sua data de > admissão <:\n')
            entrada = datetime.strptime(strAdmissao, '%d/%m/%Y')

        strDemissao = input('\nDigite sua data de > demissão <:\n')
        saida = datetime.strptime(strDemissao, '%d/%m/%Y')


        while saida < entrada: 
        
            print ('\nInsira uma data valida para sua demissão! \n Não é possível ter saido do emprego antes de ter começado a trabalhar\n')

            strDemissao = input('\nDigite sua data de > demissão <:\n')
            saida = datetime.strptime(strDemissao, '%d/%m/%Y')


        tempoDetrabalho += (saida-entrada)
    
    elif digito2 == 'n':
        break

    else:
        print ('Entrada inválida! Digite \'s\' ou \'n\'')

print ('\nTempo de trabalho: {} dias'.format (tempoDetrabalho.days))