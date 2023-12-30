from flask import Flask
from atexit import register
from pathlib import Path
from rich.console import Console

GENERAL = "b bright_white"

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

    def run(self):
        while self.running:
            prompt(
                "1",
                "2",
                "3"
                )


app = Flask(__name__)

@app.route('/')
def home():
    return 'TikTokDownloader'

if __name__ == '__main__':
##    app.run(debug=True)
    Downloader().run()
