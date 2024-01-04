@echo OFF
cd ..
if not exist ".venv" (
    py -m venv .venv && py -m pip install -r requirements.txt
)
.venv\Scripts\activate && streamlit run app.py
