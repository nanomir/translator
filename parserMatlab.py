from lexerMatlab import lexer
from semanticMatlab import variables, functions, func_var
import sys

def parser(tokens):
    ast = []

    i = 0
    while i < len(tokens):
        token = tokens[i]

        if token[0] == 'ID' and i + 1 < len(tokens) and tokens[i + 1][0] == 'ASSIGN':
            variable = token[1]
            if (not variables.__contains__(variable)):
                variables.add(variable)
            expression = parse_assign_expression(tokens[i + 2:])
            ast.append(('ASSIGN', variable, expression[0]))
            i += expression[1]+1
        elif token[0] == 'FUNCTION':
            expression = parse_function_expression(tokens[i+1:])
            ast.append(('FUNCTION', expression[0]))
            i += expression[1]+1
        elif token[0] == 'ID':
            ast.append(('ID', token[1]))
            variable = token[1]
            if variable not in variables:
                variables.add(variable)
        elif token[0] == 'NUMBER':
            ast.append(('NUMBER', token[1]))
        elif token[0] == 'STRING':
            ast.append(('STRING', token[1]))
        elif token[0] == 'PLUS':
            ast.append(('PLUS', None))
        elif token[0] == 'MINUS':
            ast.append(('MINUS', None))
        elif token[0] == 'MULTIPLY':
            ast.append(('MULTIPLY', None))
        elif token[0] == 'DIVIDE':
            ast.append(('DIVIDE', None))
        elif token[0] == 'WHILE':
            expression = parse_while_expression(tokens[i+2:])
            ast.append(('WHILE', token[1], expression[0]))
            i+= expression[1]+1
        elif token[0] == 'FOR':
            expression = parse_for_expression(tokens[i+1:])
            ast.append(('FOR', token[1], expression[0]))
            i+= expression[1]+1
        elif token[0] == 'LBRACKET':
            ast.append(('LBRACKET', None))
        elif token[0] == 'RBRACKET':
            ast.append(('RBRACKET', None))
        elif token[0] =='END':
            ast.append(('END', token[1]))
        elif token[0] =='PRINT':
            expression = parse_for_print(tokens[i+1:])
            ast.append(('PRINT',token[1], expression[0]))
        elif token[0] =='LOGIC':
            expression = parse_logic_expression(tokens[i+1:])
            ast.append(('LOGIC',token[1], expression[0]))
            i+= expression[1]+1

        i += 1

    return ast

def error(cause, guilty):
        match cause:
            case "variable":
                print(f"Ошибка: переменная '{guilty}' не была объявлена")
            case "function exists":
                print(f"Ошибка: функция '{guilty}' уже объявлена")
            case "function not exists":
                print(f"Ошибка: функция '{guilty}' не объявлена")
            case "wrong type":
                print(f"Ошибка: '{guilty}' — неверный тип данных")
            case "missing symbol":
                print(f"Ошибка: '{guilty}' — отсутствует символ")
            case _:
                print(f"Общая ошибка")
        sys.exit(1)

def parse_logic_expression(tokens):

    ast = []

    i = 0

    while i < len(tokens):
        token = tokens[i]

        if token[0] == 'NUMBER':
            ast.append(('NUMBER', token[1]))
        elif token[0] == 'STRING':
            ast.append(('STRING', token[1]))
        elif token[0] == 'PLUS':
            ast.append(('PLUS', None))
        elif token[0] == 'MINUS':
            ast.append(('MINUS', None))
        elif token[0] == 'MULTIPLY':
            ast.append(('MULTIPLY', None))
        elif token[0] == 'DIVIDE':
            ast.append(('DIVIDE', None))
        elif token[0] == 'COMPARE':
            ast.append(('COMPARE', token[1]))
        elif token[0] == 'ID':
            variable = token[1]
            if variable not in variables:
                error("variable", variable)
            else:
                ast.append(('ID', variable))
        else:
            break
        i += 1

    return ast, i

def parse_for_print(tokens):
    ast = []

    i=0

    while i < len(tokens):
        token = tokens[i]
        if token[0] == 'LPAREN':
            pass
        elif token[0] == 'NUMBER':
            ast.append(('NUMBER', token[1]))
        elif token[0] == 'STRING':
            ast.append(('STRING', token[1]))
        elif token[0] == 'PLUS':
            ast.append(('PLUS', None))
        elif token[0] == 'MINUS':
            ast.append(('MINUS', None))
        elif token[0] == 'MULTIPLY':
            ast.append(('MULTIPLY', None))
        elif token[0] == 'DIVIDE':
            ast.append(('DIVIDE', None))    
        elif token[0] == 'LPAREN':
            pass
        elif token[0] == 'ID':
            
            variable = token[1]

            if variable not in variables and variable not in functions:
                error("variable", variable)
            else:
                ast.append(('ID', variable))
        else:
            break
        i += 1

    return ast, i

