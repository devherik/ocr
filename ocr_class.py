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
    
    def buscar_texto_em_imagem(self, imagem_path: str, texto: str) -> bool:
        print(f'--- Iniciando busca por palavra no arquivo {imagem_path} ---')
        imagem = cv2.cvtColor(cv2.imread(imagem_path), cv2.COLOR_BGR2GRAY)
        texto_encontrado = self.__ocr.image_to_string(imagem)
        print(f'Texto encontrado: {texto_encontrado}')
        print(f'Texto procurado: {texto}')
        return True if texto.strip().lower() == texto_encontrado.strip().lower() else False
        
    def buscar_texto_em_tela(self, texto: str) -> bool:
        print('--- Iniciando busca por palavra ---')
        self.tirar_screenshot('screenshot.png')
        imagem = cv2.imread('screenshot.png')
        imagem_gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        texto_encontrado = self.__ocr.image_to_string(imagem_gray)
        return True if texto == texto_encontrado else False
    
    def tirar_screenshot(self, nome_arquivo: str) -> str:
        print('Tirando screenshot')
        try:
            imagem = self.__automation.screenshot(region=(0, 0, 1920, 1080))
        except Exception as e:
            print(f'Erro ao tirar screenshot: {e}')
            return None
        imagem.save(nome_arquivo)
        print(f'Screenshot salva como {nome_arquivo}')
        return nome_arquivo
    
    def pegar_resolucao(self) -> tuple:
        print('--- Pegando resolução da tela ---')
        return self.__automation.size()