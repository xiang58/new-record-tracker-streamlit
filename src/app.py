import streamlit as st
from datetime import date

import widgets as wd

def main():
    if 'current_date' not in st.session_state:
        st.session_state['current_date'] = date.today()

    wd.show_last_date()
    wd.show_circle(st.session_state['current_date'])
    wd.show_insert_new_rec(st.session_state['current_date'])
    wd.show_date_heatmap()

if __name__ == '__main__':
    main()
