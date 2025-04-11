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

    def simular_aposentadoria(idade, genero, contribuicao, media_salarial, categoria):
        # Definindo parâmetros conforme gênero e categoria
        if categoria == "idade":
            idade_min = 65 if genero == "homem" else 62
            contribuicao_min = 15
            pode_aposentar = idade >= idade_min and contribuicao >= contribuicao_min

            if not pode_aposentar:
                anos_para_idade = max(0, idade_min - idade)
                anos_para_contribuicao = max(0, contribuicao_min - contribuicao)
                anos_faltantes = max(anos_para_idade, anos_para_contribuicao)
            else:
                anos_faltantes = 0

        elif categoria == "tempo":
            contribuicao_min = 35 if genero == "homem" else 30
            pode_aposentar = contribuicao >= contribuicao_min

            if not pode_aposentar:
                anos_faltantes = contribuicao_min - contribuicao
            else:
                anos_faltantes = 0

        else:
            return "Categoria inválida!"

        # Cálculo do valor estimado
        anos_extra = max(0, contribuicao - 15)
        percentual = 60 + (anos_extra * 2)
        percentual = min(percentual, 100)  # Limitado a 100%
        valor_beneficio = (percentual / 100) * media_salarial

        # Resultados
        resultado = {
            "pode_aposentar": pode_aposentar,
            "anos_faltantes": anos_faltantes,
            "valor_estimado": round(valor_beneficio, 2)
        }

        return resultado

    # Exemplo de uso:
    res = simular_aposentadoria(
        idade=60,
        genero="mulher",
        contribuicao=20,
        media_salarial=3000,
        categoria="idade"
    )

    if res["pode_aposentar"]:
        print("Você já pode se aposentar!")
    else:
        print(f"Ainda faltam {res['anos_faltantes']} anos para se aposentar.")

    print(f"Valor estimado do benefício: R$ {res['valor_estimado']}")

    def gerencia_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Cadastro"), bgcolor=Colors.PRIMARY_CONTAINER),
                    input_titulo, input_descricao, input_categoria, input_autor,
                    ElevatedButton(text="Cadastrar", on_click=lambda _: page.go("/segunda"))
                ]
            )
        )

        if page.route == "/segunda":
            page.views.append(
                View(
                    "/segunda",
                    [
                        AppBar(title=Text("Segunda Tela"), bgcolor=Colors.PRIMARY_CONTAINER),
                        Text(value=f'Titulo: {input_titulo.value}'),
                        Text(value=f'Descrição: {input_titulo.value} '),
                        Text(value=f'Categoria: {input_categoria.value} '),
                        Text(value=f'Autor: {input_categoria.value} '),
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

    input_titulo = ft.TextField(label="Titulo",
                              hint_text="Digite seu titulo"
                              )
    input_categoria = ft.TextField(label="Categoria",
                              hint_text="Digite a categoria"
                              )
    input_autor = ft.TextField(label="Autor",
                               hint_text="Digite o Autor"
                               )

ft.app(main)

