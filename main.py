from Data.dao_salle import DataSalle
from models.salle import Salle

dao=DataSalle()
dao.insert_salle(Salle("INF1", "Test","Classe", 40))
print(dao.get_salles())


from services.services_salle import  ServiceSalle
from models.salle import Salle

s=ServiceSalle()
print(s.ajouter_salle(Salle("INF2","Info","Lab",35)))