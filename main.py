import flet as ft

def main(page: ft.Page):
    page.window_width, page.window_height = 360, 640
    page.bgcolor = "#0B0B12" # Fundo escuro real
    page.padding = 20
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # 1. Avatar
    avatar = ft.Image(src="kcarrasquinho.png", width=120, height=120)

    # Tag de Nome (CORRIGIDO: padding simplificado)
    tag_nome = ft.Container(
        content=ft.Text("KCARRASQUINHO", size=10, weight="bold", color="#A020F0"),
        bgcolor="#1A1A2E", 
        padding=10, 
        border_radius=15
    )

    # 2. Textos com múltiplas cores (TextSpans)
    titulo = ft.Text(
        spans=[
            ft.TextSpan("Abra a mente, o código\nvem para o ", ft.TextStyle(size=24, weight="bold", color="white")),
            ft.TextSpan("mundo\nreal", ft.TextStyle(size=24, weight="bold", color="#A020F0")),
            ft.TextSpan(".", ft.TextStyle(size=24, weight="bold", color="white")),
        ],
        text_align=ft.TextAlign.CENTER
    )

    subtexto = ft.Text("Toque na caixa abaixo para liberar os módulos e\niniciar nossa dinâmica de programação prática.", size=12, color="#6A82B8", text_align=ft.TextAlign.CENTER)

    # 3. Caixa Interativa (GestureDetector)
    def clicar_na_caixa(e):
        page.snack_bar = ft.SnackBar(ft.Text("Módulos da Caixa dos Devs liberados com sucesso! 🚀"), bgcolor="#A020F0")
        page.snack_bar.open = True
        page.update()

    caixa_interativa = ft.GestureDetector(
        on_tap=clicar_na_caixa,
        content=ft.Image(src="caixa.png", width=200)
    )

    # 4. Botão final (CORRIGIDO: Ícone de círculo substituído por um Container redondo)
    btn_interagir = ft.Container(
        content=ft.Row([
            ft.Container(width=10, height=10, border_radius=5, bgcolor="#A020F0"),
            ft.Text("CLIQUE PARA INTERAGIR", size=10, color="grey", weight="bold")
        ], alignment=ft.MainAxisAlignment.CENTER),
        bgcolor="#151520", padding=10, border_radius=20, width=200
    )

    # Montando a tela
    page.add(
        avatar, tag_nome, ft.Container(height=10), # Container vazio serve como espaço
        titulo, subtexto, ft.Container(height=20),
        caixa_interativa,
        ft.Container(expand=True), # Empurra o botão de interagir lá para baixo
        btn_interagir
    )

ft.run(main, view=ft.AppView.WEB_BROWSER, assets_dir="assets")