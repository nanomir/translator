from pyclbr import Function


def lexer(input_string):
    tokens = []
    current_token = ''
    isString = False
    stringHelper = False

    for i, char in enumerate(input_string):
        if char.isdigit() and not isString:
            current_token += char
            if i != len(input_string) - 1 and (input_string[i + 1] == '.' or input_string[i + 1].isdigit()) :
                continue
            tokens.append(('NUMBER', int(current_token)))
            current_token = ''
        elif char =='"' or char =="'" or isString:
            current_token += char
            isString = True
            if i != len(input_string) - 1 and not ((input_string[i] =='"' or input_string[i]=="'") and stringHelper):
                stringHelper=True
                continue
            tokens.append(('STRING', current_token))
            isString = False
            stringHelper = False
            current_token = ''
        elif char.isalpha() or char == '_':
            current_token += char
            if i != len(input_string) - 1 and (input_string[i + 1].isalpha() or input_string[i + 1].isdigit() or input_string[i + 1] == '_'):
                continue
            if current_token == 'plus':
              tokens.append(('PLUS', None))
            elif current_token == 'minus':
              tokens.append(('MINUS', None))
            elif current_token == 'multiply':
               tokens.append(('MULTIPLY', None))
            elif current_token == 'divide':
                tokens.append(('DIVIDE', None))
            elif current_token == 'assign':
                tokens.append(('ASSIGN', None))
            elif current_token == "while":
                tokens.append(("WHILE", current_token))
                current_token = ''
            elif current_token == 'function':
                tokens.append(("FUNCTION", current_token))
                current_token = ''
            elif current_token == 'for':
                tokens.append(("FOR", current_token))
                current_token = ''
            elif current_token == 'end':
                tokens.append(("END", current_token))
                current_token = ''
            elif current_token =='disp':
                tokens.append(("PRINT", None))
                current_token = ''
            elif current_token =='else':
                tokens.append(('LOGIC', current_token))
                current_token = ''
            elif current_token =='elif':
                tokens.append(('LOGIC', current_token))
                current_token = ''
            elif current_token =='if':
                tokens.append(('LOGIC', current_token))
                current_token = ''   
            else:
                tokens.append(('ID', current_token))
                current_token = ''
        elif char == '+':
            tokens.append(('PLUS', None))
        elif char == '-':
            tokens.append(('MINUS', None))
        elif char == '*':
            tokens.append(('MULTIPLY', None))
        elif char == '/':
            tokens.append(('DIVIDE', None))

        elif char == '(':
            tokens.append(('LPAREN', None))
        elif char == ')':
            tokens.append(('RPAREN', None))

        elif char == '{':
            tokens.append(('LBCRACKET', None))
        elif char == '}':
            tokens.append(('RBCRACKET', None))

        elif char == '[':
            tokens.append(('LBRACKET', None))
        elif char == ']':
            tokens.append(('RBRACKET', None))

        elif char == '=':
            current_token += char
            if i != len(input_string) - 1 and input_string[i + 1] == '=' or current_token == '==':
                if len(current_token)>1:
                    tokens.append(('COMPARE', current_token))
                    current_token=''
                else:
                    continue
            else: 
                tokens.append(('ASSIGN', None))
                current_token=''
        elif char == '\n':
            tokens.append(('NEWLINE', None))
        elif char =='>' or char =='<':
            tokens.append(('COMPARE', char))
        elif char ==':':
            tokens.append(('COLON', None))
    return tokens

# Пример использования лексера
data = '''
x = 5 + 3;
z = 3;
y = z * 2;
text = 'abra'
if x == z
y = y*2;
end
l;
l;
l;
while (x>3)
a= a+1;
    while (l<5)
    l=l+1;
    end
end
for c = 1:x
y = y + 1;
end
function [c] = myfun(b)
    x = b;
    c = x+b;
    for i = 5+1:10
    test+1;

end
end
disp(a);
v = myfun(x)
'''

#tokens = lexer(data)

#for token in tokens:
#    print(token)