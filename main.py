from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from datetime import datetime, timedelta

class BlizzardApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # Titre
        self.layout.add_widget(Label(text="VINAVINAO HANJAKANA BY RAMAH", font_size=55, color=(1,1,1,1)))
        
        # Input Heure
        self.heure_input = TextInput(hint_text="HEURE DE DEPART (HH:MM:SS)", multiline=False)
        self.layout.add_widget(self.heure_input)
        
        # Input Hex
        self.hex_input = TextInput(hint_text="HEXADECIMAL", multiline=False)
        self.layout.add_widget(self.hex_input)
        
        # Bokotra Calculer
        btn = Button(text="CALCULER", background_color=(0, 0.4, 0.8, 1))
        btn.bind(on_press=self.fikajiana)
        self.layout.add_widget(btn)
        
        # Valiny
        self.resultat = Label(text="Resultat ho hita eto", font_size=50)
        self.layout.add_widget(self.resultat)
        
        return self.layout

    def fikajiana(self, instance):
        try:
            h = self.heure_input.text
            hx = self.hex_input.text
            
            # Formula tsotra: maka ny sandan'ny hex farany ho segondra
            offset = int(hx[-2:], 16) 
            
            original_time = datetime.strptime(h, "%H:%M:%S")
            new_time = original_time + timedelta(seconds=offset + 45) # Ohatra fotsiny ny +45
            
            self.resultat.text = f"ORA MANARAKA: {new_time.strftime('%H:%M:%S')}"
        except:
            self.resultat.text = "Diso ny fampidirana nataonao!"

if __name__ == '__main__':
    BlizzardApp().run()
