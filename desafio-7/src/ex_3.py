import numpy as np

A = np.array([[50, 20], [30, 30]])
B = np.array([30, 12])

try:
    det = np.linalg.det(A)

    if np.abs(det) < 1e-10:
        print("Erro: A matriz A não é invertível (determinante zero).")
        
    else:
        
        X = np.linalg.solve(A, B)

        x = X[0]  
        y = X[1]  

        print("Quantidades por unidade:")
        print(f"x = {x:.2f} kg de farinha por pão")
        print(f"y = {y:.2f} kg de açúcar por bolo")

        farinha = 40 * x + 25 * y
        acucar = 40 * x + 25 * y  
        print(f"\nConsumo para 40 pães e 25 bolos:")
        print(f"Farinha: {farinha:.2f} kg")
        print(f"Açúcar: {acucar:.2f} kg")

        print("\nVerificação:")
        print(f"50x + 20y = 50({x:.2f}) + 20({y:.2f}) = {50*x + 20*y:.2f}")
        print(f"30x + 30y = 30({x:.2f}) + 30({y:.2f}) = {30*x + 30*y:.2f}")

except np.linalg.LinAlgError:
    print("Erro: Não foi possível resolver o sistema (matriz singular).")