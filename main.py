from flask import Flask
from atexit import register
from pathlib import Path

class Downloader:
    PROJECT_ROOT = Path('.').resolve().parent

##    def __init__(self):


app = Flask(__name__)

@app.route('/')
def home():
    return 'TikTokDownloader'

if __name__ == '__main__':
    app.run(debug=True)
