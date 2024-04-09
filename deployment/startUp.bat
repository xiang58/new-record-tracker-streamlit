@echo OFF
cd ..
if not exist ".venv" (
    py -m venv .venv
)
.venv\Scripts\activate && pip install -r requirements.txt && streamlit run src\app.py
