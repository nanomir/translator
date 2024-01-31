from lexerMatlab import lexer
from parserMatlab import parser
from semanticMatlab import variables, func_var, functions
def generate_code(ast):
    code = ""
    tabs = 2
    previousEnd = []
    for node in ast:
        if node[0] =='ID':
            if variables.__contains__(node[1]):
                for i in range(tabs):
                    code+='\t'
                code += f"var {node[1]};\n"
                variables.remove(node[1])
        if node[0] == 'ASSIGN':
            for i in range(tabs):
                code+='\t'
            if variables.__contains__(node[1]) or func_var.__contains__(node[1]):
                code += f"var {node[1]} = {generate_assign_expression(node[2])};\n"
                variables.remove(node[1])
            else:
                code += f"{node[1]} = {generate_assign_expression(node[2])};\n"
        elif node[0] == 'COMPARE':
            pass
        elif node[0] == 'WHILE':
            for i in range(tabs):
                code+='\t'

            code += f"{node[1]}({generate_while_expression(node[2])})\n"
            for i in range(tabs):
                code+='\t'
            code+="{\n"
            tabs+=1
            previousEnd.append("WHILE")
        elif node[0] == 'FOR':
            for i in range(tabs):
                code+='\t'
            code += f"{node[1]}{generate_for_expression(node[2])}\n"
            for i in range(tabs):
                code+='\t'
            code+="{\n"
            tabs+=1
            previousEnd.append("FOR")
        elif node[0] == 'LOGIC':
            for i in range(tabs):
                code+='\t'
            match node[1]:
                case 'if':
                    code += f"{node[1]} ({generate_logic_expression(node[2])})\n"
                case 'elif':
                    code += f"else if ({generate_logic_expression(node[2])})\n"
                case 'else':
                    code += f"{node[1]}\n"
            for i in range(tabs):
                code+='\t'
            code+="{\n"
            tabs+=1
            previousEnd.append("LOGIC")
        elif node[0] == 'FUNCTION':
            for i in range(tabs):
                code+='\t'
            code += f"static var {generate_function_expression(node[1])[0]}\n"
            for i in range(tabs):
                code+='\t'
            code+="{\n"
            tabs+=1
            previousEnd.append(("FUNCTION", generate_function_expression(node[1])[1]))
        elif node[0] =='PRINT':
            for i in range(tabs):
                code+='\t'
            code += f"{generate_print_expression(node[2])}\n"

        elif node[0] == 'LBRACKET':
            for i in range(tabs):
                code+='\t'
            code+="{\n"
            tabs+=1
        elif node[0] == 'RBRACKET':
            tabs-=1
            for i in range(tabs):
                code+='\t'
            code+="}\n"
        elif node[0] == 'END':
            pop = previousEnd.pop()
            if pop[0] == 'FUNCTION':
                for i in range(tabs):
                    code+='\t'
                code+="return "+pop[1]+"\n"
            tabs-=1
            for i in range(tabs):
                code+='\t'
            code+="}\n"
            
    

    return code


def generate_assign_expression(ast):
    code = ""
    for node in ast:
        if node[0] == 'NUMBER':
            code += str(node[1])
        elif node[0] == 'STRING':
            code+=str(node[1])
        elif node[0] == 'ID':
            code+=str(node[1])
        elif node[0] == 'PLUS':
            code += " + "
        elif node[0] == 'MINUS':
            code += " - "
        elif node[0] == 'MULTIPLY':
            code += " * "
        elif node[0] == 'DIVIDE':
            code += " / "
        elif node[0] == 'COMPARE':
            code+=str(node[1])
        elif node[0] == 'LPAREN':
            code +="("
        elif node[0] == 'RPAREN':
            code+=")"
    return code

def generate_while_expression(ast):
    code = ""
    for node in ast:
        if node[0] == 'NUMBER':
            code += str(node[1])
        elif node[0] == 'ID':
            code+=str(node[1])
        elif node[0] == 'PLUS':
            code += " + "
        elif node[0] == 'MINUS':
            code += " - "
        elif node[0] == 'MULTIPLY':
            code += " * "
        elif node[0] == 'DIVIDE':
            code += " / "
        elif node[0] == 'COMPARE':
            code+=str(node[1])
        elif node[0] == 'FNAME':
            code+=str(node[1])
        elif node[0] == 'LBRACKET':
            code +="["
        elif node[0] == 'RBRACKET':
            code+="]"
        elif node[0] == 'LPAREN':
            code +="("
        elif node[0] == 'RPAREN':
            code+=")"

    return code

