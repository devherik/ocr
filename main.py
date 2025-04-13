import ocr_class
def main():
    ocr = ocr_class.Ocr()
    if ocr.buscar_texto_em_tela('No results.'):
        print('Texto encontrado na imagem')
    else:
        print('Texto não encontrado na imagem')
    
if __name__ == "__main__":
    main()