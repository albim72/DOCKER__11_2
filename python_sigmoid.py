import numpy as np

def sigmoid(x):
    return 1/(1+np.exp(-x))

if __name__ == '__main__':
    x = float(input("Podaj wartość argunemtu x funkcji sigmoid: "))
    print(f"wartość funkcji sigmoid dla x = {x} wynosi {sigmoid(x):.16f}")
