from customtkinter import *


class Errors:

    label_1: CTkLabel
    label_2: CTkLabel
    msg_error: str = ""
    hide_1: bool = True
    hide_2: bool = True

    # Recibe label donde mostrar error en frame determinante
    @staticmethod
    def defineroot_det(Label):
        Errors.label_1 = Label

    # Recibe label donde mostrar error en frame suma/resta
    @staticmethod
    def defineroot_oper(Label):
        Errors.label_2 = Label

    # Mostrar label error en frame determinante
    @staticmethod
    def show_label_det():
        if Errors.hide_1:
            Errors.label_1.configure(text=Errors.msg_error)
            Errors.label_1.pack(pady=20)
            Errors.hide_1 = False
        else:
            Errors.hide_label_det()
            Errors.show_label_det()
            Errors.hide_1 = True

    # Ocular label error en frame determinante
    @staticmethod
    def hide_label_det():
        if not Errors.hide_1:
            Errors.label_1.pack_forget()
            Errors.hide_1 = True

    # Mostrar label error en frame suma/resta
    @staticmethod
    def show_label_oper():
        if Errors.hide_2:
            Errors.label_2.configure(text=Errors.msg_error)
            Errors.label_2.pack(pady=20)
            Errors.hide_2 = False
        else:
            Errors.hide_label_oper()
            Errors.show_label_oper()
            Errors.hide_2 = True
    
    # Ocultar label error en frame suma/resta
    @staticmethod
    def hide_label_oper():
        if not Errors.hide_2:            
            Errors.label_2.pack_forget()
            Errors.hide_2 = True
