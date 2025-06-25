def validar_email(email):
    if email.count("@") != 1:
        return False
    usuario, dominio = email.split("@")
    if len(usuario) < 1:
        return False
    if "." not in dominio:
        return False
    parte_antes_ponto, *resto = dominio.split(".")
    if len(parte_antes_ponto) < 1:
        return False
    if len(resto[-1]) < 2:
        return False
    return True
