# Stringe invertida

def inverter_string(string_original):
    tamanho = len(string_original)
    string_invertida = ''

    for letra in range(tamanho - 1, -1, -1):
        string_invertida += string_original[letra]

    return string_invertida

string_original = input("Digite uma palavra ou frase para inverter: ")
string_invertida = inverter_string(string_original)

print("A string invertida é:", string_invertida)

