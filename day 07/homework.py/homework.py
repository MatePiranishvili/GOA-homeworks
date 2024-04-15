#დავალება: მომხმარებელს შემოატანინეთ 4 სხვადასხვა ტიპის მონაცემი (string,integer,float,boolean) შემდეგ დაბეჭდეთ 
 #ეს შემოტანილი მონაცემები და მათი მონაცემთა ტიპები


name = input("please enter your name: ")
num1 = int(input("please enter your number: "))
num2 = float (input("please enter your second number: "))
variable = bool (input("please enter your boolean value: "))


print(name)
print(num1)
print(num2)
print(variable)

#შექმენით 5+ ცვლადი და ისე შეადარეთ ერთმანეთს რომ დაიბეჭდოს True.

boolean=True and True #True
boolean1=True or False #True
boolean2=False or True #True
boolean3=True or True  #True 
boolean4=True and False #True


print(boolean)
print(boolean1)
print(boolean2)
print(boolean3)
print(boolean4)

True and True #True
True and False #False
False and False #False
False and True  #False 
True or True  #True
True or False #True
False or False #False
False or True #True


print(True and True)#True
print(True and False)#False 
print(False and False)#False 
print(False and True)#False 
print(True or True)#True
print(True or False)#True
print(False or False)#False 
print(False or True)#True
