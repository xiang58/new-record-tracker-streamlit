from datetime import date

import streamlit as st

import helper
import widgets as wd


def main():
    if 'current_date' not in st.session_state:
        st.session_state['current_date'] = date.today()

    all_recs = helper.get_all_recs()
    wd.show_last_date(all_recs)
    wd.show_circle(all_recs, st.session_state['current_date'])
    wd.show_insert_new_rec(all_recs, st.session_state['current_date'])
    wd.show_date_heatmap(all_recs)
    
    
if __name__ == '__main__':
    main()
