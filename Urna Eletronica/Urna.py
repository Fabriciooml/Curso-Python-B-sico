from Candidato import Candidato
class Urna():
  __votos = dict()
  def __init__(self) -> None:
      pass
  
  def votar(self, voto) -> None:
    if voto in self.__votos.keys():
      self.__votos[voto] += 1
    else:
      self.__votos[voto] = 1
   
  
  def __str__(self) -> str:
    resultado_votacao = sorted(self.__votos.items(), 
                               key=lambda x: x[1],
                               reverse=True)
    numero_vencedor = resultado_votacao[0][0]
    string = "Vencedor: " \
      + Candidato.nome_pelo_numero(Candidato, numero_vencedor)
    
    return string