from Pessoa import Pessoa

class Candidato(Pessoa):
  __candidatos = dict()
  def __init__(self, nome, numero) -> None:
    super().__init__(nome)
    self.__numero = numero
    self.__candidatos[numero] = nome
  
  def nome_pelo_numero(self, numero) -> str:
    return self.__candidatos[numero]
  
  def __str__(self) -> str:
    string = Pessoa.__str__(self) \
    + "\nNumero:" + self.__numero
    return string