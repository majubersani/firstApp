import flet as ft

def main (page: ft.Page):
    #Configuração da página
    page.title = "Minha Aplicação Flet"
    page.theme_mode = ft.ThemeMode.DARK # ou ft.themeMode.LIGHT
    page.window.width = 375
    page.window.height = 667

    #Definição de funções
    def mostrar_nome_sobrenome(e):
        txt_resultado.value = f'{input_nome.value} {input_sobrenome.value}'
        page.update()


    #Criação de componentes
    input_nome = ft.TextField(label="Nome",
                              hint_text="Digite seu nome"
                              )
    input_sobrenome = ft.TextField(label="Sobrenome",
                              hint_text="Digite seu sobrenome"
                              )
    btn_enviar = ft.FilledButton(
        text="Enviar",
        width=page.window.width,
        on_click=mostrar_nome_sobrenome,
    )
    txt_resultado = ft.Text(value="")

    #Construir o layout
    page.add(
        ft.Column(
            [
                input_nome,
                input_sobrenome,
                btn_enviar,
                txt_resultado,
            ]
        )
    )

ft.app(main)