import logging as log
import kivy
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.lang import Builder

class ImageButton(ButtonBehavior, Image):
    pass

def print_kivy_pathes():
    log.info("Kivy base dir: %s" % kivy.kivy_base_dir)
    log.info("Kivy examples dir: %s" % kivy.kivy_examples_dir)

class LoginScreen(Screen):
    def try_login(self):
        login = self.ids.login_input.text
        password = self.ids.password_input.text
        print(f"Логин: {login}, Пароль: {password}")
        
    def go_registration(self):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = 'registration'

    def open_settings(self):
        print("Открыть настройки")

class RegistrationScreen(Screen):
    def try_register(self):
        login = self.ids.login_input.text
        password = self.ids.password_input.text
        email = self.ids.email_input.text
        print(f"Логин: {login}, Пароль: {password}, email: {email}")
    
    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'login'

class NotesApp(App):
    def build(self):
        
        Builder.load_file('login.kv')
        Builder.load_file('registration.kv')
        
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(RegistrationScreen(name='registration'))
        return sm

if __name__ == "__main__":
    log.basicConfig(
        level=log.CRITICAL,           # Уровень регистрации сообщений
        format='%(asctime)s [%(levelname)s]: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'    # Формат даты и времени
    )
    
    log.info("Start Kivy Tutors")
    print_kivy_pathes()
    NotesApp().run()
    log.info("End Kivy Tutors")