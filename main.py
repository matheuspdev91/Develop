from foundation.scanner import Scanner

scanner = Scanner()

documents = scanner.load(r"C:\Users\Matheus\Desktop\fitflix")


for document in documents:
    print("=" * 88)
    print(document.name)
    print(document.content[:300])