import flet as ft

def main(page: ft.Page):
    # Configuração da página
    page.title = "Minha Aplicação Flet"
    page.theme_mode = ft.ThemeMode.DARK # ou ft.ThemeMode.LIGHT
    page.window.width = 375
    page.window.height = 667

    # Definição de fuções
    def mostrar_soma(e):
        soma = int(input_numero1.value) + int(input_numero2.value)
        txt_resultado.value = soma
        page.update()

    def mostrar_subtracao(e):
        subtracao = int(input_numero1.value) - int(input_numero2.value)
        txt_resultado.value = subtracao
        page.update()

    def mostrar_multiplicacao(e):
        multiplicacao = int(input_numero1.value) * int(input_numero2.value)
        txt_resultado.value = multiplicacao
        page.update()

    def mostrar_divisao(e):
        divisao = int(input_numero1.value) * int(input_numero2.value)
        txt_resultado.value = divisao
        page.update()

    # Criação de componentes
    input_numero1 = ft.TextField(label="Número: ",
                            hint_text="Digite o primeiro número",
                            )
    input_numero2 = ft.TextField(label="Número: ",
                            hint_text="Digite o segundo número",)



    btn_soma = ft.FilledButton(text="Soma",
                            width=page.window.width,
                            on_click=mostrar_soma,
                            )

    btn_subtracao = ft.FilledButton(text="Subtrair",
                            width=page.window.width,
                            on_click=mostrar_subtracao,
                            )

    btn_divisao = ft.FilledButton(text="Dividir",
                            width=page.window.width,
                            on_click=mostrar_divisao,
                            )

    btn_multiplicacao = ft.FilledButton(text="Multiplicar",
                            width=page.window.width,
                            on_click=mostrar_multiplicacao,
                            )
    
    txt_resultado = ft.Text(value="")

    # Construir o layout
    page.add(
        ft.Column(
            [
                input_numero1,
                input_numero2,
                btn_soma,
                btn_subtracao,
                btn_divisao,
                btn_multiplicacao,
                txt_resultado,
            ]
        )
    )

ft.app(main)