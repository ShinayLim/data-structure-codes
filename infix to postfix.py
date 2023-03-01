def infixToPostfix(expression):
    Operators = {'+', '-', '*', '/', '(', ')', '^'}
    Priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    stack = []
    output = ''

    for character in expression:

        if character not in Operators:

            output += character

        elif character == '(':

            stack.append('(')

        elif character == ')':

            while stack and stack[-1] != '(':
                output += stack.pop()

            stack.pop()

        else:

            while stack and stack[-1] != '(' and Priority[character] <= Priority[stack[-1]]:
                output += stack.pop()

            stack.append(character)

    while stack:
        output += stack.pop()

    return output


print("***** INFIX TO POSTFIX *****")
expression = input('Enter the infix expression -> ')
print('Infix expression is -> ', expression)
print('Postfix Expression is -> ', infixToPostfix(expression))

