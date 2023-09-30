def triangle(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return 'Invalid' 
    if a == b == c:
        return 'Equilateral'
    elif a == b != c or a == c != b or c == b != a:
        return 'Isosceles'
    elif a != b != c:
        return 'Scalene'

while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    print(triangle(a, b, c))
