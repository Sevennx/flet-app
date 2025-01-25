import flet as ft

def page1(page: ft.Page):
    FG = '#3450a1'
    FWG = '#97b4ff'

    return ft.View(
        route="/page1",
        controls=[
            ft.Container(
                width=400,
                height=850,
                bgcolor=FG,
                border_radius=35,
                content=ft.Stack(
                    controls=[
                        ft.Row(
                            alignment=ft.MainAxisAlignment.START,
                            controls=[
                                ft.ElevatedButton(
                                    "Voltar",
                                    on_click=lambda _: page.go("/main")
                                )
                            ]
                        ),
                        ft.Column(
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                ft.Text(
                                    "Página 1",
                                    size=40,
                                    weight=ft.FontWeight.BOLD,
                                    color=FWG,
                                    text_align=ft.TextAlign.CENTER
                                )
                            ]
                        )
                    ]
                )
            )
        ]
    )
