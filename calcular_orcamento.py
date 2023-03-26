"""Um freelancer está com dificuldade para calcular qual valor cobrar por um projeto que está estimado em 80 horas. 
Após pensar e revisitar o preço de alguns projetos que cobrou no passado, ele montou a seguinte fórmula: 
valor inicial + quantidade de horas estimadas * valor da hora + 15% do valor calculado. Crie um programa que faça essa conta para o freelancer. 
Considere que o valor inicial sempre será R$ 1000,00 e o valor da hora cobrada é de R$ 20,45. A aplicação deve imprimir o valor calculado pelo 
projeto considerando duas casas decimais na formatação do valor. Dica: Preste atenção na ordem que as operações da fórmula devem ser realizadas

Dica bônus: você já tem algumas informações relevantes, como:
horas = 80
valor inicial = 1000.00
valor da hora = 20.45
taxa = 0.15 que representa os 15 porcento.

Sabendo disso, basta você declarar essas variáveis com seus respectivos valores no código e depois aplicar a fórmula citada no paragrafo anterior. 
Ah, não se esqueça de printar o resultado com duas casas decimais, para isso você pode utilizar .2f, por exemplo, print(f'{valor_total:.2f}').

Boa sorte!

"""

# valor_incial = 1000.00 reais
# horas_estimadas = 80 horas
# valor_hora = 20.45 reais
# taxa = 15% (100 * 0.15)

horas_estimadas = 80 
valor_inicial = 1000.00
valor_hora = 20.45
taxa = 1.15

valor_total = (valor_inicial + horas_estimadas * valor_hora) * taxa

print(f'{valor_total:.2f}')