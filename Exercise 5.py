a = [1,2,3,4,5,6,7,8,9,10]
m = [0,0,0,0,0,0,0,0,0,0]
x = int(input("Digite um número para multiplicar: "))

for i in range(len(a)):
    m[i] = a[i] * x

print(m)