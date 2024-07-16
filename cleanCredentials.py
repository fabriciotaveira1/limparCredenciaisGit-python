import subprocess

def reset_github_credentials():
    # Comando para excluir as credenciais do GitHub no Windows
    cmd = 'cmdkey /delete:git:https://github.com'
    subprocess.run(cmd, shell=True)

    print("Credenciais do GitHub resetadas com sucesso.")

if __name__ == "__main__":
    reset_github_credentials()