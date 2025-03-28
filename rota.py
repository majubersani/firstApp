import flet as ft
from flet import AppBar, ElevatedButton, Text, View, colors
from flet.core.app_bar import AppBar
from flet.core.colors import Colors


def main (page: ft.Page):
    #Configuração da página
    page.title = "Minha Aplicação Flet"
    page.theme_mode = ft.ThemeMode.DARK # ou ft.themeMode.LIGHT
    page.window.width = 375
    page.window.height = 667

    def gerencia_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Home"), bgcolor=Colors.PRIMARY_CONTAINER),
                    input_nome,
                    ElevatedButton(text="Navegar", on_click=lambda _: page.go("/segunda"))
                ]
            )
        )

        if page.route == "/segunda":
            page.views.append(
                View(
                    "/segunda",
                    [
                        AppBar(title=Text("Segunda Tela"), bgcolor=Colors.PRIMARY_CONTAINER),
                        Text(value=f'olá, Bem Vinda {input_nome.value}')
                    ],
                )
            )
        page.update()

    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = gerencia_rotas
    page.on_view_pop = voltar



    page.go(page.route)

    input_nome = ft.TextField(label="Nome",
                              hint_text="Digite seu nome"
                              )

ft.app(main)