import flet as ft
from pages.main_page import main_page
from pages.page1 import page1
from pages.chat import chat_page

def main(page: ft.Page):
    def route_change(e: ft.RouteChangeEvent):
        page.views.clear()
        
        if e.route == "/main":
            page.views.append(main_page(page))
        elif e.route == "/page1":
            page.views.append(page1(page))
        elif e.route == "/chat":
            page.views.append(chat_page(page))
        
        page.update()

    page.on_route_change = route_change
    page.go("/main")

ft.app(main, view=ft.AppView.WEB_BROWSER)
