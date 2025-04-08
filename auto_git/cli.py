import subprocess

def run_git_command(command):
    """Git buyruqlarini bajarish uchun yordamchi funksiya"""
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode != 0:
        print(f"Xatolik: {stderr.decode('utf-8')}")
    else:
        print(stdout.decode('utf-8'))

def aic():
    """Git add, commit va pushni bajarish"""
    # Git status (o'zgartirilgan fayllarni ko'rsatish)
    print("\nO'zgartirilgan fayllar:")
    run_git_command("git status")
    
    # Git add
    run_git_command("git add .")

    # Git diff (o'zgartirishlarni ko'rsatish)
    print("\nO'zgartirishlar:")
    run_git_command("git diff")

    aic_commit = run_git_command('aic')

    # Git commit
    run_git_command(f'git commit -m "{aic_commit}"')

    # Git push (sana uchun branchni avtomatik aniqlash)
    branch_name = subprocess.check_output("git branch --show-current", shell=True).decode().strip()
    run_git_command(f"git push origin {branch_name}")


if __name__ == "__main__":
    aic()
