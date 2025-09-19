import flet as ft
from services import adicionar_meta, progresso_meta, iniciar_timer, verificar_dia
from persistence import salvar_usuario, carregar_usuario

def main(page: ft.Page):
    
    page.title = "Gerenciador de Metas"
    page.scroll = "adaptive"
    page.padding = 20

    usuario = carregar_usuario()
    verificar_dia(usuario)  # <<< garante reset ao abrir
    
    metas_list = ft.Column()
    dias_text = ft.Text(f"Dias consecutivos: {usuario.dias_consecutivos}", size=16, weight="bold")

    def salvar():
        salvar_usuario(usuario)
        dias_text.value = f"Dias consecutivos: {usuario.dias_consecutivos}"
        page.update()

    def atualizar_lista():
        metas_list.controls.clear()
        for meta in usuario.metas:
            barra = ft.ProgressBar(value=progresso_meta(meta), width=200)

            def iniciar_timer_meta(e, m=meta, b=barra, t=ft.Text()):
                def atualizar_ui(meta_atualizada):
                    b.value = progresso_meta(meta_atualizada)
                    t.value = f"{meta_atualizada.progresso_diario.seconds//60}/{meta_atualizada.tempo_diario.seconds//60} min"
                    page.update()

                iniciar_timer(m, usuario, atualizar_ui, salvar)

            texto_tempo = ft.Text(f"{meta.progresso_diario.seconds//60}/{meta.tempo_diario.seconds//60} min")
            btn_iniciar = ft.ElevatedButton("Iniciar", on_click=lambda e, m=meta: iniciar_timer_meta(e, m, barra, texto_tempo))

            metas_list.controls.append(
                ft.Row([
                    ft.Text(meta.nome),
                    barra,
                    texto_tempo,
                    btn_iniciar
                ])
            )
        page.update()

    def add_meta(e):
        if input_meta.value:
            adicionar_meta(usuario, input_meta.value, int(input_min.value or 30))
            salvar()
            input_meta.value = ""
            input_min.value = ""
            atualizar_lista()

    input_meta = ft.TextField(label="Nova Meta")
    input_min = ft.TextField(label="Minutos p/dia", width=100)
    btn_add = ft.ElevatedButton("Adicionar", on_click=add_meta)

    page.add(
        ft.Text("Suas Metas", size=20),
        dias_text,
        ft.Row([input_meta, input_min, btn_add]),
        metas_list
    )

    atualizar_lista()