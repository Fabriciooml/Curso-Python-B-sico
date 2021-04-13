from Pessoa import Pessoa
from Candidato import Candidato
from Urna import Urna

class Eleitor(Pessoa):
  def __init__(self, nome, voto) -> None:
    super().__init__(nome)
    self.__voto = voto
    Urna.votar(Urna, voto)
  
  def __str__(self) -> str:
    string = Pessoa.__str__(self) \
    + "\nCandidato: " + Candidato.nome_pelo_numero(Candidato, self.__voto)
    return string