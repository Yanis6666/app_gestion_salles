import customtkinter as ctk
from services.services_salle import ServiceSalle
from models.salle import Salle

class ViewSalle(ctk.CTk) :

    def __init__(self):
        super().__init__()

        self.title("Gestion des salles")
        self.geometry("600x500")

        self.service_salle = ServiceSalle()


        self.frame_info = ctk.CTkFrame(self)
        self.frame_info.pack(pady=10)

        self.entry_code=ctk.CTkEntry(self.frame_info, placeholder_text="Code")
        self.entry_code.pack(pady=5)

        self.entry_desc= ctk.CTkEntry(self.frame_info,  placeholder_text="Description" )
        self.entry_desc.pack( pady=5)

        self.entry_cat=ctk.CTkEntry(self.frame_info,placeholder_text= "Catégorie" )
        self.entry_cat.pack(pady=5 )

        self.entry_cap=ctk.CTkEntry(self.frame_info, placeholder_text= "Capacité")
        self.entry_cap.pack(pady=5 )



        self.frame_btn=ctk.CTkFrame(self)
        self.frame_btn.pack(pady=10)

        self.btn_add=ctk.CTkButton(self.frame_btn, text= "Ajouter")
        self.btn_add.pack(side= "left",  padx=5)

        self.btn_mod=ctk.CTkButton(self.frame_btn, text= "Modifier")
        self.btn_mod.pack(side = "left", padx=5 )

        self.btn_del=ctk.CTkButton(self.frame_btn, text="Supprimer" )
        self.btn_del.pack(side="left", padx=5 )

        self.btn_search =ctk.CTkButton(self.frame_btn, text="Rechercher")
        self.btn_search.pack( side="left" , padx=5 )

        self.cadreList = ctk.CTkFrame(self)
        self.cadreList.pack(pady=10)

        self.treeList = ttk.Treeview(
            self.cadreList,
            columns=( "code", "description", "categorie", "capacite"),
            show= "headings"
        )
        self.treeList.heading( "code", text ="CODE")
        self.treeList.heading("description", text = "Description")
        self.treeList.heading("categorie", text="Catégorie" )
        self.treeList.heading("capacite" , text= "Capacité")

        self.treeList.pack(expand=True, fill="both", padx=10, pady=10)

        self.lister_salles()

    def lister_salles(self) :
        self.treeList.delete(*self.treeList.get_children())

        liste=self.service_salle.recuperer_salles()
        for s in liste:
            self.treeList.insert (
                "",
                "end",
                values=(s.code, s.description, s.categorie, s.capacite)
            )


    def ajouter_salle(self):
        salle=Salle(
            self.entry_code.get(),
            self.entry_desc.get(),
            self.entry_cat.get(),
            int(self.entry_cap.get())
        )
        self.service_salle.ajouter_salle(salle)
self.btn_add.configure(command=self.ajouter_salle)


    def modifier_salle(self) :
        salle=Salle(
            self.entry_code.get(),
            self.entry_desc.get(),
            self.entry_cat.get(),
            int(self.entry_cap.get())
        )
        self.service_salle.modifier_salle(salle)
self.btn_mod.configure(command=self.modifier_salle)


   def supprimer_salle(self) :
        code =self.entry_code.get()
        self.service_salle.supprimer_salle(code)
self.btn_del.configure(command=self.supprimer_salle)


    def rechercher_salle(self) :
        code=self.entry_code.get()
        salle =self.service_salle.rechercher_salle(code)
        if salle :
            self.entry_desc.delete(0, "end" )
            self.entry_desc.insert(0, salle.description)

            self.entry_cat.delete(0,"end" )
            self.entry_cat.insert( 0, salle.categorie)

            self.entry_cap.delete(0, "end" )
            self.entry_cap.insert(0, salle.capacite)
self.btn_search.configure ( command=self.rechercher_salle )

from tkinter import ttk
