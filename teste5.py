def inverter_string(s):    

    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]
    
    return string_invertida

string_original = input("Informe uma string: ")

string_invertida = inverter_string(string_original)

print(f"String original: {string_original}")
print(f"String invertida: {string_invertida}")
