import flet as ft
from deep_translator import GoogleTranslator

def main(page: ft.Page):
    # --- CONFIGURACIÓN DE LA PÁGINA ---
    page.title = "Traductor Universal Pro"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 450
    page.window_height = 800
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 30
    page.bgcolor = "#F5F7FA"  # Un gris muy claro y elegante

    # --- LÓGICA DE TRADUCCIÓN ---
    def realizar_traduccion(e):
        if not entrada_texto.value.strip():
            entrada_texto.error_text = "Por favor, escribe algo para traducir"
            page.update()
            return
        
        # Mostrar indicador de carga
        progreso.visible = True
        boton_traducir.disabled = True
        entrada_texto.error_text = None
        page.update()

        try:
            # Traducir (Detecta idioma auto -> Español)
            resultado_traducido = GoogleTranslator(source='auto', target='es').translate(entrada_texto.value)
            texto_resultado.value = resultado_traducido
            contenedor_resultado.visible = True
        except Exception as ex:
            texto_resultado.value = f"Error de conexión: Verifica tu internet."
            contenedor_resultado.visible = True
        finally:
            progreso.visible = False
            boton_traducir.disabled = False
            page.update()

    def limpiar_todo(e):
        entrada_texto.value = ""
        texto_resultado.value = ""
        contenedor_resultado.visible = False
        page.update()

    # --- ELEMENTOS DE LA INTERFAZ (UI) ---
    
    # Encabezado
    header = ft.Column(
        controls=[
            ft.Icon(name=ft.icons.TRANSLATE_ROUNDED, color=ft.colors.BLUE_700, size=50),
            ft.Text("Traductor Pro", size=28, weight="bold", color=ft.colors.BLUE_900),
            ft.Text("De cualquier idioma al Español", size=14, color=ft.colors.BLUE_GREY_400),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    # Campo de entrada
    entrada_texto = ft.TextField(
        label="Escribe aquí el texto",
        hint_text="Ej: Hello world / Bonjour tout le monde...",
        multiline=True,
        min_lines=4,
        max_lines=8,
        border_radius=15,
        border_color=ft.colors.BLUE_200,
        focused_border_color=ft.colors.BLUE_700,
        bgcolor=ft.colors.WHITE,
    )

    progreso = ft.ProgressBar(width=400, color="blue", visible=False)

    # Botones
    boton_traducir = ft.ElevatedButton(
        text="Traducir ahora",
        icon=ft.icons.BOLT,
        on_click=realizar_traduccion,
        style=ft.ButtonStyle(
            color=ft.colors.WHITE,
            bgcolor=ft.colors.BLUE_700,
            padding=20,
            shape=ft.RoundedRectangleBorder(radius=12),
        ),
    )

    boton_limpiar = ft.TextButton(
        "Limpiar", 
        icon=ft.icons.DELETE_OUTLINE, 
        on_click=limpiar_todo
    )

    # Contenedor de Resultado
    texto_resultado = ft.Text("", size=18, color=ft.colors.BLUE_GREY_900, weight="w500")
    
    contenedor_resultado = ft.Container(
        content=ft.Column([
            ft.Text("Traducción:", size=12, weight="bold", color=ft.colors.BLUE_700),
            texto_resultado,
        ]),
        visible=False,
        padding=20,
        bgcolor=ft.colors.WHITE,
        border_radius=15,
        border=ft.border.all(1, ft.colors.BLUE_100),
        shadow=ft.BoxShadow(blur_radius=10, color=ft.colors.with_opacity(0.1, "black"))
    )

    # --- ENSAMBLAJE FINAL ---
    page.add(
        header,
        ft.Divider(height=30, color="transparent"),
        entrada_texto,
        ft.Divider(height=10, color="transparent"),
        progreso,
        ft.Row([boton_traducir, boton_limpiar], alignment=ft.MainAxisAlignment.CENTER),
        ft.Divider(height=20, color="transparent"),
        contenedor_resultado
    )

if __name__ == "__main__":
    ft.app(target=main)