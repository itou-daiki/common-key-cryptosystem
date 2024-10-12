import streamlit as st

def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

st.set_page_config(page_title="シーザー暗号体験", layout="wide")

st.title("シーザー暗号体験")

tab1, tab2, tab3 = st.tabs(["鍵生成", "暗号化", "復号"])

with tab1:
    st.subheader("鍵生成")
    st.write("シーザー暗号では、シフト値を鍵として使用します。")
    st.write("1から25までの数字をシフト値（鍵）として選んでください。")

    shift = st.number_input("シフト値（1-25）を入力してください：", min_value=1, max_value=25, value=3, key="key_gen")

    st.success(f"生成された鍵（シフト値）は：{shift}")
    st.write("この鍵を覚えておいてください。暗号化と復号の両方で必要になります。")

with tab2:
    st.subheader("暗号化")
    
    plaintext = st.text_input("暗号化したいテキストを入力してください：")
    shift_encrypt = st.number_input("シフト値（鍵）を入力してください：", min_value=1, max_value=25, value=3, key="encrypt")

    if st.button("暗号化実行"):
        if plaintext:
            encrypted_text = caesar_encrypt(plaintext, shift_encrypt)
            st.success("暗号化されたテキスト：")
            st.write(encrypted_text)
        else:
            st.error("暗号化するテキストを入力してください。")

with tab3:
    st.subheader("復号")

    ciphertext = st.text_input("復号したい暗号文を入力してください：")
    shift_decrypt = st.number_input("シフト値（鍵）を入力してください：", min_value=1, max_value=25, value=3, key="decrypt")

    if st.button("復号実行"):
        if ciphertext:
            decrypted_text = caesar_decrypt(ciphertext, shift_decrypt)
            st.success("復号されたテキスト：")
            st.write(decrypted_text)
        else:
            st.error("復号するテキストを入力してください。")