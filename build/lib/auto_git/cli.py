import subprocess
from rich.console import Console
from rich.text import Text

console = Console()

def run_git_command(command, description=None, style="white"):
    """Git buyruqlarini bajarish va natijani chiqarish"""
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    output = stdout.decode('utf-8').strip()
    error = stderr.decode('utf-8').strip()

    if description:
        console.rule(f"[bold {style}]{description}[/bold {style}]")

    if output:
        console.print(Text(output, style=style))
    if error:
        console.print(Text(error, style="bold red"))

    return output


def aic():
    """Git add, aic commit va push jarayonlarini avtomatlashtiradi"""
    
    run_git_command("git add .", "Fayllar qo‘shildi (staged)", "green")

    # Endi git status (faqat staging uchun)
    run_git_command("git diff --cached", "Commit qilinadigan o‘zgarishlar", "yellow")

    # So‘ng git status (agar xohlasangiz)
    run_git_command("git status", "Git holati", "cyan")

    # AIC orqali commit xabarini olish
    aic_commit = run_git_command("aic", "AI asosidagi commit xabari", "bright_yellow")

    # Git commit
    run_git_command(f'git commit -m "{aic_commit}"', "Commit bajarildi", "bright_yellow")

    # Branch nomini olish
    branch_name = subprocess.check_output("git branch --show-current", shell=True).decode().strip()

    # Git push
    run_git_command(f"git push origin {branch_name}", f"{branch_name} branchiga push qilinmoqda", "blue")


if __name__ == "__main__":
    aic()
