from nbconvert import HTMLExporter
import nbformat

exporter = HTMLExporter()
notebook = nbformat.read('ИО ДЗ-5 ИУ5-61Б Кашима.ipynb', as_version=4)
body, _ = exporter.from_notebook_node(notebook)

with open('ИО ДЗ-5 ИУ5-61Б Кашима.html', 'w', encoding='utf-8') as f:
    f.write(body)

print("Open output.html in browser and use Print > Save as PDF")