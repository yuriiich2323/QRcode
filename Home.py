import streamlit as st

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
   - 以下の形式でCSVファイルを作成してください：
   ```
   商品名,URL
   商品A,example.com/productA
   商品B,example.com/productB
   ```
   - 1列目：商品名
   - 2列目：商品のURL（http://やhttps://は自動で追加されます）

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
   - 商品名
   - URL
   - QRコード画像
   が一覧表として保存されます

### 注意事項
- CSVファイルは必ず「商品名」と「URL」の2列で作成してください
- URLは有効なものを指定してください
- 日本語の商品名も使用可能です
""")

st.sidebar.success("「QRコード生成」をクリックして開始してください。")
