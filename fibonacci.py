def fibonacci(n):
   if n <= 1:
       return n
   else:
       return(fibonacci(n-1) + fibonacci(n-2))

numero_termos = 10

if numero_termos <= 0:
   print("O número de termos deve ser um inteiro positivo")
else:
   print("Fibonacci:")
   for i in range(numero_termos):
       print(fibonacci(i))