import sys
import os
from services.service_salle import ServiceSalle

import services.service_salle
print("FILE USED:", services.service_salle.__file__)
print("METHODS:", dir(ServiceSalle))


from Data.dao_salle import DataSalle
from models.salle import Salle

dao=DataSalle()
dao.insert_salle(Salle("S1", "Test","Classe", 40))
print(dao.get_salles())

s=ServiceSalle()
print(s.ajouter_salle(Salle("S2","Info","Lab",35)))



from views.view_salle  import ViewSalle

app=ViewSalle()
app.mainloop()


