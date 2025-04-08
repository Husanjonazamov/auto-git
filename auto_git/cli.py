import subprocess
from termcolor import colored


def run_git_command(command, description=None, style="white", print_output=True):
    """Git komandalarni bajarish va natijasini qaytarish"""
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if description:
        print(colored(f"\n{' ' + description + ' ':─^100}", style))

    output = stdout.decode("utf-8").strip()
    error = stderr.decode("utf-8").strip()

    if print_output:
        if output:
            print(colored(output, style))
        if error:
            print(colored(error, "red"))

    return output


def aic():
    """Auto Git: add → AI commit → push"""
    run_git_command("git add .", "Fayllar qo‘shildi (staged)", "green")

    run_git_command("git diff --cached", "Commit qilinadigan o‘zgarishlar", "yellow")

    aic_commit = run_git_command("aic", "AI asosidagi commit xabari", "cyan")

    aic_commit = aic_commit.strip("`'\" ").splitlines()[0]  # faqat 1-qator

    if not aic_commit:
        print(colored("❌ AI commit xabari olinmadi!", "red"))
        return

    run_git_command(f'git commit -m "{aic_commit}"', "Commit bajarildi", "magenta")

    run_git_command("git push origin main", "main branchiga push qilinmoqda", "blue")

    print(colored("\n✅ Hammasi muvaffaqiyatli yakunlandi!", "green"))
