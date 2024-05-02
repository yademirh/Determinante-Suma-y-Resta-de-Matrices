from customtkinter import *
from componentes.Determinante import Determinante
from componentes.Suma_Resta import Suma_Resta

class Matriz:

    root_1 : CTkFrame
    root_2 : CTkFrame
    frame : CTkFrame = None
    frame1 : CTkFrame = None
    frame2 : CTkFrame = None

    @staticmethod
    def defineRoot(frame_det:CTkFrame):
        Matriz.root_1 = frame_det

    @staticmethod
    def defineRoot_oper(frame_det:CTkFrame):
        Matriz.root_2 = frame_det
        
    @staticmethod
    def createMatriz(row, column):

        if Matriz.frame is not None:
            Matriz.frame.destroy()

        Matriz.frame = CTkFrame(master=Matriz.root_1)

        for i in range(row):
            for j in range(column):
                entry = CTkEntry(master=Matriz.frame, width=40, height=35, justify="center", font=("Arial", 16))
                entry.grid(column=j, row=i, padx=4, pady=4)
                Determinante.recibe_entrys(entry)
        Matriz.frame.pack()


    @staticmethod
    def createMatriz_oper(row:int, column:int):        
        
        if Matriz.frame1 is not None:
            Matriz.frame1.destroy()
        if Matriz.frame2 is not None:
            Matriz.frame2.destroy()

        Matriz.frame1 = CTkFrame(master=Matriz.root_2)
        Matriz.frame2 = CTkFrame(master=Matriz.root_2)
        
        for i in range(row):
            for j in range(column):                
                entry = CTkEntry(master=Matriz.frame1, width=35, height=30, justify="center", font=("Arial", 14))
                entry.grid(column=j, row=i, padx=4, pady=4)
                Suma_Resta.recibe_entrys(entry)

        for i in range(row):
            for j in range(column):                
                entry = CTkEntry(master=Matriz.frame2, width=35, height=30, justify="center", font=("Arial", 14))
                entry.grid(column=j, row=i, padx=4, pady=4)
                Suma_Resta.recibe_entrys(entry)

        Matriz.frame1.grid(row=0, column=0, padx=40)
        Matriz.frame2.grid(row=0, column=1) 

    @staticmethod
    def show_matriz_sol(frame_sol:CTkFrame, row:int, col:int, rta_matriz:list ):
        # for i in range(row):
        #     for j in range(col):
        #         label = CTkLabel(frame_sol, text=rta_matriz[i][j], width=35, height=30, font=("Arial", 14))
        #         label.grid(column=j, row=i, padx=4, pady=4)
        print("mostrando matriz")
        pass
        