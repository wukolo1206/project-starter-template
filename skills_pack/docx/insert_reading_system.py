import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
from lxml import etree

W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
W14 = 'http://schemas.microsoft.com/office/word/2010/wordml'

def w(tag): return f'{{{W}}}{tag}'
def w14(tag): return f'{{{W14}}}{tag}'

def make_para(text, color='555555', sz=18, bold=False):
    p = etree.Element(w('p'))
    p.set(w14('paraId'), '0A001001')
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
    if bold:
        etree.SubElement(rPr, w('b'))
    col = etree.SubElement(rPr, w('color'))
    col.set(w('val'), color)
    size = etree.SubElement(rPr, w('sz'))
    size.set(w('val'), str(sz))
    lang2 = etree.SubElement(rPr, w('lang'))
    lang2.set(w('eastAsia'), 'zh-TW')
    t = etree.SubElement(r, w('t'))
    t.text = text
    if text.startswith(' '):
        t.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
    return p

def make_cell(text, width, fill=None, bold=False, sz=18, color='000000', center=False):
    tc = etree.Element(w('tc'))
    tcPr = etree.SubElement(tc, w('tcPr'))
    tcW = etree.SubElement(tcPr, w('tcW'))
    tcW.set(w('w'), str(width))
    tcW.set(w('type'), 'dxa')
    if fill:
        shd = etree.SubElement(tcPr, w('shd'))
        shd.set(w('val'), 'clear')
        shd.set(w('color'), 'auto')
        shd.set(w('fill'), fill)
    va = etree.SubElement(tcPr, w('vAlign'))
    va.set(w('val'), 'center')

    p = etree.SubElement(tc, w('p'))
    p.set(w14('paraId'), '0A001010')
    p.set(w14('textId'), '77777777')
    pPr = etree.SubElement(p, w('pPr'))
    sp = etree.SubElement(pPr, w('spacing'))
    sp.set(w('before'), '40')
    sp.set(w('after'), '40')
    if center:
        jc = etree.SubElement(pPr, w('jc'))
        jc.set(w('val'), 'center')

    r = etree.SubElement(p, w('r'))
    rPr = etree.SubElement(r, w('rPr'))
    if bold:
        etree.SubElement(rPr, w('b'))
    col = etree.SubElement(rPr, w('color'))
    col.set(w('val'), color)
    size = etree.SubElement(rPr, w('sz'))
    size.set(w('val'), str(sz))
    t = etree.SubElement(r, w('t'))
    t.text = text
    if text.startswith(' ') or text.endswith(' '):
        t.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
    return tc

def make_row(cells_data, widths, fill=None, bold=False, sz=18, color='000000'):
    tr = etree.Element(w('tr'))
    tr.set(w14('paraId'), '0A001020')
    tr.set(w14('textId'), '77777777')
    trPr = etree.SubElement(tr, w('trPr'))
    jc = etree.SubElement(trPr, w('jc'))
    jc.set(w('val'), 'center')
    for text, width in zip(cells_data, widths):
        tc = make_cell(text, width, fill=fill, bold=bold, sz=sz, color=color)
        tr.append(tc)
    return tr

# 欄寬
WIDTHS = [1500, 800, 1000, 1500, 3930]
HEADERS = ['文本', '類型', '認知歷程', '教學策略', '學生常見迷思']

ROWS = [
    ['小光與雜貨店', '記敘文', '提取訊息', '找出重點句', '簡單題，若錯代表未看完全文'],
    ['小光與雜貨店', '記敘文', '推論訊息', '小偵探找原因', '文中未明說「愧疚」，需從行為推論'],
    ['小光與雜貨店', '記敘文', '詮釋整合', '人物放大鏡', '選項具誘答性，需歸納核心價值'],
    ['馬與驢子', '記敘文', '推論訊息', '玩拼圖找因果', '需因果推論，文中未直說「因為太重」'],
    ['馬與驢子', '記敘文', '詮釋整合', '小偵探找原因', '需整合全文提煉核心道理（主旨整合）'],
]

def make_table():
    tbl = etree.Element(w('tbl'))
    tblPr = etree.SubElement(tbl, w('tblPr'))
    tblStyle = etree.SubElement(tblPr, w('tblStyle'))
    tblStyle.set(w('val'), 'aff2')
    tblW = etree.SubElement(tblPr, w('tblW'))
    tblW.set(w('w'), '0')
    tblW.set(w('type'), 'auto')
    jc = etree.SubElement(tblPr, w('jc'))
    jc.set(w('val'), 'center')

    tblGrid = etree.SubElement(tbl, w('tblGrid'))
    for ww in WIDTHS:
        gc = etree.SubElement(tblGrid, w('gridCol'))
        gc.set(w('w'), str(ww))

    # 表頭
    header_row = make_row(HEADERS, WIDTHS, fill='1F5C8B', bold=True, sz=18, color='FFFFFF')
    tbl.append(header_row)

    # 資料列
    for i, row_data in enumerate(ROWS):
        fill = 'EEF4FF' if i % 2 == 0 else 'F8F8F8'
        data_row = make_row(row_data, WIDTHS, fill=fill, sz=18)
        tbl.append(data_row)

    return tbl

# ===== 主程式 =====
tree = etree.parse('unpacked_2-3/word/document.xml')
body = tree.find(f'{{{W}}}body')
children = list(body)

# 找 child[49]（URL段落）的index
target_idx = 49

# 建立要插入的元素
new_elements = []

# 1. 小標題
new_elements.append(make_para(
    '▌ 系統架構說明：試題逐題分析 ＋ AI 擴充學習遷移題庫',
    color='555555', sz=18
))

# 2. 說明文字
new_elements.append(make_para(
    '　　系統將108–114年三至六年級篩選測驗閱讀題逐題標記認知歷程與教學策略，並診斷學生常見迷思。教師可依此精準選題，對應「找→連→說」三步驟進行差異化教學。以下為三年級題目分析舉例：',
    color='333333', sz=18
))

# 3. 表格
new_elements.append(make_table())

# 4. 題庫規模說明
new_elements.append(make_para(
    '　　系統收錄 108–114 年三至六年級閱讀測驗考古題 195 道，搭配 AI 擴充高品質學習遷移題目 585 道，共計 780 題。',
    color='333333', sz=18
))

# 5. 來源檔案
new_elements.append(make_para(
    '  【來源檔案】附件2-4\\其他附件資料\\學習扶助閱讀測驗試題分析_全新修正版.xlsx　/　04_差異化學習單_馬與驢子.xlsx',
    color='555555', sz=18
))

# 插入在 child[49] 之後（即 child[50] 之前）
insert_pos = target_idx + 1
for i, elem in enumerate(new_elements):
    body.insert(insert_pos + i, elem)

# 儲存
with open('unpacked_2-3/word/document.xml', 'w', encoding='utf-8') as f:
    f.write(etree.tostring(tree, encoding='unicode', xml_declaration=False))
print('完成！已在閱讀系統URL之後插入說明段落和表格。')
