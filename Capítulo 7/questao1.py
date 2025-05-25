class processo():
    def _init_(self, idd, desc):
        self.idd = idd
        self.desc = desc

def limparTela():
    print("\n"*100)

    return

id = 0
desc = ""
iden = 0
digito = 1
processos = []

def menu():
    print("Menu\n")

    print("[1] Adicionar Processo")
    print("[2] Remover Processo")
    print("[3] Encerrar \n")

    digito = int(input("Digite a opção: \n"))

    return digito

while True:

    limparTela()

    digito = menu()

    while digito < 0 or digito > 3:

        limparTela()

        print("\nEntrada Inválida, Tente Novamente")

        digito = menu()

        limparTela()

    if digito == 1:

        limparTela()

        id = int(input("Digite o id do processo: \n"))
        desc = str(input("Digite a descrição do processo: \n"))

        processos.insert(0, processo(id, desc))

        print("\n"*3)

        for i in range(0, len(processos)):
            print(f"Processo {processos[i].idd}")

        input("\nTecle enter para retornar ao menu ")

    if digito == 2:

        limparTela()

        if ((len(processos)) == 0):
            print("\nLista vazia!")
        else:
            iden = int(input(" Digite o id do processo que voce deseja remover.\n Id: "))

            for i in range(len(processos)):
                if (((processos[i]).idd) == iden):
                    print(f"Removido o processo {processos[i].idd} — Descrição: {processos[i].desc}")
                    processos.pop(i)
                else:
                    print("\nProcesso não encontrado!")

                print("\n"*3)

                for i in range(0, len(processos)):
                    print(f"Processo {processos[i].idd}")

    if digito == 3:
        processos.clear()
        break