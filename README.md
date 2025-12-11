# PNG 文字轉文字檔工具

這個專案提供一個簡單的指令工具，能將包含文字的 PNG 圖片透過 OCR 轉換成純文字 (`.txt`) 檔案。

## 安裝需求

1. 安裝 [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)。在 Debian/Ubuntu 可使用：
   ```bash
   sudo apt-get update && sudo apt-get install tesseract-ocr
   ```
2. 安裝 Python 套件：
   ```bash
   pip install -r requirements.txt
   ```

## 使用方式

```bash
python png_to_txt.py <圖片路徑.png> [-o 輸出檔案路徑.txt]
```

- 若未指定 `-o`，文字檔會與圖片放在同一路徑並使用 `.txt` 副檔名。
- 產出的文字檔末尾會自動補上換行，方便直接閱讀或串接其他指令。

## 範例

```bash
python png_to_txt.py example.png
# -> 會產生 example.txt 並印出存檔位置
```
