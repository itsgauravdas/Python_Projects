import subprocess

def webauto():
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    URLS = [
        "https://stackoverflow.com",
        "https://github.com/avinashkranjan",
        "https://gmail.com",
        "https://google.co.in",
        "https://youtube.com",
    ]

    for url in URLS:
        print(f"Opening: {url}")
        try:
            subprocess.Popen([chrome_path, url])
        except FileNotFoundError:
            print(f"Chrome not found at: {chrome_path}")
            break

webauto()
