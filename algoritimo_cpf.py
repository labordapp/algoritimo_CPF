from pathlib import Path
algoritmo_cpf = Path(__file__)
print (algoritmo_cpf.absolute())

 #------------------------------ Início do código ------------------------------#   
print()
print()

while True: # loop principal, do início ao fim do código
    cpf = (input("Digite o seu CPF sem pontos, espaços ou hífen: ")[0:11])
    if (cpf == "11111111111" or cpf == "22222222222" or cpf == "33333333333" or cpf == "44444444444" or
            cpf == "55555555555" or cpf == "66666666666" or cpf == "77777777777" or cpf == "88888888888" or
            cpf == "99999999999" or cpf == "00000000000"):
        print ()
        print (f"O CPF {cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]} é >>> INVÁLIDO <<< !!!")
        print ()
        break # retorna ao loop secundário
    
    
    #----------------- Início do Cálculo do 1º dígito verificador -----------------#
    priMultiplica = int(cpf[0]) * 10
    segMultiplica =  int(cpf[1]) * 9
    terMultiplica = int(cpf[2]) * 8 
    quaMultiplica =  int(cpf[3]) * 7
    quiMultiplica =  int(cpf[4]) * 6
    sexMultiplica = int(cpf[5]) * 5
    setMultiplica =  int(cpf[6]) * 4
    oitMultiplica =  int(cpf[7]) * 3
    nonMultiplica =  int(cpf[8]) * 2

    somaUm = (priMultiplica + segMultiplica + terMultiplica + quaMultiplica + quiMultiplica
        + sexMultiplica + setMultiplica + oitMultiplica + nonMultiplica)

    divisaoUm = int(somaUm / 11)
    restoDaDivisao = somaUm%11

    if restoDaDivisao == 0 or restoDaDivisao == 1:
        dvUm = 0
    else:
        dvUm = 11 - restoDaDivisao 

    #     #-----------------Fim do cálculo do 1º dígito verificador --------------------#

    #     #-----------------Início do cálculo do 2º dígito verificador -----------------#
    priMultiplicaS = int(cpf[0]) * 11
    segMultiplicaS = int(cpf[1]) * 10
    terMultiplicaS = int(cpf[2]) * 9
    quaMultiplicaS = int(cpf[3]) * 8
    quiMultiplicaS = int(cpf[4]) * 7
    sexMultiplicaS = int(cpf[5]) * 6
    setMultiplicaS = int(cpf[6]) * 5
    oitMultiplicaS = int(cpf[7]) * 4
    nonMultiplicaS = int(cpf[8]) * 3
    decMultiplicaS = int(cpf[9]) * 2
    depMultiplicaS = int(cpf[10])

    somaDois = (priMultiplicaS + segMultiplicaS + terMultiplicaS + quaMultiplicaS + quiMultiplicaS
            + sexMultiplicaS + setMultiplicaS + oitMultiplicaS + nonMultiplicaS + decMultiplicaS)

    divisaoDois = int(somaDois / 11)
    restoDaDivisaoDois = somaDois%11

    if restoDaDivisaoDois == 0 or restoDaDivisaoDois == 1:
            dvDois = 0
    else:
            dvDois = 11 - restoDaDivisaoDois
    #-----------------Fim do cálculo do 2º dígito verificador -----------------#

    #----------- Início da validação dos dois dígitos verificadores -----------#
    if dvUm == int(cpf[9]) and dvDois == int(cpf[10]):
            print ()
            print (f"CPF {cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]} validado com sucesso!!! ")
            print ()
            print ()
            resposta = input("Digite S para validar outro CPF ou ENTER para finalizar o App: ").upper().strip()
            print()
            if resposta == "S": continue
            else: break # Retorna ao loop principal
    else:
            print ()
            print (f"O CPF {cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]} é >>> INVÁLIDO <<< !!!")
            print ()
        

        #----------- Final da validação dos dois dígitos verificadores ------------#

    #------------------------------- Fim do código --------------------------------#

