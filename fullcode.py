from sympy import *
x=symbols('x')
#INPUT

print("Enter constraints")
a=float(input("Enter a"))
b=float(input("Enter b"))
ex=input("Enter expression")
expr=sympify(ex)

#1 segment

print("\n\n1-SEGMENT")
h1=(int(b)-int(a))/2
fa=expr.subs(x,a)
fb=expr.subs(x,b)
y0=h1*(fa+fb)
print("y0=",y0)

# 2-seg
print("\n\n2-SEGMENT")
fab=expr.subs(x,a+h1)
print("x    f(x)")
print(a,"   ",fa)
print(a+h1,"   ",fab)
print(b,"   ",fb)
y1=(h1/2)*(fa+2*fab+fb)
print("y1=",y1)



# 4-seg
print("\n\n2 SEGMENT")
h3=(b-a)/4
n=a
#for displaying
print("x   f(x)")
for i in range(5):
    print(n,"  ",expr.subs(x,n))
    n=n+h3
s=0
n=a
#for calculating
for i in range(5):
    if i==0 or i==4:
        s=s+expr.subs(x,n)
        n=n+h3
    else:
        s=s+2*expr.subs(x,n)
        n=n+h3
y2=h3*s/2
print("y2=",y2)

#8 segment
print("\n\n8 segment")
h4=(b-a)/8
n=a
# for displaying
for i in range(9):
    print(n,"  ",expr.subs(x,n))
    n=n+h4
s=0
n=a
#for calculating
for i in range(9):
    if i==0 or i==8:
        s=s+expr.subs(x,n)
        n=n+h4
    else:
        s=s+2*expr.subs(x,n)
        n=n+h4
y3=h4*s/2
print("y3=",y3)


#FInal calculation
r11=(4*y1-y0)/3
r12=(4*y2-y1)/3
r13=(4*y3-y2)/3
print("\n\n r11=",r11,"\n r12=",r12,"\n r13=",r13,"\n\n")

r21=(16*r12-r11)/15
r22=(16*r13-r12)/15
print(" r21=",r21,"\nr22=",r22,"\n\n")

r31=(64*r22-r21)/63
print("r31=",r31)
