import random
import string
import os
import csv

def gerar_senha(size=10):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for i in range(size))
    return senha

def salvar_senha(nome, email, senha):
    with open("senhas.csv", "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nome, email, senha])

def ler_senhas():
    if os.path.exists("senhas.csv"):
        with open("senhas.csv", "r") as file:
            reader = csv.reader(file)
            senhas = list(reader)
            if senhas:
                print("Senhas salvas:")
                for linha in senhas:
                    print(f"Nome: {linha[0]}, Email: {linha[1]}, Senha: {linha[2]}")
            else:
                print("Nenhuma senha salva.")
    else:
        print("Nenhuma senha salva.")

def adicionar_conta_existente():
    nome = input("Nome da conta ou serviço: ")
    email = input("Email: ")
    senha = input("Senha: ")
    salvar_senha(nome, email, senha)
    print(f"Conta {nome} adicionada com sucesso.")

def main():
    while True:
        bem_vindo = int(input("--------------- Bem-vindo ao gerenciador de senhas ---------------\nEscolha uma opção para prosseguir:\n1-Gerar senha\n2-Abrir gerenciador de senhas\n3-Adicionar conta existente\n4-Sair\n"))
        
        if bem_vindo == 1:
            nome = input("Nome da conta ou serviço: ")
            email = input("Email: ")
            senha = gerar_senha()
            salvar_senha(nome, email, senha)
            print(f"Sua senha gerada para {nome} é: {senha}")
            input("Pressione Enter para continuar...")
        elif bem_vindo == 2:
            ler_senhas()
            input("Pressione Enter para continuar...")
        elif bem_vindo == 3:
            adicionar_conta_existente()
            input("Pressione Enter para continuar...")
        elif bem_vindo == 4:
            print("Saindo do gerenciador de senhas.")
            break
        else:
            print("Opção inválida. Por favor, escolha 1, 2, 3 ou 4.")
            input("Pressione Enter para continuar...")

if __name__ == "__main__":
    main()
