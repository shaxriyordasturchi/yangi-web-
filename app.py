def main():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "username" not in st.session_state:
        st.session_state.username = ""
    if "page" not in st.session_state:
        st.session_state.page = "Bosh sahifa"

    if not st.session_state.logged_in:
        login.app()
    else:
        st.sidebar.title(f"Xush kelibsiz, {st.session_state.username}!")
        page_list = ["Bosh sahifa", "Admin", "Lab 1 - WDM", "Lab 2 - OCDMA", "Lab 3 - PON"]
        page = st.sidebar.selectbox("Sahifa tanlang", page_list,
                                    index=page_list.index(st.session_state.page))
        st.session_state.page = page

        if page == "Bosh sahifa":
            st.title("🏠 Bosh sahifa")
            st.write("Bu asosiy sahifa yoki foydalanuvchi paneli.")
            if st.button("Keyingi sahifaga o‘tish (Lab 1 - WDM)"):
                st.session_state.page = "Lab 1 - WDM"
                st.experimental_rerun()
            if st.button("Chiqish"):
                st.session_state.logged_in = False
                st.session_state.username = ""
                st.session_state.page = "Bosh sahifa"
                st.experimental_rerun()
        elif page == "Admin":
            admin.app()
        elif page == "Lab 1 - WDM":
            lab1_wdm.app()
        elif page == "Lab 2 - OCDMA":
            lab2_ocdma.app()
        elif page == "Lab 3 - PON":
            lab3_pon.app()

if __name__ == "__main__":
    main()
