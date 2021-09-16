from gtts import gTTS
from pygame import mixer
from pydub import AudioSegment
import os


class TransformarAudio:
    """Classe Utilizada para transformar um texto em um audio."""
    def __init__(self, texto, idioma='pt-br', titulo=None):
        self.texto = texto
        self.idioma = idioma
        self.__audio_criado = False
        if titulo is None:
            self.titulo = self.texto.replace(' ', '')[:10]
    
    def criar_audio(self):
        """Criar um audio com o texto informado e o transforma para o formato .ogg"""
        google_audio = gTTS(text=self.texto, lang=self.idioma)
        google_audio.save(self.titulo+'.mp3')
        AudioSegment.from_mp3(self.titulo+'.mp3').export(self.titulo+'.ogg', format='ogg')
        os.remove(self.titulo+'.mp3')
        self.__audio_criado = True

    def tocar_audio(self):
        """Utilizado para tocar o audio criado com a função 'criar_audio'."""
        if self.__audio_criado:
            mixer.init()
            mixer.music.load(self.titulo+'.ogg')
            mixer.music.play()
            while mixer.music.get_busy() == True:
                continue
        else:
            raise FileNotFoundError('Arquivo ainda não foi criado.')
            
    def remover_audio(self):
        """Função utilizada para excluir o audio criado anteriormente."""
        if self.__audio_criado:
            os.remove(self.titulo+'.ogg')
        else:
            raise FileNotFoundError('Arquivo ainda não foi criado.')



if __name__ == '__main__':
    texto = 'Eu sou uma pessoa muito legal!'
    audio = TransformarAudio(texto) # Inicializa a classe com o texto.
    audio.criar_audio() # Cria um arquivo com a voz do google lendo o texto.
    audio.tocar_audio() # Reproduz o Audio criando anteriormente.
    audio.remover_audio() # Após criar e executar o audio, essa função excluir permanentemente o arquivo do audio.