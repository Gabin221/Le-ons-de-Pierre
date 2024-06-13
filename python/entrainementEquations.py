import sympy as sp
import random

def generate_equation(choice):    
    x = sp.Symbol('x')
    
    if choice == 1:
        # Equation de type ax + b = 0
        a = 0
        while a == 0:
            a = random.randint(-10, 10)
        b = random.randint(-10, 10)
        equation = a * x + b
        solutions = sp.solve(equation, x)
        
    elif choice == 2:
        # Equation de type ax^2 + bx + c = 0
        a = 0
        while a == 0:
            a = random.randint(-10, 10)
        b = random.randint(-10, 10)
        c = random.randint(-10, 10)
        equation = f"{a} * x**2 + {b} * x + {c}"
        solutions = sp.solve(a * sp.Symbol('x')**2 + b * sp.Symbol('x') + c, sp.Symbol('x'))
        
    elif choice == 3:
        # Equation de type a*exp(b*x) + c = 0
        a = 0
        b = 0
        c = 0
        while a == 0 or b == 0:
            a = random.randint(-10, 10)
            b = random.randint(-10, 10)
            c = random.randint(-10, 10)
            if a != 0:
                while -c/a <= 0:
                    a = random.randint(-10, 10)
                    b = random.randint(-10, 10)
                    c = random.randint(-10, 10)
            else:
                a = random.randint(-10, 10)
                b = random.randint(-10, 10)
                c = random.randint(-10, 10)
        equation = f"{a}*exp({b}*x) + {c}"
        solutions = sp.solve(a*sp.exp(b*sp.Symbol('x')) + c, sp.Symbol('x'), dict=False)
        solutions = [sol.evalf() for sol in solutions if sol.is_real]
        
    elif choice == 4:
        # Equation de type a*log(b*x) + c = 0
        a = 0
        b = 0
        while a == 0 or b == 0:
            a = random.randint(-10, 10)
            b = random.randint(2, 10)  # b doit être > 1 pour éviter les logarithmes de nombre négatif ou nul
        c = random.randint(-10, 10)
        equation = f"{a}*log({b}*x) + {c}"
        solutions = sp.solve(a*sp.log(b*sp.Symbol('x')) + c, sp.Symbol('x'), dict=False)
        solutions = [sol.evalf() for sol in solutions if sol.is_real]
        
    elif choice == 5:
        types = ['cos', 'sin', 'tan']
        selected_type = random.choice(types)
        a = 0
        b = 0
        while a == 0 or b == 0:
            a = random.randint(-10, 10)
            b = random.randint(-10, 10)
        
        if selected_type == "cos":
            equation = f"{a}*cos({b}*x)"
            solutions = sp.solveset(a*sp.cos(b*sp.Symbol('x')), sp.Symbol('x'))
            solutions = [sol.evalf() for sol in solutions if sol.is_real]
        elif selected_type == "sin":
            equation = f"{a}*sin({b}*x)"
            solutions = sp.solveset(a*sp.sin(b*sp.Symbol('x')), sp.Symbol('x'))
            solutions = [sol.evalf() for sol in solutions if sol.is_real]
        elif selected_type == "tan":
            equation = f"{a}*tan({b}*x)"
            solutions = sp.solveset(a*sp.tan(b*sp.Symbol('x')), sp.Symbol('x'))
            solutions = [sol.evalf() for sol in solutions if sol.is_real]
        
    return sp.pretty(equation), solutions

def main():
    print("Bienvenue dans le solveur d'équations!")
    
    while True:
        print("\nChoisissez le type d'équation (tapez le numéro correspondant) :")
        print("1. Polynôme de degré 1")
        print("2. Polynôme de degré 2")
        print("3. Exponentielle")
        print("4. Logarithme")
        print("5. Trigonométrique")
        print("6. Quitter")
        
        choice = input("Votre choix : ")
        
        if choice == '6':
            print("Au revoir!")
            break
        
        try:
            choice = int(choice)
            if choice < 1 or choice > 5:
                print("Choix invalide. Veuillez choisir un numéro entre 1 et 5.")
                continue
        except ValueError:
            print("Choix invalide. Veuillez entrer un numéro.")
            continue
        
        equation, solutions = generate_equation(choice)
        print(f"\nÉquation générée : {equation}")
        
        ready = input("Êtes-vous prêt à voir les solutions de cette équation ? (oui) : ")
        
        if ready.lower() == 'oui':
            if solutions:
                print("La/les solution(s) de l'équation sont :")
                for solution in solutions:
                    print(f"x = {solution}")
            else:
                print("L'équation n'a pas de solution dans l'ensemble des réels.")
        else:
            print("Opération annulée.")

if __name__ == "__main__":
    main()
