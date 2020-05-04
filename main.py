# extract_doc_info.py

from PyPDF2 import PdfFileReader, PdfFileWriter
from PIL import Image
import os


def extract_information(pdf_path):
    with open(pdf_path, 'rb') as f:
        pdf = PdfFileReader(f)
        information = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()

    txt = f"""
    Information about {pdf_path}: 

    Author: {information.author}
    Creator: {information.creator}
    Producer: {information.producer}
    Subject: {information.subject}
    Title: {information.title}
    Number of pages: {number_of_pages}
    """

    print(txt)
    return information


def merge_pdfs(paths, output):
    pdf_writer = PdfFileWriter()
    for path in paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            # Add each page to the writer object
            pdf_writer.addPage(pdf_reader.getPage(page))

        # Write out the merged PDF
    with open(output, 'wb') as out:
        pdf_writer.write(out)


def convert_to_pdf(files, path):
    images = list()
    for file in files:
        image1 = Image.open(file)
        im1 = image1.convert('RGB')
        im1.save(path+"/"+file.split("/")[-1][0:-4]+".pdf")
        images.append(im1)



if __name__ == '__main__':
    # path = '/home/vahid/Documents/Steuer_Docs/2019/to_print/04105_BetriebsKosten.pdf'
    # extract_information(path)
    path = '/home/vahid/Development/Python/Scanner/output_image'
    img_files = [path + "/" + x for x in os.listdir(path) if x.endswith(".jpg")]
    pdf_images = convert_to_pdf(img_files, path)
    #pdf_files = [path + "/" + x for x in os.listdir(path) if x.endswith(".pdf")]

    #merge_pdfs(pdf_files, output=path+'/merged.pdf')
