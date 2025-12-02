import os
import sys
import webbrowser
from threading import Timer

def resolve_path(path):
    if getattr(sys, 'frozen', False):
        application_path = sys._MEIPASS
    else:
        application_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(application_path, path)

def open_browser():
    webbrowser.open("http://localhost:8501")

if __name__ == "__main__":
    from streamlit.web import cli as stcli

    main_script_path = resolve_path("app.py")
    
    Timer(2, open_browser).start()

    sys.argv = [
        "streamlit",
        "run",
        main_script_path,
        "--global.developmentMode=false",
        "--server.headless=true",
        "--server.port=8501",
        "--server.enableCORS=false"
    ]

    sys.exit(stcli.main())