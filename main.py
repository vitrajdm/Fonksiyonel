def faktoriyel(n):
    if n == 1:
        return 1
    else:
        return n * faktoriyel(n - 1)
print(faktoriyel())     # Parametre yerine faktoriyel işleme girmesini istediğiniz sayıyı yazın.