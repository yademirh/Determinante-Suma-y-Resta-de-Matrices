from customtkinter import *
import numpy as np
from validaciones.Errors import Errors

class Determinante:

    Matriz : list[CTkEntry] = []
    row : int
    column : int
    count=0
    count_f=0
    band = True

    @staticmethod
    def recibe_entrys(entry: CTkEntry):
        Determinante.Matriz.append(entry)

    @staticmethod
    def calculate_det():
        matriz_values = []
        count = 0
        try:
            for i in range(Determinante.row):
                matriz_values.append([])
                for j in range(Determinante.column):
                    value_without_space = Determinante.Matriz[count].get().replace(" ","")
                    value = eval(value_without_space)
                    matriz_values[i].append(float(value))
                    count+=1
            
            matriz_np = np.array(matriz_values)            
            return [True, f"{round(np.linalg.det(matriz_np),4):.4f}"]
        
        except ArithmeticError:
            Errors.msg_error = "XD"
            return [False]
        
        except EOFError:
            Errors.msg_error = "XD"
            return [False]

        except:
            Errors.msg_error = "General"
            return [False]
        

