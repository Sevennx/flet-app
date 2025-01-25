import flet as ft

def main_page(page: ft.Page):
    BG = '#041955'
    FWG = '#97b4ff'

    return ft.View(
        route="/main",
        controls=[
            ft.Container(
                width=400, 
                height=850, 
                bgcolor=BG,
                border_radius=35,
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Text(
                            "Bem-Vindo",
                            size=40,
                            weight=ft.FontWeight.BOLD,
                            color=FWG,
                            text_align=ft.TextAlign.CENTER
                        ),
                        ft.ElevatedButton(
                            "Ir para Página 1",
                            on_click=lambda _: page.go("/page1")
                        ),
                        ft.ElevatedButton(
                            "Ir para Chat",
                            on_click=lambda _: page.go("/chat")
                        )
                    ]
                )
            )
        ]
    )
