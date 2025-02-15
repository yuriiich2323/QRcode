import streamlit as st
import base64

def get_csv_download_link():
    csv_content = """ProductName,ProductUrl
Product A,example.com/productA
Product B,example.com/productB
Product C,example.com/productC"""
    
    b64 = base64.b64encode(csv_content.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="template.csv">CSVテンプレートをダウンロード</a>'
    return href

st.set_page_config(
    page_title="QRコード生成アプリ",
    page_icon="📱",
    layout="wide"
)

st.title("QRコード生成アプリ")

st.markdown("""
## 機能紹介

このアプリでは、商品情報のCSVファイルからQRコードを一括生成することができます。

### 使用方法

1. **CSVファイルの準備**
   - 以下のテンプレートをダウンロードして編集してください：
""")

st.markdown(get_csv_download_link(), unsafe_allow_html=True)

st.markdown("""
   - CSVファイルの形式：
   ```
   ProductName,ProductUrl
   Product A,example.com/productA
   Product B,example.com/productB
   ```
   - 1列目（ProductName）：商品名
   - 2列目（ProductUrl）：商品のURL（http://やhttps://は自動で追加されます）

2. **QRコード生成**
   - サイドバーの「QRコード生成」をクリック
   - 「CSVファイルをアップロード」ボタンからファイルを選択
   - アップロード後、自動的にQRコードが生成されます

3. **出力形式**
   - **ZIP形式**: 各QRコードが個別のPNGファイルとして保存
   - **Excel形式**: 商品名、URL、QRコードが一覧表として保存

### 出力ファイルについて

1. **ZIPファイル (product_qrcodes.zip)**
   - 各商品のQRコードが個別の画像ファイルとして保存
   - ファイル名は「商品名_qr.png」の形式

2. **Excelファイル (products_with_qr.xlsx)**
   - ProductName（商品名）
   - ProductUrl（URL）
   - QRコード画像
   が一覧表として保存されます

### 注意事項
- CSVファイルの列名は必ず「ProductName」と「ProductUrl」にしてください
- URLは有効なものを指定してください
- 商品名は日本語でも英語でも使用可能です
""")

st.sidebar.success("「QRコード生成」をクリックして開始してください。")
