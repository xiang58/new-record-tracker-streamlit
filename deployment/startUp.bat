@echo OFF
cd ..
pipenv install
pipenv run streamlit run app.py
