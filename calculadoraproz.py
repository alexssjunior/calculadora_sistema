def calculadora (num1, num2, operacao):
    if operacao == 1 :
        return num1 + num2
    elif operacao == 2:
        return num1 * num2
    elif operacao == 3:
        return num1 - num2
    elif operacao == 4:
        if num2 != 0:
            return num1 / num2
        else:
            return "erro: divisao por zero"
    else:
        return 0
    
    print(calculadora(10, 5, 1))  # Soma: retorna 15
print(calculadora(10, 5, 2))  # Multiplicação: retorna 50
print(calculadora(10, 5, 3))  # Subtração: retorna 5
print(calculadora(10, 0, 4))  # Divisão por zero: retorna "Erro: divisão por zero"