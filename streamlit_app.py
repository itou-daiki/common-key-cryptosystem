import streamlit as st

def is_valid_input(text):
    return all(char.isalpha() and ord(char) < 128 for char in text)

def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        ascii_offset = 65 if char.isupper() else 97
        result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

st.set_page_config(page_title="共通鍵暗号体験（シーザー暗号体験）", layout="wide")

st.title("共通鍵暗号体験（シーザー暗号体験）")
st.write("")
st.subheader("ブラウザでシーザー暗号の「暗号化」→「復号」まで体験することができます")
st.write("")
st.subheader("シーザー暗号とは")
st.write("シーザー暗号は、古代ローマの将軍であるガイウス・ユリウス・カエサル（Julius Caesar）が使ったとされる暗号です。")
st.write("シーザー暗号は、アルファベットの文字を一定の数だけずらすことで暗号化を行います。")
st.write("例えば、シフト値が3の場合、A→D、B→E、C→F、...、X→A、Y→B、Z→C というように暗号化されます。")
st.write("この暗号化方法は、暗号化と復号の両方に同じシフト値を使う「共通鍵暗号」の一種です。")


tab1, tab2 = st.tabs([ "ステップ１：暗号化", "ステップ２：復号"])

with tab1:
    st.subheader("ステップ１：暗号化")
    
    plaintext = st.text_input("暗号化したいテキストを入力してください（半角アルファベットのみ）：")
    shift_encrypt = st.number_input("シフト値（鍵）を入力してください：", min_value=1, max_value=25, value=3, key="encrypt")

    if st.button("暗号化実行"):
        if plaintext:
            if is_valid_input(plaintext):
                encrypted_text = caesar_encrypt(plaintext, shift_encrypt)
                st.success("暗号化されたテキスト："+encrypted_text)
                st.subheader("「ステップ２：複号」タブに進み、暗号文を入力し、復号を行ってください")
            else:
                st.error("エラー：入力は半角アルファベット（A-Z, a-z）のみを使用してください。")
        else:
            st.error("暗号化するテキストを入力してください。")

with tab2:
    st.subheader("ステップ２：復号")

    ciphertext = st.text_input("復号したい暗号文を入力してください（半角アルファベットのみ）：")
    shift_decrypt = st.number_input("シフト値（鍵）を入力してください：", min_value=1, max_value=25, value=shift_encrypt, key="decrypt")

    if st.button("復号実行"):
        if ciphertext:
            if is_valid_input(ciphertext):
                decrypted_text = caesar_decrypt(ciphertext, shift_decrypt)
                st.success("復号されたテキスト："+decrypted_text)
            else:
                st.error("エラー：入力は半角アルファベット（A-Z, a-z）のみを使用してください。")
        else:
            st.error("復号するテキストを入力してください。")
