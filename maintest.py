import flet as ft

def maintest(page: ft.Page):
    page.title = "METAstic - Gerenciador de Metas"
    page.horizontal_alignment = "center"
    page.scroll = "adaptive"
    page.padding = 20

    # Estado do usuário
    dias_consecutivos = ft.Text("0: Dias Consecutivos", size=14, weight="bold")

    # Campos de entrada para nova meta
    input_nome = ft.TextField(label="Nova Meta", width=300)
    input_tempo = ft.TextField(label="Min p/dia", width=120, keyboard_type=ft.KeyboardType.NUMBER)
    btn_add = ft.ElevatedButton("Adicionar")

    # Lista de metas (container principal)
    metas_column = ft.Column(spacing=10)

    def adicionar_meta(e):
        if not input_nome.value or not input_tempo.value.isdigit():
            return
        
        nome = input_nome.value
        tempo_total = int(input_tempo.value)
        progresso = 20  # teste inicial fixo
        estado = "ativo" if len(metas_column.controls) % 2 == 0 else "inativo"

        # Barra de progresso
        barra = ft.ProgressBar(value=progresso/tempo_total if tempo_total > 0 else 0, width=300)

        # Label superior (nome e estado)
        lbl = ft.Row([
            ft.Text(f"{nome} - {estado}", size=14, weight="bold"),
            ft.Text(f"{progresso}/{tempo_total} min", size=14)
        ], alignment="spaceBetween")

        # Linha da meta
        linha_meta = ft.Container(
            content=ft.Column([
                lbl,
                barra,
                ft.Row([
                    ft.ElevatedButton("Iniciar", bgcolor=ft.Colors.GREEN, color=ft.Colors.WHITE),
                    ft.ElevatedButton("Parar", bgcolor=ft.Colors.RED, color=ft.Colors.WHITE),
                ], spacing=10)
            ]),
            padding=10,
            border=ft.border.all(1, ft.Colors.GREY),
            border_radius=5
        )

        metas_column.controls.append(linha_meta)
        page.update()

    btn_add.on_click = adicionar_meta

    # Layout principal
    page.add(
        ft.Column([
            ft.Row([input_nome, input_tempo, btn_add], spacing=10),
            dias_consecutivos,
            ft.Container(
                content=metas_column,
                padding=10,
                border=ft.border.all(1, ft.Colors.GREY_400),
                border_radius=5,
                width=500
            )
        ], spacing=20)
    )

ft.app(target=maintest)