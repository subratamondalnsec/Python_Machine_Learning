a=0b1010 #Binary Literals
b=100 #Decimal Literals
c=0o310 # Octal Literals
d=0x12c # Hexadecimal Literals

# Float Literals

float_1=10.5
float_2=1.5e2 # 1.5*10^2
float_3=1.5e-3 # 1.5*10^-3

# Complex Literals
x=3.14j

print (a,b,c,d)
print(float_1,float_2,float_3)
print(x,x.imag,x.real)


st='This is python'
sts="This is python"
char = "C"
multiline_Str="""This is a multiline String with more than one line code"""
unicode=u"\U0001f600\U0001f606" # emoji
raw_str=r"raw \n string"

print(st)
print(sts)
print(char)
print(multiline_Str)
print(unicode)
print(raw_str)

a=True+4
b=False+10
print ("a",a)
print ("b",b)

a=None
print(a)