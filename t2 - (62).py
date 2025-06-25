def eh_palindromo(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

print(eh_palindromo("arara"))       
print(eh_palindromo("Ame a ema"))   
print(eh_palindromo("Python"))      
