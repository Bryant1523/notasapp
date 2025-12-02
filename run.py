import streamlit.web.cli as stcli
import sys
import os

def resolve_path(path):
    if getattr(sys, 'frozen', False):
        application_path = sys._MEIPASS
    else:
        application_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(application_path, path)

if __name__ == '__main__':
    main_script_path = resolve_path("app.py") 
    
    sys.argv = [
        "streamlit",
        "run",
        main_script_path,
        "--global.developmentMode=false",
        "--server.headless=true",
        "--server.port=8501"
    ]
    
    sys.exit(stcli.main())