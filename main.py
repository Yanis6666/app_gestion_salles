from Data.dao_salle import DataSalle
from models.salle import Salle

dao =DataSalle()
s= Salle("INF1", "Salle test", "Classe", 40)
dao.insert_salle(s)

print(dao.get_salles())