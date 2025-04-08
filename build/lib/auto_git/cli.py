import subprocess

def run_git_command(command):
    """Git buyruqlarini bajarish uchun yordamchi funksiya"""
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    print(stdout.decode('utf-8'))

def aic():
    """Git add, commit va pushni bajarish"""
    run_git_command("git status")
    
    # Git add
    run_git_command("git add .")

    run_git_command("git diff")

    aic_commit = run_git_command('aic')

    run_git_command(f'git commit -m "{aic_commit}"')

    branch_name = subprocess.check_output("git branch --show-current", shell=True).decode().strip()
    run_git_command(f"git push origin {branch_name}")


if __name__ == "__main__":
    aic()
