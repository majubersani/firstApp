import flet as ft
from flet import AppBar, ElevatedButton, Text, Colors, View, Icons
from flet.core import slider
from flet.core.list_view import ListView
from flet.core.text_style import TextStyle
from flet.core.textfield import TextField


def main(page: ft.Page):
    # Configuração da página
    page.title = "Simulação de Aposentadoria"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    page.theme = ft.Theme(
        text_theme=ft.TextTheme(
            body_medium=TextStyle(color="#000000") #Cor da letra
        )
    )

# Definição de funções
def gerencia_rotas(e):
    page.views.clear()
    page.views.append(
        View(
            '/',
            [
                AppBar(title=Text("Simulador de aposentadoria"), color="#C6E2FF", bgcolor="#191970", center_title=True),

                ft.Container(
                    content=ft.Column(
                        [
                            # ft.Icon(name=Icons.ATTACH_MONEY_ROUNDED, color="#191970", size=100),
                            ft.Image(src=f"inss.png",
                                     width=(page.window.width / 2),
                                     fit=ft.ImageFit.CONTAIN)
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,  # Alinha no centro verticalmente
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER  # Alinha no centro horizontalmente
                    ),
                    alignment=ft.alignment.center,  # Centraliza o Container
                    padding=ft.padding.only(top=80)  # Ajuste para mover um pouco para baixo
                ),
                ft.Container(
                    content=ft.Column(
                        [
                            ElevatedButton(text='Simular aposentadoria',
                                           width=(page.window.width / 2),
                                           color="#C6E2FF",
                                           bgcolor="#191970",
                                           on_click=lambda _: page.go('/simular_aposentadoria')),
                            ElevatedButton(text='Ver regras',
                                           width=(page.window.width / 2),
                                           color="#C6E2FF",
                                           bgcolor="#191970",
                                           on_click=lambda _: page.go('/regras')
                                           )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,  # Alinha no centro verticalmente
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER  # Alinha no centro horizontalmente
                    ),
                    alignment=ft.alignment.center,  # Centraliza o Container
                    padding=ft.padding.only(top=80)  # Ajuste para mover um pouco para baixo
                )

            ],  # controls
            bgcolor="#C6E2FF",
        )
    )


ft.app(main)