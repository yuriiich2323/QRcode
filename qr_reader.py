import streamlit as st
import cv2
import numpy as np
from urllib.parse import urlparse
import validators

def is_valid_url(url):
    try:
        return validators.url(url)
    except:
        return False

def main():
    st.title("QRコードリーダー")
    
    # アプリの状態管理
    if 'url_detected' not in st.session_state:
        st.session_state.url_detected = False
    
    # カメラの設定
    camera = cv2.VideoCapture(0)
    qr_detector = cv2.QRCodeDetector()
    
    # カメラフレームの表示用プレースホルダー
    frame_placeholder = st.empty()
    result_placeholder = st.empty()
    
    while not st.session_state.url_detected:
        ret, frame = camera.read()
        if not ret:
            st.error("カメラの起動に失敗しました。カメラへのアクセスを許可してください。")
            break
            
        # フレームをRGBに変換
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # QRコードの検出
        retval, decoded_info, points, _ = qr_detector.detectAndDecodeMulti(frame)
        
        if retval and len(decoded_info) > 0:
            qr_data = decoded_info[0]
            if is_valid_url(qr_data):
                st.session_state.url_detected = True
                result_placeholder.markdown(f"""
                    ### QRコードを検出しました！
                    URL: {qr_data}
                    
                    [商品ページへ移動]({qr_data})
                """)
                camera.release()
                break
            else:
                result_placeholder.warning("無効なURLが含まれているQRコードです。")
        
        # フレームの表示
        frame_placeholder.image(frame_rgb)
    
    # スキャンを再開するボタン
    if st.session_state.url_detected:
        if st.button("スキャンを再開"):
            st.session_state.url_detected = False
            st.experimental_rerun()

if __name__ == "__main__":
    st.set_page_config(page_title="QRコードリーダー")
    main()
