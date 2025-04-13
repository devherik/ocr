import ocr_class
def main():
    ocr = ocr_class.Ocr()
    ocr.tirar_screenshot('test.png')
    
if __name__ == "__main__":
    main()