from string import *

if __name__ == '__main__':
    # Imprimindo uma string.
    s = "Olá, mundo!"
    print(s)

    # Tipo de uma string.
    type(s)

    # Tamanho de uma string.
    len(s)

    # Concatenação
    print("Meu Brasil " + "brasileiro")

    # Substitui uma substring por alguma outra coisa.
    s1 = s.replace("mundo", "meu abacate")

    print(s1)

    # A string s começa com "Olá"?
    print(s.startswith("Olá"))

    # A string s termina com "mundo"?
    print(s.endswith("mundo"))

    # Quantas ocorrências da palavra "abacate" a string s1 possui?
    print(s1.count("abacate"))
    
    # Como "capitalizar" (transformar a primeira letra da primeira palavra em maiúscula).
    s = "ordem e progresso"
    print(s.capitalize())

    # Como verificar se uma string só possui números.
    '12345'.isdigit()
    '12345abc'.isdigit()

    # Como verificar se uma string é alfanumérica (só possui letras e números).
    '12345abc'.isalnum()
    
    s = "Olá, mundo!"
    print(s[0])
    print(s[2])
    print(s[6])
    print(s[-1])
    print(s[-2])
    print(s[-4])
    s[1:3]
    
    # Forma mais avançada de formatação de strings
    frase = 'Um triângulo de base igual a {0} e altura igual a {1} possui área igual a {2}.'.format(3, 4, 12)
    print(frase)

    # Formatação de strings com f-strings
    linguagem = "Python"    
    print(f"Programando em {linguagem}")