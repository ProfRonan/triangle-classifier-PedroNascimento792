def verificar_triangulo(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "Não é um triângulo"
    elif a == b == c:
        return "Equilátero"
    elif a == b or a == c or b == c:
        return "Isósceles"
    else:
        return "Escaleno"

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

tipo_triangulo = verificar_triangulo(a, b, c)

print("O tipo de triângulo formado é:", tipo_triangulo)
