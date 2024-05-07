from customtkinter import *
import numpy as np
from validaciones.Errors import Errors


class Determinante:

    Matriz: list[CTkEntry] = []
    row: int
    column: int

    # Recibir cada entry que se genera
    @staticmethod
    def recibe_entrys(entry: CTkEntry):
        Determinante.Matriz.append(entry)

    # Sacar el numero de cada entry, validarlo y retornar el resultado
    @staticmethod
    def calculate_det():
        matriz_values = []
        count = 0
        try:
            for i in range(Determinante.row):
                matriz_values.append([])
                for j in range(Determinante.column):
                    value_without_space = (
                        Determinante.Matriz[count].get().replace(" ", "")
                    )
                    value = eval(value_without_space)
                    matriz_values[i].append(float(value))
                    count += 1

            matriz_np = np.array(matriz_values)
            return [True, f"{round(np.linalg.det(matriz_np),4):.4f}"]

        except ZeroDivisionError:
            Errors.msg_error = "División por cero"
            return [False]
        except IndexError:
            Errors.msg_error = "Campo(s) nulo"
            return [False]
        except KeyError:
            Errors.msg_error = "Campo(s) nulo"
            return [False]
        except AttributeError:
            Errors.msg_error = "Campo(s) nulo"
            return [False]
        except ArithmeticError:
            Errors.msg_error = "Operación no válida o posible división por cero"
            return [False]
        except ValueError:
            Errors.msg_error = "Campo(s) nulo"
            return [False]
        except TypeError:
            Errors.msg_error = "Operación no válida"
            return [False]
        except SyntaxError:
            Errors.msg_error = "Campo(s) nulo"
            return [False]
        except Exception as e:
            Errors.msg_error = "Por favor leer instrucciones"
            return [False]