def generate_print_expression(ast):
    code = "System.Console.WriteLine("
    for node in ast:
        if node[0] == 'NUMBER':
            code += str(node[1])
        elif node[0] == 'ID':
            code+=str(node[1])
        elif node[0] == 'STRING':
            code+=str(node[1])
        elif node[0] == 'PLUS':
            code += " + "
        elif node[0] == 'MINUS':
            code += " - "
        elif node[0] == 'MULTIPLY':
            code += " * "
        elif node[0] == 'DIVIDE':
            code += " / "
        elif node[0] == 'COMPARE':
            code+=str(node[1])

    code+=')'
    return code

def generate_logic_expression(ast):
    code = ""
    for node in ast:
        if node[0] == 'NUMBER':
            code += str(node[1])
        elif node[0] == 'ID':
            code+=str(node[1])
        elif node[0] == 'PLUS':
            code += " + "
        elif node[0] == 'MINUS':
            code += " - "
        elif node[0] == 'MULTIPLY':
            code += " * "
        elif node[0] == 'DIVIDE':
            code += " / "
        elif node[0] == 'COMPARE':
            code+=str(node[1])
        elif node[0] == 'FNAME':
            code+=str(node[1])
        elif node[0] == 'LBRACKET':
            code +="["
        elif node[0] == 'RBRACKET':
            code+="]"
        elif node[0] == 'LPAREN':
            code +="("
        elif node[0] == 'RPAREN':
            code+=")"

    return code    

def generate_for_expression(ast):
    code = "(int "

    firstStage = True
    secondStage = False
    counter = ''
    for node in ast: 
        if node[0] == 'ID':
            if firstStage:
                code+=str(node[1])
                counter = str(node[1])
                firstStage = False
            elif secondStage:
                code+=counter + ' <= ' + str(node[1])
                secondStage = False
            else:
                code+=str(node[1])
        elif node[0] == 'ASSIGN':
            code +=' = '
        elif node[0] == 'NUMBER':
            if secondStage:
                code+=counter + ' <= ' + str(node[1])
                secondStage = False
            else:
                code+=str(node[1])
        elif node[0] == 'LPAREN':
            code +="("
        elif node[0] == 'RPAREN':
            code+=")"
        elif node[0] == 'PLUS':
            code += " + "
        elif node[0] == 'MINUS':
            code += " - "
        elif node[0] == 'MULTIPLY':
            code += " * "
        elif node[0] == 'DIVIDE':
            code += " / "
        elif node[0] == 'COLON':
            code+='; '
            secondStage=True
    code+='; ' + counter+'++)'
    return code
#for (int i=1; i<20; i++)
def generate_function_expression(ast):
    code = ""
    answer =''
    for node in ast: 
        if node[0] == 'FARGS':
            code+=str(node[1])  
        elif node[0] == 'FANSWER':
            answer = str(node[1])
        elif node[0] == 'FNAME':
            code+=str(node[1])
        elif node[0] == 'LPAREN':
            code +="("
        elif node[0] == 'RPAREN':
            code+=")"
    '''for node in ast:
        if node[0] == 'NUMBER':
            code += str(node[1])
        elif node[0] == 'ID':
            code+=str(node[1])
        elif node[0] == 'PLUS':
            code += " + "
        elif node[0] == 'MINUS':
            code += " - "
        elif node[0] == 'MULTIPLY':
            code += " * "
        elif node[0] == 'DIVIDE':
            code += " / "
        elif node[0] == 'COMPARE':
            code+=str(node[1])
        elif node[0] == 'FARGS':
            code+=str(node[1])  
        elif node[0] == 'FANSWER':
            answer = str(node[1])
        elif node[0] == 'FNAME':
            code+=str(node[1])
        elif node[0] == 'LBRACKET':
            pass
        elif node[0] == 'RBRACKET':
            pass
        elif node[0] == 'LPAREN':
            code +="("
        elif node[0] == 'RPAREN':
            code+=")"
        elif node[0] == 'ASSIGN':
            code+="="'''
    return code, answer

# Пример использования генератора кода
data = '''
x = 5 + 3;
z = 5;
y = z * 2;
text = 'abra';
l;
l;
l;
if 3 == z
y = y*2;
end
elif 2 == z
y = y*3;
end
else
y = y*1;
end
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

tokens = lexer(data)
ast = parser(tokens)
generated_code = '''
static void main()
\t{
'''
generated_code+=generate_code(ast)
generated_code+="\t}"

print(generated_code)