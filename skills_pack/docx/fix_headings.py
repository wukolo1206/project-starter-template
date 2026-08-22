import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
from lxml import etree

W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
def w(tag): return f'{{{W}}}{tag}'

tree = etree.parse('unpacked_2-3/word/document.xml')
ns = {'w': W}
body = tree.find('.//w:body', ns)
paras = body.findall('.//w:p', ns)

BLUE = '1F5C8B'
SZ = '24'  # 12pt = 24 half-points

count = 0
for p in paras:
    texts = p.findall('.//w:t', ns)
    line = ''.join(t.text or '' for t in texts)
    if not line.strip().startswith('▌'):
        continue

    # 修改段落層級的 rPr（pPr/rPr）
    pPr = p.find(w('pPr'), ns)
    if pPr is not None:
        rPr_p = pPr.find(w('rPr'), ns)
        if rPr_p is None:
            rPr_p = etree.SubElement(pPr, w('rPr'))
        # 設定顏色
        col = rPr_p.find(w('color'), ns)
        if col is None:
            col = etree.SubElement(rPr_p, w('color'))
        col.set(w('val'), BLUE)
        # 設定字級
        sz_el = rPr_p.find(w('sz'), ns)
        if sz_el is None:
            sz_el = etree.SubElement(rPr_p, w('sz'))
        sz_el.set(w('val'), SZ)

    # 修改所有 run 的 rPr
    for r in p.findall(w('r'), ns):
        rPr = r.find(w('rPr'), ns)
        if rPr is None:
            rPr = etree.SubElement(r, w('rPr'))
            r.insert(0, rPr)

        col = rPr.find(w('color'), ns)
        if col is None:
            col = etree.SubElement(rPr, w('color'))
        col.set(w('val'), BLUE)

        sz_el = rPr.find(w('sz'), ns)
        if sz_el is None:
            sz_el = etree.SubElement(rPr, w('sz'))
        sz_el.set(w('val'), SZ)

        szCs = rPr.find(w('szCs'), ns)
        if szCs is None:
            szCs = etree.SubElement(rPr, w('szCs'))
        szCs.set(w('val'), SZ)

    count += 1
    print(f'已修改: {line[:60]}')

with open('unpacked_2-3/word/document.xml', 'w', encoding='utf-8') as f:
    f.write(etree.tostring(tree, encoding='unicode', xml_declaration=False))

print(f'\n共修改 {count} 個 ▌ 小標題 → 12pt 藍色 #{BLUE}')
