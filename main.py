import ocr_class
def main():
    ocr = ocr_class.Ocr()
    print(ocr.pegar_resolucao())
    if ocr.buscar_texto_em_tela('Reddit'):
        print('Texto encontrado na tela')
    else:
        print('Texto não encontrado na tela')
    
if __name__ == "__main__":
    main()