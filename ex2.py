entrada = float(input('Qual a distancia da viagem?'))

if entrada <= 200 :
    var1 = entrada * 0.50
if entrada >200:
    var1 = entrada * 0.45
        
print(f'o valor foi: R${var1}')