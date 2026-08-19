import flet as ft

def main(page: ft.Page):
    # 1. Configurações da página simulando um celular
    page.window_width = 360
    page.window_height = 640
    page.bgcolor = "#F4F1EA" # Cor de fundo bege
    page.padding = 20
    page.scroll = "auto" # Adiciona rolagem na tela inteira automaticamente

    # 2. Elementos da interface
    titulo = ft.Text("Encontrar profissional", size=24, weight=ft.FontWeight.BOLD, color="#185650")
    
    busca = ft.TextField(hint_text="Eletricista", bgcolor="white", border_radius=10)

    # Botões de filtro lado a lado (Row)
    filtros = ft.Row([
        ft.ElevatedButton("Recife", bgcolor="#185650", color="white"),
        ft.OutlinedButton("Hoje"),
        ft.OutlinedButton("Preço"),
    ])

    # 3. Função para criar um card (Componentização)
    def criar_card(iniciais, nome, info, status, cor_icone):
        return ft.Container(
            bgcolor="white",
            padding=15,
            border_radius=10,
            content=ft.Row([
                # Ícone redondo com as iniciais
                ft.CircleAvatar(content=ft.Text(iniciais, color="black"), bgcolor=cor_icone),
                
                # Textos empilhados (Column)
                ft.Column([
                    ft.Text(nome, weight=ft.FontWeight.BOLD, color="black"),
                    ft.Text(info, size=12, color=ft.colors.GREY),
                    ft.Text(status, size=12, color="#537052", weight=ft.FontWeight.BOLD),
                ], spacing=2) # Espaçamento entre os textos
            ])
        )

    # 4. Adicionando tudo na tela (na ordem que deve aparecer)
    page.add(
        titulo,
        busca,
        filtros,
        ft.Divider(height=10, color="transparent"), # Apenas um espaço em branco
        criar_card("JS", "João Silva", "4,8 · 127 serviços · 3km", "Disponível agora", ft.colors.LIGHT_GREEN_300),
        criar_card("CA", "Carlos Alves", "4,9 · 84 serviços · 5km", "Disponível amanhã", ft.colors.LIGHT_GREEN_300)
    )

# 5. O SEGREDO DO CODESPACES: Iniciar como Web Browser
ft.app(target=main, view=ft.AppView.WEB_BROWSER)