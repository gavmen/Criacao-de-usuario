# Declaração Variáveis

x = input('Deseja criar um novo usuário? ')
listau = []
listasenha = []

# Declaração Funções


def novouser():

    usersx = input('Usuário = ')
    senhauser = input('Defina uma senha = ')

    listau.append(usersx)
    listasenha.append(senhauser)
    print(listau)

    outrouser()


def outrouser():
    outrouser = input('Deseja criar outro usuário ?: ')
    if outrouser == 'sim' or outrouser == 's':
        novouser()
    elif outrouser == 'nao' or outrouser == 'n':
        with open(r'Usuario.txt', 'a') as fp:
            for item in listau:
                fp.write("%s\n" % item)
        with open(r'senhas.txt', 'a') as fp:
            for item in listasenha:
                fp.write("%s\n" % item)
        novouserneg()
    else:
        simounao()


def novouserneg():
    x == 'nao' or x == 'n'
    print('Lista de Usuários: ', listau)


def simounao():
    print('responda apenas sim ou nao')


# Execeução

if x == 'sim' or x == 's':
    novouser()
elif x == 'n' or x == 'nao':
    novouserneg()
else:
    simounao()
