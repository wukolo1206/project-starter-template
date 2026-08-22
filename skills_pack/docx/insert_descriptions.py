import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
from lxml import etree

W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
W14 = 'http://schemas.microsoft.com/office/word/2010/wordml'

def w(tag): return f'{{{W}}}{tag}'
def w14(tag): return f'{{{W14}}}{tag}'

def make_desc(text, pid):
    p = etree.Element(w('p'))
    p.set(w14('paraId'), pid)
    p.set(w14('textId'), '77777777')
    pPr = etree.SubElement(p, w('pPr'))
    sp = etree.SubElement(pPr, w('spacing'))
    sp.set(w('before'), '40')
    sp.set(w('after'), '40')
    rPr_p = etree.SubElement(pPr, w('rPr'))
    lang = etree.SubElement(rPr_p, w('lang'))
    lang.set(w('eastAsia'), 'zh-TW')

    r = etree.SubElement(p, w('r'))
    rPr = etree.SubElement(r, w('rPr'))
    col = etree.SubElement(rPr, w('color'))
    col.set(w('val'), '333333')
    sz = etree.SubElement(rPr, w('sz'))
    sz.set(w('val'), '18')
    lang2 = etree.SubElement(rPr, w('lang'))
    lang2.set(w('eastAsia'), 'zh-TW')
    t = etree.SubElement(r, w('t'))
    t.text = text
    if text.startswith('　'):
        t.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
    return p

tree = etree.parse('unpacked_2-3/word/document.xml')
body = tree.find(f'{{{W}}}body')
children = list(body)

desc1 = make_desc(
    '　　本系統為自製教師備課工具，可依年級與類別（字音、字形、字義）快速篩選108–114年篩選測驗歷屆考題，投影講義模式支援課堂即時互動，有效縮短備課時間，並精準診斷學生形近字與字義弱點。',
    '0B001101'
)

desc2 = make_desc(
    '　　本系統整合168道歷年篩選測驗句段真題，依句序排列、刪除贅字、文意通順等六大類型建置差異化互動練習。教師可依學生弱點逐一指派任務，系統即時批改並回傳全班錯題分布，協助掌握教學優先順序。',
    '0B001201'
)

# 從下往上插入，避免 index 偏移影響上方插入點
# ② 學扶句段：child[41] 後面插入
body.insert(42, desc2)
print('已在 child[41]（② 學扶句段）後插入說明文字')

# ① 字音形：child[37] 後面插入（② 已插，不影響 37）
body.insert(38, desc1)
print('已在 child[37]（① 字音形系統）後插入說明文字')

with open('unpacked_2-3/word/document.xml', 'w', encoding='utf-8') as f:
    f.write(etree.tostring(tree, encoding='unicode', xml_declaration=False))
print('完成！')
