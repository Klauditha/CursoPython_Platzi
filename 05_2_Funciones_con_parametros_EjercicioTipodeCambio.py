# -*- coding: utf-8 -*-
def foreign_change_calculator(ammount):
    mex_to_col_rate = 145.97
    return mex_to_col_rate * ammount

def run():
    print('CALCULADORA DE DIVISAS')
    print('Convierte pesos mexicanos a colombianos')
    print('')

    ammount = float(input('Ingresa la cantidad de epsos mexicanos que quieres convertir'))


    result = foreign_change_calculator(ammount)
    print(' ${} pesos mexicanos son ${} pesos colombianos', format(ammount, result))

if __name__ == ' __main__':
    run()
