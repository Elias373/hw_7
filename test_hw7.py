import zipfile
import os
import pandas as pd
from pypdf import PdfReader



def test_create_archive():
    if not os.path.exists('resources'):  # проверяем существует ли папка
        os.mkdir('resources')  # создаем папку если её нет
    with zipfile.ZipFile('resources/7.zip', 'w') as zf:  # создаем архив
        for file in ['sample.pdf', 'file_example_XLSX_10.xlsx', 'file_example.csv']:  # добавляем файлы в архив
            add_file = os.path.join('docs', file)  # склеиваем путь к файлам которые добавляют в архив
            zf.write(add_file, os.path.basename(add_file))  # добавляем файл в архив


def test_check_archive_content_pdf():
    with zipfile.ZipFile("resources/7.zip", "r") as zip_:
         with zip_.open("sample.pdf") as pdf_file:
            reader = PdfReader(pdf_file)
            pdf_text = ""
            for page in reader.pages:
                pdf_text += page.extract_text() or ""
            print('PDF File:')
            print(pdf_text)

            assert 'Fun fun fun' in pdf_text



def test_check_archive_content_xls():
    with zipfile.ZipFile('resources/7.zip', 'r') as zip_:
        with zip_.open("file_example_XLSX_10.xlsx") as xls_file:
            df = pd.read_excel(xls_file)
            print('Exel Table:')
            print(df)

            assert df['First Name'].iloc[6] == 'Etta'





def test_check_archive_content_csv():
    with zipfile.ZipFile('resources/7.zip', 'r') as zip_:
        with zip_.open("file_example.csv") as csv_file:
            df = pd.read_csv(csv_file)
            print ('CSV Table:')
            print(df)

            assert df['Item'].iloc[42] == 'Other'









