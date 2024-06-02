import random
import string
import os

def gerar_senha(size=10):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for i in range(size))
    return senha

def salvar_senha(nome, senha):
    with open("senhas.txt", "a") as file:
        file.write(f"{nome}: {senha}\n")

def ler_senhas():
    if os.path.exists("senhas.txt"):
        with open("senhas.txt", "r") as file:
            senhas = file.readlines()
            if senhas:
                print("Senhas salvas:")
                for senha in senhas:
                    print(senha.strip())
            else:
                print("Nenhuma senha salva.")
    else:
        print("Nenhuma senha salva.")

def main():
    while True:
        bem_vindo = int(input("--------------- Bem-vindo ao gerenciador de senhas ---------------\nEscolha uma opção para prosseguir:\n1-Gerar senha\n2-Abrir gerenciador de senhas\n3-Sair\n"))
        
        if bem_vindo == 1:
            nome = input("Nome da conta ou serviço: ")
            senha = gerar_senha()
            salvar_senha(nome, senha)
            print(f"Sua senha gerada para {nome} é: {senha}")
        elif bem_vindo == 2:
            ler_senhas()
        elif bem_vindo == 3:
            print("Saindo do gerenciador de senhas.")
            break
        else:
            print("Opção inválida. Por favor, escolha 1, 2 ou 3.")

if __name__ == "__main__":
    main()
