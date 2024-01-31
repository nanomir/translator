import generatorMatlab

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
generatorMatlab.generate(data, True, True, True)