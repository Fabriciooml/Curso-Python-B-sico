from random import choice

def get_palavra():
  palavras = ["python", "sauron", "toalha", "gallifrey"]
  palavra = choice(palavras)
  return palavra

palavra_certa = get_palavra()
display = []
n_letras = len(palavra_certa)
tentativas = 0
letra = ''
letras_usadas = []

#print(palavra_certa)

for i in palavra_certa:
  display.append("_")

while n_letras != 0 and letra != "sair":
  print("".join(display))
  letra = input("Digite uma letra: ")
  
  if letra.lower() in letras_usadas:
    print("Essa letra já foi, tente outra!")
  
  else:
    for i in range(len(palavra_certa)):
      if letra.lower() == palavra_certa[i]:
        display[i] = letra.upper()
        n_letras -= 1
    tentativas += 1
  
  letras_usadas.append(letra.lower())

if letra == "sair":
  print("Eita, tá bom, tchau!")
else:
  print("".join(display))
  print("Nice! Você acertou a palavra {} depois de {} tentativas!"
        .format(palavra_certa, tentativas))