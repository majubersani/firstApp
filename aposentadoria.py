import flet as ft
from flet import AppBar, ElevatedButton, Page, Text, View, Column
from flet.core.colors import Colors
from flet.core.dropdown import Option


def main(page: Page):
    page.title = "Simulador de Aposentadoria"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.width = 375
    page.window.height = 667

    def gerenciar_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text('Simulador Aposentadoria'), center_title=True, bgcolor=Colors.GREEN_400),
                    ft.Image(src="assets/aposentadoria.png", width=350),
                    ElevatedButton(text="Simular aposentadoria", width=page.window.width,
                                   on_click=lambda _: page.go("/simular_aposentadoria")),
                    ElevatedButton(text="Regras aposentadoria", width=page.window.width,
                                   on_click=lambda _: page.go("/regras")),
                ]
            )
        )

        if page.route == "/simular_aposentadoria":
            page.views.append(
                View(
                    "/simular_aposentadoria", [
                        AppBar(title=Text("Simulação Aposentadoria"), center_title=True, bgcolor=Colors.GREEN_400),
                        Text(value="Simulação aposentadoria", color=Colors.GREEN_800),
                        genero_escolhido,
                        idade_dropdown,
                        tempo_contribuicao_dropdown,
                        media_salarial,
                        opcao,
                        ElevatedButton(text="Calcular", on_click=verificar_campos, width=page.window.width),
                        alerta,
                    ],
                    bgcolor=Colors.WHITE,
                )
            )

        if page.route == '/regras':
            page.views.append(
                View(
                    '/regras',
                    [
                        AppBar(title=Text('Regras'), color="#C6E2FF", bgcolor="#388E3C", center_title=True),
                        ft.ListView(
                            [
                                ft.Container(
                                    content=ft.Column(
                                        [
                                            Text(value='• Aposentadoria por idade', size=24, weight=ft.FontWeight.BOLD,
                                                 color="#388E3C"),
                                            ft.Container(
                                                content=ft.Column(
                                                    [
                                                        Text(value='- Homens', size=20, weight=ft.FontWeight.BOLD,
                                                             italic=True, color="#388E3C"),
                                                        ft.Container(
                                                            content=ft.Column(
                                                                [
                                                                    Text(
                                                                        value='65 anos de idade e pelo menos 15 anos de contribuição.',
                                                                        size=16, color="#2C6B2F"),
                                                                ]
                                                            ),  # Column 3
                                                            padding=ft.padding.only(left=40)
                                                        ),  # Container 3

                                                        Text(value='- Mulheres', size=20, weight=ft.FontWeight.BOLD,
                                                             italic=True, color="#388E3C"),
                                                        ft.Container(
                                                            content=ft.Column(
                                                                [
                                                                    Text(
                                                                        value='62 anos de idade e pelo menos 15 anos de contribuição.',
                                                                        size=16, color="#2C6B2F")
                                                                ]
                                                            ),  # COlumn 4
                                                            padding=ft.padding.only(left=40)
                                                        )  # Column 4
                                                    ]
                                                ),  # column 2 D
                                                padding=ft.padding.only(left=20)
                                            ),  # container 2 C

                                            Text(value='• Aposentadoria por tempo de contribuição', size=20,
                                                 weight=ft.FontWeight.BOLD, color="#388E3C"),
                                            ft.Container(
                                                content=ft.Column(
                                                    [
                                                        Text(value='- Homens', size=20, weight=ft.FontWeight.BOLD,
                                                             italic=True, color="#388E3C"),
                                                        ft.Container(
                                                            content=ft.Column(
                                                                [
                                                                    Text(value='35 anos de contribuição.', size=16,
                                                                         color="#2C6B2F")
                                                                ]
                                                            ),
                                                            padding=ft.padding.only(left=40)
                                                        ),

                                                        Text(value='- Mulheres', size=20, weight=ft.FontWeight.BOLD,
                                                             color="#388E3C"),
                                                        ft.Container(
                                                            content=ft.Column(
                                                                [
                                                                    Text(value='30 anos de contribuição', size=16,
                                                                         color="#2C6B2F")
                                                                ]
                                                            ),
                                                            padding=ft.padding.only(left=40)
                                                        )

                                                    ]
                                                ),  # Column 5 D
                                                padding=ft.padding.only(left=20)
                                            ),  # Container 3 C

                                            Text(value='• Valor estimado do benefício', size=20,
                                                 weight=ft.FontWeight.BOLD, color="#388E3C"),
                                            ft.Container(
                                                content=ft.Column(
                                                    [
                                                        ft.Container(
                                                            content=ft.Column(
                                                                [
                                                                    Text(
                                                                        value='O valor da aposentadoria será uma média de 60% da média salarial informada,'
                                                                              ' acrescido de 2% por ano que exceder o tempo mínimo de contribuição.',
                                                                        size=16, color="#2C6B2F")
                                                                ]
                                                            ),
                                                            padding=ft.padding.only(left=40)
                                                        )
                                                    ]
                                                )
                                            )
                                        ]
                                    ),  # Column B
                                    alignment=ft.alignment.center,  # Centraliza o Container
                                    padding=ft.padding.only(top=50)  # Ajuste para mover um pouco para baixo
                                )  # Container A
                            ],
                            expand=True
                        ),

                    ],  # controls
                    bgcolor=Colors.WHITE,
                )  # View
            )

        if page.route == "/resultados":
            calcular_beneficio()
            page.views.append(
                View(
                    '/resultados', [
                        Text('Resultados', color=Colors.GREEN_800),
                        com_aposentadoria,
                        sem_aposentadoria,
                        beneficio,
                        alerta,
                        ElevatedButton(
                            text="Voltar à página inicial",
                            on_click=lambda _: page.go("/"),
                            width=page.window.width
                        ),
                    ]
                )
            )

        page.update()

    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_view_pop = voltar
    page.on_route_change = gerenciar_rotas
    page.go(page.route)

    def verificar_campos(e):
        try:
            int(media_salarial.value)

            if genero_escolhido.value is None or idade_dropdown.value is None or tempo_contribuicao_dropdown.value is None or media_salarial.error or opcao.value is None:
                raise ValueError
            else:
                page.go('/resultados')
        except ValueError:
            alerta.value = 'Preencha os campos corretamente'
            page.update()

    def limpar_alerta(e):
        alerta.value = ''
        page.update()

    def calcular_beneficio():
        try:
            genero = genero_escolhido.value
            idade_var = int(idade_dropdown.value)
            salario = int(media_salarial.value)
            tempo_contribuicao_var = int(tempo_contribuicao_dropdown.value)
            categoria = opcao.value

            if genero == 'masculino':
                if categoria == 'idade':
                    if idade_var >= 65 and tempo_contribuicao_var >= 15:
                        com_aposentadoria.value = 'Você pode se aposentar!'
                        v = salario * (0.6 + 0.02 * (tempo_contribuicao_var - 15))
                        beneficio.value = v
                    elif idade_var < 65 and tempo_contribuicao_var < 15:
                        sem_aposentadoria.value = 'Você não pode se aposentar'
                    elif idade_var < 65 and tempo_contribuicao_var >= 15:
                        sem_aposentadoria.value = 'Você não pode se aposentar'
                    else:
                        sem_aposentadoria.value = 'Você não pode se aposentar'
                else:
                    if tempo_contribuicao_var >= 35:
                        com_aposentadoria.value = 'Você pode se aposentar'
                        v = salario * (0.6 + 0.02 * (tempo_contribuicao_var - 35))
                        beneficio.value = v
                    else:
                        sem_aposentadoria.value = 'Você não pode se aposentar'
            elif genero == 'feminino':
                if categoria == 'idade':
                    if idade_var >= 62 and tempo_contribuicao_var >= 15:
                        com_aposentadoria.value = 'Você pode se aposentar'
                        v = salario * (0.6 + 0.02 * (tempo_contribuicao_var - 15))
                        beneficio.value = v
                    elif idade_var < 62 and tempo_contribuicao_var < 15:
                        sem_aposentadoria.value = 'Você não pode se aposentar'
                    elif idade_var < 62 and tempo_contribuicao_var >= 15:
                        sem_aposentadoria.value = 'Você não pode se aposentar'
                    else:
                        sem_aposentadoria.value = 'Você não pode se aposentar'
                else:
                    if tempo_contribuicao_var >= 30:
                        com_aposentadoria.value = "Você pode se aposentar"
                        v = salario * (0.6 + 0.02 * (tempo_contribuicao_var - 30))
                        beneficio.value = v
                    else:
                        sem_aposentadoria.value = "Você não pode se aposentar"

        except ValueError:
            alerta.value = 'Preencha todos campos'
        page.update()

    idade_dropdown = ft.Dropdown(
        label="Idade",
        width=page.window.width,
        border_color=Colors.GREEN_400,
        on_change=limpar_alerta,
        options=[Option(key=str(i), text=str(i)) for i in range(18, 101)]  # Idades de 18 a 100
    )

    tempo_contribuicao_dropdown = ft.Dropdown(
        label="Tempo de contribuição",
        width=page.window.width,
        border_color=Colors.GREEN_400,
        on_change=limpar_alerta,
        options=[Option(key=str(i), text=str(i)) for i in range(0, 51)]  # Tempo de 0 a 50 anos
    )

    genero_escolhido = ft.Dropdown(
        label="Gênero",
        width=page.window.width,
        border_color=Colors.GREEN_400,
        on_change=limpar_alerta,
        options=[
            Option(key='masculino', text='masculino'), Option(key='feminino', text='feminino')],
    )

    media_salarial = ft.TextField(label='Média salarial', border_color=Colors.GREEN_400,
                                  border_radius=10, on_click=limpar_alerta)

    opcao = ft.RadioGroup(on_change=limpar_alerta, content=ft.Row([
        ft.Radio(value='tempo', label="Tempo de contribuição"),
        ft.Radio(value='idade', label="Idade")
    ]))

    alerta = ft.Text(value='', color=Colors.GREEN_600)
    sem_aposentadoria = ft.Text(value='', color=Colors.GREEN_600)
    com_aposentadoria = ft.Text(value='', color=Colors.GREEN_600)
    beneficio = ft.Text(value='', color=Colors.GREEN_600)

ft.app(main)
