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
                    AppBar(title=Text("Simulador de aposentadoria"), color="#000000", bgcolor="#8f76d1", center_title=True),

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
        if page.route == '/regras':
            page.views.append(
                View(
                    '/regras',
                    [
                        AppBar(title=Text('Regras'), color="#C6E2FF", bgcolor="#191970", center_title=True),
                        ft.ListView(
                            [
                                ft.Container(
                                    content=ft.Column(
                                        [
                                            Text(value='• Aposentadoria por idade', size=24, weight=ft.FontWeight.BOLD),
                                            ft.Container(
                                                content=ft.Column(
                                                    [
                                                        Text(value='- Homens', size=20, weight=ft.FontWeight.BOLD,
                                                             italic=True),
                                                        ft.Container(
                                                            content=ft.Column(
                                                                [
                                                                    Text(
                                                                        value='65 anos de idade e pelo menos 15 anos de contribuição.',
                                                                        size=16),
                                                                ]
                                                            ),  # Column 3
                                                            padding=ft.padding.only(left=40)
                                                        ),  # Container 3

                                                        Text(value='- Mulheres', size=20, weight=ft.FontWeight.BOLD,
                                                             italic=True),
                                                        ft.Container(
                                                            content=ft.Column(
                                                                [
                                                                    Text(
                                                                        value='62 anos de idade e pelo menos 15 anos de contribuição.',
                                                                        size=16)
                                                                ]
                                                            ),  # COlumn 4
                                                            padding=ft.padding.only(left=40)
                                                        )  # Column 4
                                                    ]
                                                ),  # column 2 D
                                                padding=ft.padding.only(left=20)
                                            ),  # container 2 C

                                            Text(value='• Aposentadoria por tempo de contribuição', size=20,
                                                 weight=ft.FontWeight.BOLD),
                                            ft.Container(
                                                content=ft.Column(
                                                    [
                                                        Text(value='- Homens', size=20, weight=ft.FontWeight.BOLD,
                                                             italic=True),
                                                        ft.Container(
                                                            content=ft.Column(
                                                                [
                                                                    Text(value='35 anos de contribuição.', size=16)
                                                                ]
                                                            ),
                                                            padding=ft.padding.only(left=40)
                                                        ),

                                                        Text(value='- Mulheres', size=20, weight=ft.FontWeight.BOLD),
                                                        ft.Container(
                                                            content=ft.Column(
                                                                [
                                                                    Text(value='30 anos de contribuição', size=16)
                                                                ]
                                                            ),
                                                            padding=ft.padding.only(left=40)
                                                        )

                                                    ]
                                                ),  # Column 5 D
                                                padding=ft.padding.only(left=20)
                                            ),  # Container 3 C

                                            Text(value='• Valor estimado do benefício', size=20,
                                                 weight=ft.FontWeight.BOLD),
                                            ft.Container(
                                                content=ft.Column(
                                                    [
                                                        ft.Container(
                                                            content=ft.Column(
                                                                [
                                                                    Text(
                                                                        value='O valor da aposentadoria será uma média de 60% da média salarial informada,'
                                                                              ' acrescido de 2% por ano que exceder o tempo mínimo de contribuição.',
                                                                        size=16)
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
                                    # padding=ft.padding.only(top=50)  # Ajuste para mover um pouco para baixo
                                )  # Container A
                            ],
                            expand=True
                        ),

                    ],  # controls
                    bgcolor="#C6E2FF"
                )  # View
            )

        if page.route == '/simular_aposentadoria':
            page.views.append(
                View(
                    '/simular_aposentadoria',
                    [
                        AppBar(title=Text('Simular'), color="#C6E2FF", bgcolor="#191970", center_title=True),
                        ft.ListView(
                            [
                                Text(value='Selecione sua idade:', size=22, weight=ft.FontWeight.BOLD),

                                slider_idade,
                                txt_idade,

                                Text(value='Selecione seu gênero:', size=22, weight=ft.FontWeight.BOLD),
                                radio_genero,
                                Text(value='Selecione seu tempo de contribuição:', size=22, weight=ft.FontWeight.BOLD),

                                slider_tempo_contribuicao,
                                txt_tempo_contribuicao,

                                Text(value='Selecione a categoria da aposentadoria desejada:', size=22, weight=ft.FontWeight.BOLD),
                                radio_categoria,

                                slider_salario,
                                txt_salario,

                                ft.Container(
                                    content=ft.Column(
                                        [
                                            ElevatedButton(text='Calcular',
                                                           width=(page.window.width / 2),
                                                           color="#C6E2FF",
                                                           bgcolor="#191970",
                                                           # on_click=exibir_info)
                                                           on_click=lambda _: page.go('/resultado'))
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,  # Alinha no centro verticalmente
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                                        # Alinha no centro horizontalmente
                                    ),
                                    padding=ft.padding.only(top=40)
                                )

                            ],
                            expand=True,
                        )
                    ],
                    bgcolor="#C6E2FF"

                )
            )

        elif page.route == '/resultado':
            calcular_beneficio()
            page.views.append(
                View(
                    '/resultado',
                    [
                        AppBar(title=Text('Simular'), color="#C6E2FF", bgcolor="#191970", center_title=True),
                        ft.Container(
                            content=ft.Column(
                                [
                                    txt_resultado
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,  # Alinha no centro verticalmente
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER
                                # Alinha no centro horizontalmente
                            ),
                            alignment=ft.alignment.center,  # Centraliza o Container
                        )

                    ],
                    bgcolor="#C6E2FF"
                )
            )

        page.update()

    def calcular_beneficio():
        qualificado=None
        motivo=None
        cat=None
        if radio_categoria.value == 'porIdade' and radio_genero.value == 'homem':
            cat = 'por idade'
            if slider_idade.value >= 65 and slider_tempo_contribuicao.value >= 15:
                qualificado = True
                motivo = 'idade'
            elif slider_idade.value < 65 and slider_tempo_contribuicao.value >= 15:
                qualificado = False
                motivo = 'idade'
            elif slider_idade.value >= 65 and slider_tempo_contribuicao.value < 15:
                qualificado = False
                motivo = 'tempo de contribuição'
            elif slider_idade.value < 65 and slider_tempo_contribuicao.value < 15:
                qualificado = False
                motivo = 'idade e tempo'

        elif radio_categoria.value == 'porTempo' and radio_genero.value == 'homem':
            cat = 'por tempo'
            if slider_tempo_contribuicao.value >= 35:
                qualificado = True
                motivo = 'tempo de contribuição'
            elif slider_tempo_contribuicao.value < 35:
                qualificado = False
                motivo = 'tempo de contribuição'

        elif radio_categoria.value == 'porIdade' and radio_genero.value == 'mulher':
            cat = 'por idade'
            if slider_idade.value >= 62 and slider_tempo_contribuicao.value >= 15:
                qualificado = True
                motivo = 'idade'
            elif slider_idade.value < 62 and slider_tempo_contribuicao.value >= 15:
                qualificado = False
                motivo = 'idade'
            elif slider_idade.value >= 62 and slider_tempo_contribuicao.value < 15:
                qualificado = False
                motivo = 'tempo de contribuição'
            elif slider_idade.value < 62 and slider_tempo_contribuicao.value < 15:
                qualificado = False
                motivo = 'idade e tempo'

        elif radio_categoria.value == 'porTempo' and radio_genero.value == 'mulher':
            cat = 'por tempo'
            if slider_tempo_contribuicao.value >= 30:
                qualificado = True
                motivo = 'tempo de contribuição'
            elif slider_tempo_contribuicao.value < 30:
                qualificado = False
                motivo = 'tempo de contribuição'

        if qualificado:
            salario = slider_salario.value
            tmp_delta = calcular_variacao(cat, motivo)
            tmp_delta = tmp_delta[1] * -1
            print(tmp_delta)
            print(salario)
            valor_beneficio = salario * (0.6 + (tmp_delta * 0.02))

            txt_resultado.value = (f'Parabéns! Você se qualifica para a aposentadoria {cat}'
                                   f'O valor estimado do seu benefício é de: {valor_beneficio} R$')
        else:
            lista_delta = calcular_variacao(cat, motivo)
            if motivo == 'idade':
                txt_resultado.value = (f'Você não é capaz de se aposentar {cat}.'
                                       f' pois ainda faltam mais {int(lista_delta[0])} anos de {motivo}.')
            if motivo == 'tempo de contribuição':
                txt_resultado.value = (f'Você não é capaz de se aposentar {cat}.'
                                       f' pois ainda faltam mais {int(lista_delta[1])} anos de {motivo}.')
            else:
                txt_resultado.value = (f'Você não é capaz de se aposentar {cat}.'
                                       f' pois ainda possui pouca {motivo} de contribuição,'
                                       f' faltam {int(lista_delta[0])} {'ano' if int(lista_delta[0]) == 1 else 'anos'} de idade e '
                                       f'{int(lista_delta[1])} {'ano' if int(lista_delta[1]) == 1 else 'anos'} de contribuição.')

    def slider_change_idade(e):
        txt_idade.value = f'IDADE: {int(e.control.value)}'
        page.update()

    def slider_change_tempo(e):
        txt_tempo_contribuicao.value = f'TEMPO DE CONTRIBUIÇÃO: {int(e.control.value)}'
        page.update()

    def slider_salario(e):
        txt_salario.value = f'SALÁRIO: {int(e.control.value)}'
        page.update()

    def calcular_variacao(cat, motivo):
        tmp = slider_tempo_contribuicao.value
        idade = slider_idade.value

        lista_delta = None
        if cat == 'por tempo' and motivo == 'tempo de contribuição':
            if radio_genero.value == 'homem':
                lista_delta = [65 - idade, 35 - tmp]
            else:
                lista_delta = [65 - idade, 30 - tmp]
        elif cat == 'por idade' and motivo == 'tempo de contribuição':
            if radio_genero.value == 'homem':
                lista_delta = [65 - idade, 15 - tmp]
            else:
                lista_delta = [62 - idade, 15 - tmp]
        elif cat == 'por idade' and motivo == 'idade':
            if radio_genero.value == 'homem':
                lista_delta = [65 - idade, 15 - tmp]
            else:
                lista_delta = [62 - idade, 15 - tmp]
        elif cat == 'por idade' and motivo == 'idade e tempo':
            if radio_genero.value == 'homem':
                lista_delta = [65 - idade, 15 - tmp]
            else:
                lista_delta = [62 - idade, 15 - tmp]
        return lista_delta

    def exibir_info(e):
        print('radio genero', radio_genero.value)
        print('radio categoria', radio_categoria.value)
        print('tempo contribuicao', slider_tempo_contribuicao.value)
        print('idade', slider_idade.value)

    def volta(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = gerencia_rotas
    page.go(page.route)
    page.on_view_pop = volta

    #     Criação de componentes
    txt_idade = Text(value='IDADE: 18', size=20, weight=ft.FontWeight.BOLD, bgcolor="cyan")
    slider_idade = ft.Slider(min=18, max=100, divisions=82, label="{value}",
                                  overlay_color="dark_blue", active_color="cyan",
                                  inactive_color="grey", on_change=slider_change_idade)

    txt_tempo_contribuicao = Text(value='TEMPO DE CONTRIBUIÇÃO: 0', size=20, weight=ft.FontWeight.BOLD, bgcolor="cyan")
    slider_tempo_contribuicao = ft.Slider(min=0, max=90, divisions=90, label="{value}",
                             overlay_color="dark_blue", active_color="cyan",
                             inactive_color="grey", on_change=slider_change_tempo)

    txt_salario = Text(value='SALÁRIO: 0', size=20, weight=ft.FontWeight.BOLD, bgcolor="cyan")
    slider_salario = ft.Slider(min=1500, max=10000, divisions=85, label="{value}",
                                          overlay_color="dark_blue", active_color="cyan",
                                          inactive_color="grey", on_change=slider_salario)

    radio_genero = ft.RadioGroup(content=ft.Column([
                                    ft.Radio(value="homem", label="Homem", fill_color={
                                        ft.ControlState.HOVERED: "#191970",
                                        ft.ControlState.DEFAULT: "cyan",
                                    }),
                                    ft.Radio(value="mulher", label="Mulher", fill_color={
                                        ft.ControlState.HOVERED: "#191970",
                                        ft.ControlState.DEFAULT: "cyan",
                                    })]))

    radio_categoria = ft.RadioGroup(content=ft.Column([
                                    ft.Radio(value="porIdade", label="Por idade", fill_color={
                                        ft.ControlState.HOVERED: "#191970",
                                        ft.ControlState.DEFAULT: "cyan",
                                    }),
                                    ft.Radio(value="porTempo", label="Por tempo de contribuição", fill_color={
                                        ft.ControlState.HOVERED: "#191970",
                                        ft.ControlState.DEFAULT: "cyan",
                                    })]))
    txt_resultado = Text(value='', size=24, )

ft.app(main)