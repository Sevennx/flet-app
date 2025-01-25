from flet import *

def main(page: Page):
    BG = '#041955'
    FWG = '#97b4ff'
    FG = '#3450a1'
    PINK = '#eb0cff'
    
    # Mensagem "Bem-vindo" centralizada
    welcome_message = Text(
        "Bem-vindo",
        size=40,
        weight=FontWeight.BOLD,
        color=FWG,
        text_align=TextAlign.CENTER
    )
    
    # Primeira página com a mensagem "Bem-vindo"
    first_page_Contents = Container(
        content=Column(
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            controls=[
                Row(
                    alignment=MainAxisAlignment.CENTER,
                    controls=[
                        welcome_message
                    ]
                )
            ]
        )
    )
    
    page_1 = Container(
        width=400,
        height=850,
        bgcolor=FG,
        border_radius=35,
        content=first_page_Contents
    )
    
    page_2 = Row(
        controls=[
            Container(
                width=400,
                height=850,
                bgcolor=FG,
                border_radius=35,
                padding=padding.only(
                    top=50, 
                    left=20,
                    right=20, 
                    bottom=5 
                ),
                content=Column(
                    controls=[first_page_Contents] 
                )
            )
        ]
    )
    
    container = Container(
        width=400, 
        height=850, 
        bgcolor=BG,
        border_radius=35,
        content=Stack(
            controls=[
                page_1,
                page_2
            ]
        )
    )
    
    page.add(container)
    
app(target=main)