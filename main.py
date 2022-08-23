import pyttsx3
import PyPDF2
def money():
    book1 = open('wise.pdf', 'rb')
    pdfReader1 = PyPDF2.PdfFileReader(book1)
    pages1 = pdfReader1.numPages
    print(pages1)
    speaker1 = pyttsx3.init()
    for num in range(8, pages1):
        page1 = pdfReader1.getPage(num)
        text = page1.extractText()
        speaker1.say(text)
        speaker1.runAndWait()
    book1.close()

def pre():
    book2 = open('present.pdf', 'rb')
    pdfReader2 = PyPDF2.PdfFileReader(book2)
    pages2 = pdfReader2.numPages

    speaker2 = pyttsx3.init()
    for num in range(9, pages2):
        page2 = pdfReader2.getPage(num)
        text2 = page2.extractText()
        speaker2.say(text2)
        speaker2.runAndWait()
    book2.close()

def atomic():
    book3 = open('essay.pdf', 'rb')
    pdfReader3 = PyPDF2.PdfFileReader(book3)
    pages3 = pdfReader3.numPages
    print(pages3)
    speaker3 = pyttsx3.init()
    for num in range(0, pages3):
        page3 = pdfReader3.getPage(num)
        text3 = page3.extractText()
        speaker3.say(text3)
        speaker3.runAndWait()
    book3.close()

def japan():
    book4 = open('maketime.pdf', 'rb')
    pdfReader4 = PyPDF2.PdfFileReader(book4)
    pages4 = pdfReader4.numPages
    print(pages4)
    speaker4 = pyttsx3.init()
    for num in range(13, pages4):
        page4 = pdfReader4.getPage(num)
        text4 = page4.extractText()
        speaker4.say(text4)
        speaker4.runAndWait()
    book4.close()


if __name__ == '__main__':
    print("Available audiobooks:\n\t1.The P2sychology of Money by Morgan Housel\n\t2.Presentation Secrets of Steve Jobs\n\t3.Atomic Habits\n\t4.Ikigai-the-japanese-secret-to-a-long-and-happy-life")
    print("\nEnter the audiobook no: ")
    a=int(input())
    if(a==1):
        money()
    elif(a==2):
        pre()
    elif(a==3):
        atomic()
    elif(a==4):
        japan()
