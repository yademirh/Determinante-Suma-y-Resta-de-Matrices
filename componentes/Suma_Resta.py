
from customtkinter import *
import numpy as np
from validaciones.Errors import Errors

class Suma_Resta:

    Matriz : list[CTkEntry] = []
    row : int
    column : int
    band : bool

    @staticmethod
    def recibe_entrys(entry: CTkEntry):
        Suma_Resta.Matriz.append(entry) 

    @staticmethod
    def calculate_oper():
        matriz_1 = []
        matriz_2 = []
        count = 0
        try:
            for i in range(Suma_Resta.row):
                matriz_1.append([])
                for j in range(Suma_Resta.column):
                    value_without_space = Suma_Resta.Matriz[count].get().replace(" ","")
                    value = eval(value_without_space)
                    matriz_1[i].append(float(value))
                    count+=1

            for i in range(Suma_Resta.row):
                matriz_2.append([])
                for j in range(Suma_Resta.column):
                    value_without_space = Suma_Resta.Matriz[count].get().replace(" ","")
                    value = eval(value_without_space)
                    matriz_2[i].append(float(value))
                    count+=1                
            matriz_np_1 = np.array(matriz_1)   
            matriz_np_2 = np.array(matriz_2)   

            if Suma_Resta.band:
                
                return [True, matriz_np_1 + matriz_np_2]
            else:
                
                return [True, matriz_np_1 - matriz_np_2]
               
        except ZeroDivisionError:
            Errors.msg_error = "División por cero"
            return [False, []]
        except IndexError:
            Errors.msg_error = "Campo(s) nulo"
            return [False, []]
        except KeyError:
            Errors.msg_error = "Campo(s) nulo"
            return [False, []]
        except AttributeError:
            Errors.msg_error = "Campo(s) nulo"
            return [False, []]
        except ArithmeticError:
            Errors.msg_error = "Operación no válida o posible división por cero"
            return [False, []]
        except ValueError:
            Errors.msg_error = "Campo(s) nulo"
            return [False, []]
        except TypeError:
            Errors.msg_error = "Operación no válida"
            return [False, []]
        except SyntaxError:
            Errors.msg_error = "Operación no válida"
            return [False, []]
        except Exception as e:
            Errors.msg_error = e
            return [False, []]