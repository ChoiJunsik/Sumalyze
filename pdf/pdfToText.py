from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
from django.conf import settings
def convert_pdf_to_txt(fileName):
    #pdf리소스 매니저 객체 생성
    rsrcmgr = PDFResourceManager()
    #문자열 데이터를 파일처럼 처리하는 stringio -> pdf 파일 내용이 여기 담김
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(fileName, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()
 
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)
    #text에 결과가 담김
    text = retstr.getvalue()
    text = ' '.join(text.strip().split('\n'))


    # file = open('C:\sumalyze\media\\'+fileName+'.txt', 'w',-1, "utf-8") # 파일 열기
    # file.write(text)
    # file.close() # 파일 닫기

    fp.close()
    device.close()
    retstr.close()
    return text
