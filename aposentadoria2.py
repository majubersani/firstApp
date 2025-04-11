import flet as ft
from flet import AppBar, ElevatedButton, Text, View, colors
from flet.core.app_bar import AppBar
from flet.core.colors import Colors

def main (page: ft.Page):
    #Configuração da página
    page.title = "Simulação de Aposentadoria"
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

ft.app(main)