# Consumo mensal    Percetual de desconto
# <= 30             65%
# >= 30 && <= 100   40%
# > 100 && <= 220  10%
# > 220             0%
#Função:

# Função
# f(x)= {
  # 65% se x <= 30
  # 40% se 30 > x <= 100 
  # 10% se  100 >  x <= 220 
  # 0% se x > 200
# }

#PROGRAMA

#Declaração de variáveis


consumo = int(input("Informe o seu consumo desse mês "))
porcentagem = 0
#Variável responsável pela função
funcao = 0
desconto = 0

#Estrutura condicional para verificar se o consumo é valido
if consumo < 0:
    print("Valor inválido, insira um valor válido")
else:
      #Estrutura condicional para verificar o desconto do cliente
  if consumo <= 30:
      funcao = (65*consumo)/100
      print("Deu 65% de desconto, você terá "+ str(funcao) + " reais de desconto") 
  if consumo > 30 and consumo <= 100:
      funcao = (40*consumo)/100
      print("Deu 40% de desconto, você terá "+ str(funcao) + " reais de desconto")
  if consumo > 100 and consumo <= 200:
      funcao = (10*consumo)/100
      print("Deu 10% de desconto, você terá "+ str(funcao) + " reais de desconto")
  if consumo > 200:
      funcao = (0*consumo)/100
      print("Deu 0% de desconto, você terá "+ str(funcao) + " reais de desconto")
    
  #Resposta do programa
  desconto = funcao
  print(desconto)