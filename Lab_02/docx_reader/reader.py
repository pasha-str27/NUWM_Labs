import docx

document = docx.Document("DockerBasics.docx")
text = []
for paragraph in document.paragraphs:
    print(paragraph.text)