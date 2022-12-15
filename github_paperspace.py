import os


# Setup Github connection
def create_github_sshkey_on_machine(github_email: str):
    github_ssh_config = """
    Host *.github.com
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_ed25519
    """

    os.system(f'ssh-keygen -t ed25519 -C "{github_email}"')
    os.system('eval "$(ssh-agent -s)"')
    os.system("touch ~/.ssh/config")
    os.system(f"echo '{github_ssh_config}' >> ~/.ssh/config")
    os.system("ssh-add ~/.ssh/id_ed25519")
    os.system("cat ~/.ssh/id_ed25519.pub")
