import streamlit as st
from classify_group import get_name_group, get_file_group

options = get_name_group(r"C:\Users\KNT21617\Downloads\OneDrive_1_1-30-2024\トライアル①②\New folder")
options.insert(0, 'Select All')
add_button = st.button("Add")
new_option = st.text_input("Add new group:")
if new_option and new_option not in options:
    options.append(new_option)

selected_options = st.multiselect(
    'What are your group',
    options,
    placeholder="Choose group"
)
if 'Select All' in selected_options:
    selected_options = options[1:]
    st.info("All options selected.")

# st.write('You selected:', selected_options)
end_list = get_file_group(selected_options)
st.write(end_list)
