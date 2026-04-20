from Data.dao_salle import DataSalle

class ServiceSalle:

    def __init__(self):
        self.dao = DataSalle()

    def ajouter_salle(self, salle):
        if not salle.code or not salle.description or not salle.categorie:
            return False, "Champs obligatoires manquants"

        if salle.capacite < 1:
            return False, "Capacité invalide"

        self.dao.insert_salle(salle)
        return True, "Salle ajoutée"

    def modifier_salle(self, salle):
        if salle.capacite < 1:
            return False, "Capacité invalide"
        self.dao.update_salle(salle)
        return True, "Salle modifiée"

    def supprimer_salle(self, code):
        self.dao.delete_salle(code)

    def rechercher_salle(self, code):
        return self.dao.get_salle(code)

    def recuperer_salles(self):
        return self.dao.get_salles()

from Data.dao_salle import DataSalle
class ServiceSalle :
    def __init__(self):
        self.dao=DataSalle()


def ajouter_salle(self, salle):
    if not salle.code or not salle.description or not salle.categorie:
        return False, "Champs vides"
    if salle.capacite < 1:
        return False, "La capacité est invalide"
    self.dao.insert_salle(salle)
    return True, "L'ajout est réussi"


def modifier_salle(self, salle) :
    if salle.capacite < 1 :
        return False, "La capacité est invalide"

    self.dao.update_salle(salle)
    return True, "Modification OK"

def supprimer_salle(self, code) :
    self.dao.delete_salle(code)

def rechercher_salle(self, code):
    return self.dao.get_salle(code)
