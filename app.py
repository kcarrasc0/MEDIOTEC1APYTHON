import flet as ft

def main(page: ft.Page):
 
    page.window_width = 360
    page.window_height = 740
    page.padding = 0
    page.theme_mode = ft.ThemeMode.LIGHT # ou DARK

    # nav
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.MENU),
        leading_width=40,
        title=ft.Text("Meu App"),
        center_title=True,
        bgcolor=ft.colors.BLUE_700,
        color=ft.colors.WHITE
    )

    # Conteúdo 
    conteudo = ft.Container(
        padding=20,
        content=ft.Column(
            controls=[
                ft.Icon(ft.icons.MOBILE_FRIENDLY, size=80, color=ft.colors.BLUE_700),
                ft.Text("Página Estática", size=24, weight=ft.FontWeight.BOLD),
                ft.Text(
                    "Este é um exemplo de layout simples focado em dispositivos móveis utilizando Python e Flet.",
                    text_align=ft.TextAlign.CENTER,
                    size=16
                ),
                ft.Divider(height=20, color=ft.colors.TRANSPARENT),
                ft.Card(
                    content=ft.Container(
                        padding=15,
                        content=ft.Column([
                            ft.Text("Informações", weight=ft.FontWeight.BOLD),
                            ft.Text("O Flet adapta seus componentes nativamente para Android e iOS.")
                        ])
                    )
                ),
                ft.Divider(height=20, color=ft.colors.TRANSPARENT),
                ft.ElevatedButton(
                    text="Continuar", 
                    icon=ft.icons.ARROW_FORWARD,
                    width=200,
                    style=ft.ButtonStyle(
                        color=ft.colors.WHITE,
                        bgcolor=ft.colors.BLUE_700,
                    )
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

    page.add(conteudo)

ft.app(target=main)