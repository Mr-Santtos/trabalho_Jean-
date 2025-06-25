texto_completo = "Programação em Python"
indice_inicio = 4
indice_fim = 12

indice_inicio = max(0, indice_inicio)
indice_fim = min(len(texto_completo), indice_fim)

substring = texto_completo[indice_inicio:indice_fim]
print(substring)

texto_completo_2 = "ABCDE"
indice_inicio_2 = 1
indice_fim_2 = 10

indice_inicio_2 = max(0, indice_inicio_2)
indice_fim_2 = min(len(texto_completo_2), indice_fim_2)

substring_2 = texto_completo_2[indice_inicio_2:indice_fim_2]
print(substring_2)
