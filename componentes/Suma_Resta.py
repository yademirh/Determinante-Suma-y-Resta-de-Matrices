
from customtkinter import *
import numpy as np
from validaciones.Errors import Errors

class Suma_Resta:

    Matriz : list[CTkEntry] = []
    row : int
    column : int
    count=0
    count_f=0
    band = True

    @staticmethod
    def recibe_entrys(entry: CTkEntry):
        Suma_Resta.Matriz.append(entry) 

    @staticmethod
    def calculate_oper(sum:bool):
        matriz_1 = []
        matriz_2 = []
        count = 0
        try:
            for i in range(Suma_Resta.row):
                matriz_1.append([])
                for j in range(Suma_Resta.column):
                    # value_without_space = Determinante.Matriz[count].get().replace(" ","")
                    value = eval(Suma_Resta.Matriz[count].get())
                    matriz_1[i].append(float(value))
                    count+=1

            for i in range(Suma_Resta.row):
                matriz_2.append([])
                for j in range(Suma_Resta.column):
                    # value_without_space = Determinante.Matriz[count].get().replace(" ","")
                    value = eval(Suma_Resta.Matriz[count].get())
                    matriz_2[i].append(float(value))
                    count+=1                
            matriz_np_1 = np.array(matriz_1)   
            matriz_np_2 = np.array(matriz_2)   

            return matriz_1 + matriz_2

            # return [True, f"{round(np.linalg.(matriz_np_1),4):.4f}"]
        
        except:
            return [False]
            
        pass           