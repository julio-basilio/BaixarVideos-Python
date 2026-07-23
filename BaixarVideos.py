from colorama import Fore, Back, Style, init
import json
from pytubefix import YouTube
from pytubefix.cli import on_progress

init(autoreset=True)


with open("usuarios.json", encoding='utf-8') as arquivo:
    usuarios = json.load(arquivo)
    
def AcharUser(nome, senha, usuarios):
    for usuario in usuarios:
        if usuario['nome'] == nome and usuario['senha'] == senha:
            return usuario  
    return None

def Layout():
    for _ in range(20):
        print(Fore.MAGENTA + "-", end="") 
    print() 
    

def InserirUser(usuarios, novo_nome):
    with open("usuarios.json", "w", encoding='utf-8') as arquivo_escrita:
        json.dump(usuarios, arquivo_escrita, indent=4, ensure_ascii=False)
                    
    print(Fore.GREEN + f"Usuário '{novo_nome}' cadastrado com sucesso!")
        
def BaixarVideos(usuario_atual):
    url = input("Digite a URL do video do Youtube: ")

    yt = YouTube(url, on_progress_callback=on_progress)
    ys = yt.streams.get_highest_resolution()
    print(Fore.YELLOW + f"Baixando: {yt.title} "+Fore.BLUE)
    ys.download(output_path="Video")
    print(Fore.GREEN + "\nDownload concluído!")

    if "links_baixados" not in usuario_atual:
        usuario_atual["links_baixados"] = []
        
    usuario_atual["links_baixados"].append(url)

    with open("usuarios.json", "w", encoding='utf-8') as arquivo_escrita:
        json.dump(usuarios, arquivo_escrita, indent=4, ensure_ascii=False)
    print(Fore.CYAN + "Histórico de downloads atualizado no JSON!")
        
def Op(op):
    match op:
        case 1:
            print(Fore.CYAN + "--- LOGIN ---")
            nome = input("Nome: ").lower() 
            senha = input("Senha: ")
            
            usuario_logado = AcharUser(nome, senha, usuarios)
            
            if usuario_logado: 
                print(Fore.GREEN + "Login efetuado com sucesso!")
                BaixarVideos(usuario_logado)
            else:
                print(Fore.RED + "Usuário ou Senha não encontrado.")
            
        case 2:
            print(Fore.CYAN + "--- CADASTRO ---")
            novo_nome = input("Digite o nome para cadastro: ").lower()
            
            if AcharUser(novo_nome, "", usuarios) or any(u['nome'] == novo_nome for u in usuarios):
                print(Fore.RED + "Erro: Este usuário já está cadastrado!")
                return 

            nova_senha = input("Digite a senha: ")

            novo_usuario = {
                "nome": novo_nome, 
                "senha": nova_senha,
                "links_baixados": []
            }
            
            usuarios.append(novo_usuario)


            InserirUser(usuarios, novo_nome)
            

            BaixarVideos(novo_usuario)
            
        case _:
            print(Fore.RED + "Opção inválida")
            
Layout()

try:
    op = int(input("Escolha uma opção \n1- Entrar\n2- Cadastrar\n: "))
    Op(op)
except ValueError:
    print(Fore.RED + "Por favor, digite um número válido!")

input(Fore.LIGHTBLACK_EX + "\nPrescione ENTER para sair...")