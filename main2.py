import flet as ft

def main(page: ft.Page):
    # Configuração da página
    page.title = "Minha Aplicação Flet"
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeMode.LIGHT
    page.window.width = 375
    page.window.height = 667

    # Definição de fuções
    def numero_par_impar(e):
        if int(input_numero.value) != 0:
            if int(input_numero.value) % 2 == 0:
                txt_resultado.value = "Esse número é par!"
            else:
                txt_resultado.value = "Esse número é Ímpar!"
        else:
            txt_resultado.value = 'Escolha outro número'
        page.update()

    # Criação de componentes
    input_numero = ft.TextField(
        label="Número: ",
        color="lightgreen",
    )
    btn_enviar = ft.FilledButton(
        text="Enviar",
        width=page.window.width,
        on_click=numero_par_impar,
    )

    txt_resultado = ft.Text(value="")

    # Construir o layout
    page.add(
        ft.Column(
            [
                input_numero,
                btn_enviar,
                txt_resultado,
            ]
        )
    )


ft.app(main)
