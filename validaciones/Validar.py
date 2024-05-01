from customtkinter import *

class Validar:

    label : CTkLabel
    entrys = list() 
    row : int
    column : int

    def defineroot(Label):
        Validar.label = Label

    @staticmethod
    def recibe_row_column(row,column):
        Validar.row = row
        Validar.column = column

    @staticmethod
    def hola():
        Validar.label.pack(ipady=5, ipadx=5)

    @staticmethod
    def recibe_entrys(entry: CTkEntry):
        Validar.entrys.append(entry)

    @staticmethod
    def validar_entrys():
        for num in Validar.entrys:

            pass