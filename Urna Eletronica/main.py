from Candidato import Candidato
from Eleitor import Eleitor
from Urna import Urna

candidato1 = Candidato(nome="Ford Prefect", numero="42")
candidato2 = Candidato(nome="David Tennant", numero="10")
candidato3 = Candidato(nome="Sherlock Holmes", numero="221")

eleitor1 = Eleitor(nome="Marvin", voto="42")
eleitor2 = Eleitor(nome="Rose", voto="10")
eleitor3 = Eleitor(nome="Mycroft", voto="221")
eleitor4 = Eleitor(nome="John", voto="221")
eleitor5 = Eleitor(nome="Jack Harkness", voto="10")
eleitor6 = Eleitor(nome="Martha", voto="10")

print(Urna())