import pygame
import random
import sys
import serial
import time
from gtts import gTTS
import os
import threading

pygame.init()

# Definindo algumas cores
IMAGEM_X = 500
IMAGEM_Y = 350
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
MAGENTA = (250,128,114)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Definindo as configurações da janela
FPS = 60

palavra = ['0', '0', '0', '0', '0', '0']

# Inicializando o Pygame
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_width, screen_height = screen.get_size()
pygame.display.set_caption("Digite a Palavra")

# Carregando a fonte
font = pygame.font.Font("./fontes/Copyduck.ttf", 130)

# Carregando sons
acerto_som = pygame.mixer.Sound("./sons/correct.mp3")
erro_som = pygame.mixer.Sound("./sons/error.mp3")

# Lista de imagens
def load_and_scale_image(path, width, height):
    image = pygame.image.load(path)
    return pygame.transform.scale(image, (width, height))

image_banana = load_and_scale_image("./imagens/bananaa.png", IMAGEM_X, IMAGEM_Y)
image_sol = load_and_scale_image("./imagens/sool.png", IMAGEM_X, IMAGEM_Y)
image_cachorro = load_and_scale_image("./imagens/cachorro.png", IMAGEM_X, IMAGEM_Y)
image_gato = load_and_scale_image("./imagens/gato.png", IMAGEM_X, IMAGEM_Y)
image_carro = load_and_scale_image("./imagens/carro.png", IMAGEM_X, IMAGEM_Y)
image_lapis = load_and_scale_image("./imagens/lapis.png", IMAGEM_X, IMAGEM_Y)
image_bolas = load_and_scale_image("./imagens/bolas.png", IMAGEM_X, IMAGEM_Y)
image_radio = load_and_scale_image("./imagens/radio.png", IMAGEM_X, IMAGEM_Y)
image_amor = load_and_scale_image("./imagens/amor.png", IMAGEM_X, IMAGEM_Y)
image_comer = load_and_scale_image("./imagens/comer.png", IMAGEM_X, IMAGEM_Y)
image_nadar = load_and_scale_image("./imagens/nadar.png", IMAGEM_X, IMAGEM_Y)
image_casar = load_and_scale_image("./imagens/casar.png", IMAGEM_X, IMAGEM_Y)
image_pular = load_and_scale_image("./imagens/pular.png", IMAGEM_X, IMAGEM_Y)
image_rato = load_and_scale_image("./imagens/rato.png", IMAGEM_X, IMAGEM_Y)
image_linha = load_and_scale_image("./imagens/linha.png", IMAGEM_X, IMAGEM_Y)

# Lista de palavras e imagens
dicio = {
    "banana": image_banana,
    "sol": image_sol,
    "cachorro": image_cachorro,
    "gato": image_gato,
    "carro": image_carro,
    "lapis": image_lapis,
    "bolas": image_bolas,
    "radio": image_radio,
    "amor": image_amor,
    "comer": image_comer,
    "nadar": image_nadar,
    "casar": image_casar,
    "pular": image_pular,
    "rato": image_rato,
    "linha": image_linha
}
palavras = list(dicio.keys())

# Posições das letras faltantes
posicoes = {
    "banana": [4, 5],
    "sol": [1, 2],
    "cachorro": [5, 6],
    "gato": [1, 3],
    "carro": [2, 3],
    "lapis": [0, 1],
    "bolas": [0, 1],
    "radio": [0, 1],
    "amor": [2, 3],
    "comer": [0, 1],
    "nadar": [0, 1],
    "casar": [2, 3],
    "pular": [2, 3],
    "rato": [0, 1],
    "linha": [0, 1]
}

# Criar diretório de áudios, se não existir
if not os.path.exists('audios'):
    os.makedirs('audios')

# Função para criar áudio da palavra
def criar_audio(palavra):
    tts = gTTS(text=palavra, lang='pt-br')
    filename = os.path.join('audios', f"{palavra}.mp3")
    tts.save(filename)
    return filename

# Função para tocar áudio da palavra
def tocar_audio(filename):
    try:
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()
    except pygame.error as e:
        print(f"Erro ao tocar áudio: {e}")

# Variável global para rastrear a palavra atual
indice_palavra = 0

# Função para exibir a próxima palavra na lista 
def proxima_palavra():
    global indice_palavra
    palavra = palavras[indice_palavra]
    palavra_modificada = list(palavra)
    letras_faltantes = []
    for pos in posicoes[palavra]:
        letras_faltantes.append(palavra[pos])
        palavra_modificada[pos] = '_'
    indice_palavra = (indice_palavra + 1) % len(palavras)
    return "".join(palavra_modificada), letras_faltantes, palavra

