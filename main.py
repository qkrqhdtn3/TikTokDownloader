from flask import Flask
from atexit import register
from pathlib import Path
from rich.console import Console

GENERAL = "b black"
PROMPT = "b black"

class ColorfulConsole(Console):
    def print(self, *args, style=GENERAL, highlight=False, **kwargs):
        super().print(*args, style=style, highlight=highlight, **kwargs)

    def input(self, prompt_="", *args, **kwargs):
        return super().input(
            f"[{PROMPT}]{prompt_}[/{PROMPT}]", *args, **kwargs)
    
class Downloader:
    PROJECT_ROOT = Path('.').resolve().parent

    def __init__(self):
        self.console = ColorfulConsole()
        self.running = True
##        self.register = 

    def run(self):
        self.menu()
            
    def menu(self, menuNum="0"):
        while self.running:
            menuNum = self.prompt(
                "TikTokDownloader",
                [
                "Link",
                "Login",
                "Quit"
                ],
                self.console
                )
            self.selectMenuNum(menuNum)
            menuNum = "0"

    def prompt(self, title: str, contentList: list, console):
        printConsole = f"{title}\n"
        for i, j in enumerate(contentList):
            printConsole += f"{i + 1} {j}\n"
        return console.input(printConsole)

    def selectMenuNum(self, menuNum: str):
        if menuNum == "1":
            self.link()
        elif menuNum == "2":
            self.login()
        elif menuNum == "3":
            self.quit()

    def link(self):
        self.console.print("link\n")
    def login(self):
        self.console.print("login\n")
    def quit(self):
        self.console.print("quit\n")
    
app = Flask(__name__)

@app.route('/')
def home():
    return 'TikTokDownloader'

if __name__ == '__main__':
##    app.run(debug=True)
    Downloader().run()
