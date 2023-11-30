def calculatrice():
    try:
        expression = input("Entrez une expression mathématique : ")
        resultat = evaluer_expression(expression)
        print(f"Le résultat de l'expression {expression} est : {resultat}")

    except (ValueError, ZeroDivisionError) as e:
        print(f"Erreur : {e}")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

def evaluer_expression(expression):
    operateurs = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    output = []
    operateurs_stack = []

    for token in expression.split():
        if token.isnumeric():
            output.append(float(token))
        elif token in operateurs:
            while (operateurs_stack and
                   operateurs_stack[-1] in operateurs and
                   operateurs[operateurs_stack[-1]] >= operateurs[token]):
                output.append(operateurs_stack.pop())
            operateurs_stack.append(token)
        elif token == '(':
            operateurs_stack.append(token)
        elif token == ')':
            while operateurs_stack and operateurs_stack[-1] != '(':
                output.append(operateurs_stack.pop())
            operateurs_stack.pop()

    while operateurs_stack:
        output.append(operateurs_stack.pop())

    return evaluer_postfixe(output)

def evaluer_postfixe(expression_postfixe):
    pile = []
    for token in expression_postfixe:
        if isinstance(token, (int, float)):
            pile.append(token)
        elif token in ('+', '-', '*', '/'):
            b = pile.pop()
            a = pile.pop()
            if token == '+':
                pile.append(a + b)
            elif token == '-':
                pile.append(a - b)
            elif token == '*':
                pile.append(a * b)
            elif token == '/':
                if b == 0:
                    raise ValueError("Division par zéro")
                pile.append(a / b)
    return pile[0]

if __name__ == "__main__":
    calculatrice()