# Função para desenhar o texto na tela
def desenhar_texto(texto, x, y, cor=BLACK):
    texto_surface = font.render(texto, True, cor)
    texto_rect = texto_surface.get_rect(center=(x, y))
    screen.blit(texto_surface, texto_rect)

def leitura_caracteres():
    received_chars = ser.read(2).decode('utf-8').strip().lower()
    while len(received_chars) < 2:
        received_chars += ser.read(2 - len(received_chars)).decode('utf-8').strip().lower()
    return received_chars[0], received_chars[1]

def monta_palavra(posicao, caractere):
    if posicao.isdigit() and int(posicao) in range(len(palavra)):
        palavra[int(posicao)] = caractere
    else:
        print("Erro na montagem de palavras")

def limpar():
    global palavra
    palavra = ['0', '0', '0', '0', '0', '0']

# Configurações da porta serial
port = '/dev/ttyUSB0'  # Ajuste conforme necessário
baud_rate = 9600

try:
    ser = serial.Serial(port, baud_rate, timeout=0.1)
except serial.SerialException as e:
    print(f"Erro ao abrir a porta serial: {e}")
    sys.exit(1)

# Função principal do jogo
def main():
    palavra_atual, letras_faltando, palavra_completa = proxima_palavra()
    input_text = ""
    palavra_filtrada = ""
    
    score = 0
    mostrar_palavra_completa = False

    # Criar e tocar áudio da palavra
    audio_file = criar_audio(palavra_completa)
    tocar_audio(audio_file)

    tempo_inicial = pygame.time.get_ticks()

    clock = pygame.time.Clock()
    running = True

    try:
        while running:
            screen.fill(MAGENTA)

            # Desenha a palavra atual na tela com '_'
            desenhar_texto(palavra_atual, screen_width // 2, screen_height // 1.56)
            desenhar_texto(palavra_filtrada, screen_width // 2, screen_height // 1.3)
            # Desenha o texto de entrada na tela
            #desenhar_texto(palavra_filtrada, screen_width // 2, screen_height // 6 + 10)

            # Desenha a pontuação na tela
            desenhar_texto(f"Score: {score}", screen_width // 6, 80)

            tempo_decorrido = (pygame.time.get_ticks() - tempo_inicial) / 1000  # em segundos
            desenhar_texto(f"Tempo: {tempo_decorrido:.0f}s", screen_width // 1.24, 80)

            # Desenha a imagem correspondente
            screen.blit(dicio[palavra_completa], (screen_width // 2.5, screen_height // 4))

            pygame.display.flip()

            # Verifica eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        break

            # Leitura da entrada serial
            if ser.in_waiting > 0:
                received_char = ser.read().decode('utf-8').strip().lower()
                input_text += received_char

                if len(input_text) >= 2:

                    posicao, caractere = input_text[:2]
                    input_text = input_text[2:]

                    if posicao.isdigit() and int(posicao) in range(len(palavra)):
                        palavra[int(posicao)] = caractere
                        palavra_filtrada = ''.join([char for char in palavra if char != '0'])
                        print(palavra_filtrada)
                        pygame.display.flip()

                        if len(palavra_filtrada) == 2:
                            if sorted(palavra_filtrada) == sorted(letras_faltando):
                                score += 1
                                acerto_som.play()
                                desenhar_texto(palavra_completa, screen_width // 2, screen_height // 1.36 + 150)  # Desenha a palavra completa após o acerto
                                pygame.display.flip()  # Atualiza a tela
                                time.sleep(1)  # Dá um delay
                                tocar_audio(audio_file)  # Toca a palavra completa
                                time.sleep(2)  # Dá um delay
                                palavra_filtrada = ""
                                input_text = ""
                                palavra_atual, letras_faltando, palavra_completa = proxima_palavra()
                                audio_file = criar_audio(palavra_completa)
                                tocar_audio(audio_file)
                                limpar()
                                tempo_inicial = pygame.time.get_ticks()  # Reseta o tempo inicial
                            else:
                                erro_som.play()
                                palavra_filtrada = ""
                                limpar()

            clock.tick(FPS)

    finally:
        # Fechar o Pygame e a porta serial
        
                    import menu as mn
                    mn.menu_principal()
                    

if __name__ == "__main__":
    main()