import streamlit as st

st.set_page_config(
    page_title="QRコードアプリ",
    page_icon="🔍",
    layout="wide"
)

st.title("QRコードアプリ")

st.markdown("""
## 機能一覧

1. **QRコード生成** 📱
   - CSVファイルから商品QRコードを一括生成
   - Excel形式でエクスポート可能
   - ZIP形式でQRコード画像をダウンロード

2. **QRコードリーダー** 🎥
   - カメラでQRコードを読み取り
   - URLを自動検出
   - 商品ページへ直接アクセス

サイドバーのメニューから使用したい機能を選択してください。
""")

st.sidebar.success("上記の機能から選択してください。")
