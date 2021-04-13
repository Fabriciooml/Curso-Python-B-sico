class Pessoa():
  def __init__(self, nome) -> None:
    self.__nome = nome
  
  def __str__(self) -> str:
      return "nome: " + self.__nome
