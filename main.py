import ocr_class
def main():
    ocr = ocr_class.Ocr()
    ocr.mapear_tela(ocr.tirar_screenshot('screenshot.png', 0, 0, ocr.resolucao[0], ocr.resolucao[1]))
    
if __name__ == "__main__":
    main()