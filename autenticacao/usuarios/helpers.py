dominios = ["gmail", "hotmail", "outlook", "yahoo", "icloud", "protonmail"]
simbolos = ["!", "@", "$", "%", "¨¨", "&", "*", "(", ")", "#"]

def validar_email(email):
    if len(email) < 10: 
        return "E-mail pequeno demais. Tente novamente."
    if not "@" in email: 
        return "E-mail não contém \"@\". Tente novamente."

    # Verifica e-mail a partir do "@"
    partes_endereco_email = email[email.index("@"):]
    
    # Verifica domínio e extensão do e-mail
    if not any(dominio in partes_endereco_email for dominio in dominios) or not ".com" in partes_endereco_email or ".br" in partes_endereco_email: 
       return "E-mail não é válido. Tente novamente."
    
    return None


def validar_senha(senha):
    if len(senha) < 8:
        return "Senha possui menos de 8 caracteres. Tente novamente."
    if senha == senha.lower() or senha == senha.upper(): 
        return "A senha precisa possuir pelo menos uma letra maiúscula e uma minúscula. Tente novamente."
    if not any (simbolo in senha for simbolo in simbolos): 
        return "A senha precisa possuir pelo menos um símbolo. Tente novamente."

    return None