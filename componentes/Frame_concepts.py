from customtkinter import *

class Frame_concepts:
    root : CTkFrame

    @staticmethod
    def defineroot(app):
        Frame_concepts.root = app

    @staticmethod
    def defineDeterminante():

        frame_def_det = CTkFrame(Frame_concepts.root, fg_color="azure3")
        frame_def_det.pack(fill="both", expand=1)
        Frame_concepts.root.pack_forget()
        