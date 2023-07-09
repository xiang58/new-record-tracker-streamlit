import streamlit as st
from datetime import date

import widgets as wd

def main():
    if 'current_date' not in st.session_state:
        st.session_state['current_date'] = date.today()

    wd.show_last_date()
    wd.show_score()
    wd.show_circle(st.session_state['current_date'])
    wd.show_insert_new_rec()
    wd.get_chart_54456624()

if __name__ == '__main__':
    main()
