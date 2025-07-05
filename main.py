import logging as log
import kivy
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image

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

    def open_settings(self):
        print("Открыть настройки")

class LoginApp(App):
    def build(self):
        return LoginScreen()

if __name__ == "__main__":
    log.basicConfig(
        level=log.CRITICAL,           # Уровень регистрации сообщений
        format='%(asctime)s [%(levelname)s]: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'    # Формат даты и времени
    )
    
    log.info("Start Kivy Tutors")
    print_kivy_pathes()
    LoginApp().run()
    log.info("End Kivy Tutors")