def parse_for_expression(tokens):
    ast = []

    i=0
    isNameOfCounter = True
    while i < len(tokens):
        token = tokens[i]

        if token[0] == 'NUMBER':
            ast.append(('NUMBER', token[1]))
        elif token[0] == 'STRING':
            error("wrong type", 'string')
        elif token[0] == 'COLON':
            ast.append(('COLON', None))
        elif token[0] == 'ASSIGN':
            ast.append(('ASSIGN', None))
        elif token[0] == 'PLUS':
            ast.append(('PLUS', None))
        elif token[0] == 'MINUS':
            ast.append(('MINUS', None))
        elif token[0] == 'MULTIPLY':
            ast.append(('MULTIPLY', None))
        elif token[0] == 'DIVIDE':
            ast.append(('DIVIDE', None))
        elif token[0] == 'RPAREN':
            ast.append(('RPAREN', None))
        elif token[0] == 'LPAREN':    
            ast.append(('LPAREN', None))
        elif token[0] == 'ID':
            
            variable = token[1]

            if isNameOfCounter:
                ast.append(('ID', variable))
                isNameOfCounter = False
            elif variable not in variables and variable not in func_var:
                error("variable", variable)
            else:
                ast.append(('ID', variable))
        else:
            break
        i += 1

    return ast, i

def parse_assign_expression(tokens):
    ast = []

    i = 0
    isAssigned = False
    while i < len(tokens):
        token = tokens[i]

        if token[0] == 'NUMBER':
            ast.append(('NUMBER', token[1]))
            isAssigned = True
        elif token[0] == 'STRING':
            ast.append(('STRING', token[1]))
            isAssigned = True
        elif token[0] == 'PLUS':
            ast.append(('PLUS', None))
        elif token[0] == 'MINUS':
            ast.append(('MINUS', None))
        elif token[0] == 'MULTIPLY':
            ast.append(('MULTIPLY', None))
        elif token[0] == 'DIVIDE':
            ast.append(('DIVIDE', None))
        elif token[0] == 'RPAREN':
            ast.append(('RPAREN', None))
        elif token[0] == 'LPAREN':    
            ast.append(('LPAREN', None))
        elif token[0] == 'ID':
            
            variable = token[1]
            if variable not in variables and variable not in func_var and variable not in functions:
                error("variable", variable)
            else:
                ast.append(('ID', variable))
                isAssigned = True
        else:
            break
        i += 1
    
    if not isAssigned :
            error('missing symbol', 'Обьявление')

    return ast, i

def parse_function_expression(tokens):
    ast = []

    i = 0
    args = False
    name = False
    answer = False
    while i < len(tokens):
        token = tokens[i]

        if token[0] == 'NUMBER':
            ast.append(('NUMBER', token[1]))
        elif token[0] == 'STRING':
            ast.append(('STRING', token[1]))
        elif token[0] == 'PLUS':
            ast.append(('PLUS', None))
        elif token[0] == 'ASSIGN':
            ast.append(('ASSIGN', None))
            name = True
        elif token[0] == 'MINUS':
            ast.append(('MINUS', None))
        elif token[0] == 'MULTIPLY':
            ast.append(('MULTIPLY', None))
        elif token[0] == 'DIVIDE':
            ast.append(('DIVIDE', None))
        elif token[0] == 'COMPARE':
            ast.append(('COMPARE', token[1]))

        elif token[0] == 'RBRACKET':
            ast.append(('RBRACKET', None))
            answer = False
        elif token[0] == 'LBRACKET':
            ast.append(('LBRACKET', None))
            answer= True

        elif token[0] == 'RBCRACKET':
            ast.append(('RBCRACKET', None))
            break
        elif token[0] == 'LBCRACKET':
            ast.append(('LBCRACKET', None))

        elif token[0] == 'RPAREN':
            ast.append(('RPAREN', None))
            args = False
        elif token[0] == 'LPAREN':    
            ast.append(('LPAREN', None))
            args = True
            
        elif token[0] == 'ID':
            if args ==True:
                if token[1] not in functions:
                    func_var.add(token[1])
                ast.append(('FARGS', token[1]))
            if answer ==True:
                if token[1] not in functions:
                    func_var.add(token[1])
                ast.append(('FANSWER', token[1]))
            if name ==True:
                if token[1] not in functions:
                    functions.add(token[1])
                else:
                    error("function exists", token[1])
                ast.append(('FNAME', token[1]))
                name = False
        else:
            break
        i += 1

    return ast, i    

def parse_while_expression(tokens):

    ast = []

    i = 0

    while i < len(tokens):
        token = tokens[i]

        if token[0] == 'NUMBER':
            ast.append(('NUMBER', token[1]))
        elif token[0] == 'STRING':
            ast.append(('STRING', token[1]))
        elif token[0] == 'PLUS':
            ast.append(('PLUS', None))
        elif token[0] == 'MINUS':
            ast.append(('MINUS', None))
        elif token[0] == 'MULTIPLY':
            ast.append(('MULTIPLY', None))
        elif token[0] == 'DIVIDE':
            ast.append(('DIVIDE', None))
        elif token[0] == 'COMPARE':
            ast.append(('COMPARE', token[1]))
        elif token[0] == 'ID':
            variable = token[1]
            if variable not in variables:
                error("variable", variable)
            else:
                ast.append(('ID', variable))
        else:
            break
        i += 1

    return ast, i

# Пример использования парсера
data = '''
x = 5 + 3;
z = 5;
y = z * 2;
text = 'abra';
l;
l;
l;
function [c] = myfun(b)
    x = b;
    c = x+b;
end
while (x>3)
a= a+1;
    while (l<5)
    l=l+1;
    end
end
for c = 1:x
end
y = y + 1;
disp(y);
v = myfun(x);
'''

#tokens = lexer(data)
#ast = parser(tokens)

#for node in ast:
#    print(node)
#variables = variables.clear
#func_var = func_var.clear
#functions = functions.clear