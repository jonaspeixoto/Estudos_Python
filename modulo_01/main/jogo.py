from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import random

class JogoDaForca(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.palavras = ['banana', 'abacaxi', 'computador', 'elefante', 'girafa']
        self.palavra_atual = random.choice(self.palavras)
        self.letras_corretas = set()
        self.tentativas_maximas = 6
        self.tentativas = 0

    def build(self):
        layout = BoxLayout(orientation='vertical')

        self.label_palavra = Label(text=self.obter_palavra_mascarada())
        layout.add_widget(self.label_palavra)

        self.input_letra = TextInput(multiline=False)
        layout.add_widget(self.input_letra)

        btn_adivinhar = Button(text="Adivinhar", on_press=self.adivinhar)
        layout.add_widget(btn_adivinhar)

        return layout

    def obter_palavra_mascarada(self):
        return ' '.join([letra if letra in self.letras_corretas else '_' for letra in self.palavra_atual])

    def adivinhar(self, instance):
        letra = self.input_letra.text.lower()
        self.input_letra.text = ''

        if letra in self.letras_corretas:
            self.mostrar_mensagem("Você já tentou essa letra.")
            return

        if letra in self.palavra_atual:
            self.letras_corretas.add(letra)
            self.mostrar_mensagem("Letra correta!")
        else:
            self.tentativas += 1
            self.mostrar_mensagem(f"Letra incorreta. Tentativas restantes: {self.tentativas_maximas - self.tentativas}")

        self.label_palavra.text = self.obter_palavra_mascarada()

        if all(letra in self.letras_corretas for letra in self.palavra_atual):
            self.mostrar_mensagem("Parabéns, você acertou a palavra!")
            self.reiniciar_jogo()

        if self.tentativas == self.tentativas_maximas:
            self.mostrar_mensagem(f"Você perdeu. A palavra era: {self.palavra_atual}")
            self.reiniciar_jogo()

    def mostrar_mensagem(self, mensagem):
        self.root.add_widget(Label(text=mensagem))

    def reiniciar_jogo(self):
        self.palavra_atual = random.choice(self.palavras)
        self.letras_corretas.clear()
        self.tentativas = 0
        self.label_palavra.text = self.obter_palavra_mascarada()

if __name__ == '__main__':
    JogoDaForca().run()
