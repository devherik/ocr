import pyautogui
import cv2
import pytesseract
import time
from PIL import Image
from datetime import date, datetime


class Ocr():
    __instance = None

    def __new__(self):
        if self.__instance is None:
            self.__instance = super().__new__(self)
        return self.__instance

    def __init__(self) -> None:
        self.__ocr = pytesseract.pytesseract
        self.__automation = pyautogui
        self.resolucao = self.pegar_resolucao()
        self.__width = self.resolucao[0]
        self.__height = self.resolucao[1]

    def buscar_texto_em_imagem(self, imagem_path: str, texto: str) -> bool:
        print(f'--- Iniciando busca por palavra no arquivo {imagem_path} ---')
        imagem = cv2.cvtColor(cv2.imread(imagem_path), cv2.COLOR_BGR2GRAY)
        texto_encontrado = self.__ocr.image_to_string(imagem)
        print(f'Texto encontrado: {texto_encontrado}')
        print(f'Texto procurado: {texto}')
        return True if texto.strip().lower() == texto_encontrado.strip().lower() else False

    def buscar_texto_em_tela(self, texto: str) -> bool:
        print('--- Iniciando busca por palavra ---')
        self.tirar_screenshot('screenshot.png', 0, 0, self.resolucao[0], self.resolucao[1])
        imagem = cv2.imread('screenshot.png')
        imagem_gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        texto_encontrado = self.__ocr.image_to_string(imagem_gray)
        return True if texto == texto_encontrado else False

    def tirar_screenshot(self, nome_arquivo: str, x1: int, y1: int, x2: int, y2: int) -> None:
        print('Tirando screenshot')
        try:
            # tira um screenshot partindo dos pontos x1 e y2, somando à eles os valores x2 e y2
            imagem = self.__automation.screenshot(region=(x1, y1, x2, y2))
        except Exception as e:
            print(f'Erro ao tirar screenshot: {e}')
            return None
        imagem.save(nome_arquivo)
        print(f'Screenshot salva como {nome_arquivo}')

    def pegar_resolucao(self) -> tuple:
        print('--- Pegando resolução da tela ---')
        return self.__automation.size()

    def mapear_tela(self, qnt_quadrantes: int) -> None:
        print('--- Mapeando tela ---')
        time.sleep(2)
        mapa = []
        for r in range(qnt_quadrantes):
            mapa.append([])
            for c in range(qnt_quadrantes): mapa[r].append(c)
        # define o tamanho de cada quadrante
        quadrante_x = self.__width / qnt_quadrantes
        quadrante_y = self.__height / qnt_quadrantes
        # percorre a tela e divide em quadrantes
        for y in range(qnt_quadrantes):
            for x in range(qnt_quadrantes):
                x1 = int(x * quadrante_x)
                y1 = int(y * quadrante_y)
                x2 = int((x + 1) * quadrante_x)
                y2 = int((y + 1) * quadrante_y)
                # salva a imagem do quadrante
                self.tirar_screenshot(f'quadrante_{x}_{y}.png', x1, y1, int(quadrante_x), int(quadrante_y))
                # adiciona o quadrante ao mapa
                mapa[x][y] = (x1, y1, x2, y2)
                print(f'Quadrante {x}_{y} salvo como quadrante_{x}_{y}.png')
        print('--- Mapeamento concluído ---')
        
    def buscar_em_tela(self, texto: str, qnt_quadrantes: int) -> bool:
        print('--- Buscando texto em tela ---')
        time.sleep(2)
        mapa = []
        for r in range(qnt_quadrantes):
            mapa.append([])
            for c in range(qnt_quadrantes): mapa[r].append(c)
        # define o tamanho de cada quadrante
        quadrante_x = self.__width / qnt_quadrantes
        quadrante_y = self.__height / qnt_quadrantes
        # percorre a tela e divide em quadrantes
        for y in range(qnt_quadrantes):
            for x in range(qnt_quadrantes):
                x1 = int(x * quadrante_x)
                y1 = int(y * quadrante_y)
                x2 = int((x + 1) * quadrante_x)
                y2 = int((y + 1) * quadrante_y)
                # salva a imagem do quadrante
                self.tirar_screenshot(f'quadrante_{x}_{y}.png', x1, y1, int(quadrante_x), int(quadrante_y))
                # adiciona o quadrante ao mapa
                mapa[x][y] = (x1, y1, x2, y2)
                print(f'Quadrante {x}_{y} salvo como quadrante_{x}_{y}.png')