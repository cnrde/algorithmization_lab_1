def  F(n):
    if n == 1:
        return 5
    if n == 2:
        return 5
    if n > 2:
        return 5*F(n-1) - 4*F(n-2)
print(F(13))
