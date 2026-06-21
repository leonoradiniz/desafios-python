import numpy as np

A = np.array([[60, 40], [50, 30]])
B = np.array([26, 20])

try:
    det = np.linalg.det(A)

    if np.abs(det) < 1e-10:
        print("Erro: A matriz A não é invertível (determinante zero).")

    else:
        X = np.linalg.solve(A, B)

        x = X[0]  
        y = X[1] 

        print("Quantidades de ingrediente X:")
        print(f"x = {x:.2f} unidades por litro de A")
        print(f"y = {y:.2f} unidades por litro de B")

        unidades_x = 70 * x + 50 * y
        print(f"\nUnidades de X em 70 litros de A e 50 litros de B: {unidades_x:.2f} unidades")

        print("\nVerificação:")
        print(f"60x + 40y = 60({x:.2f}) + 40({y:.2f}) = {60*x + 40*y:.2f}")
        print(f"50x + 30y = 50({x:.2f}) + 30({y:.2f}) = {50*x + 30*y:.2f}")

except np.linalg.LinAlgError:
    print("Erro: Não foi possível resolver o sistema (matriz singular).")