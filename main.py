from models import Usuario, Meta, Estado
import os
import time
import msvcrt

class SistemaMetas:
    def __init__(self):
        self.usuario = Usuario("José")

    # ------------------------------
    # Funções utilitárias
    # ------------------------------
    def clear(self):
        os.system("cls||clear")

    def mostrar_titulo(self):
        print(" ____ ____ ____ ____ ____ ____ ____ _________ ____ ____ _________ ____ ____ ____ ____ ____ _________ ")
        print("||S |||i |||s |||t |||e |||m |||a |||       |||d |||e |||       |||M |||e |||t |||a |||s |||       ||")
        print("||__|||__|||__|||__|||__|||__|||__|||_______|||__|||__|||_______|||__|||__|||__|||__|||__|||_______||")
        print("|/__\\|/__\\|/__\\|/__\\|/__\\|/__\\|/__\\|/_______\\|/__\\|/__\\|/_______\\|/__\\|/__\\|/__\\|/__\\|/__\\|/_______\\|")
        print("Painel Geral do Sistema de Metas - Sistema v0.3\n")

    # ------------------------------
    # Painel interativo de uma meta
    # ------------------------------
    def rodar_meta(self, meta: Meta):
        meta.iniciar_timer()
        try:
            while meta._estado != Estado.CONCLUIDA:
                self.clear()
                self.mostrar_titulo()
                nome, tempo, estado, progresso = meta.get_descricao()
                print(f"{nome}: {estado}, progresso {progresso}/{tempo}")
                print("Comandos: [P]ausar, [R]etomar, [S]top, [Q]uit painel")

                if msvcrt.kbhit():
                    key = msvcrt.getwch().lower()
                    if key == "p":
                        meta.pausar()
                    elif key == "r":
                        meta.retomar()
                    elif key == "s":
                        meta.parar()
                    elif key == "q":
                        meta.pausar()
                        self.menu_principal()
                time.sleep(1)
        finally:
            meta.parar()
            print(f"\nMeta '{meta._nome}' finalizada ou painel fechado.")
            time.sleep(1)

    # ------------------------------
    # Menu principal
    # ------------------------------
    def menu_principal(self):
        while True:
            self.clear()
            self.mostrar_titulo()

            if self.usuario.get_metas():
                print("Metas cadastradas:")
                for index, m in enumerate(self.usuario.get_metas()):
                    nome, tempo, estado, progresso = m.get_descricao()
                    print(f" - [N° {index}] {nome}: {estado}, progresso {progresso}/{tempo}")
            else:
                print("Nenhuma meta cadastrada.")

            # Menu de opções
            print("\nComandos:")
            print("[1] Criar nova meta")
            print("[2] Rodar painel de uma meta")
            print("[3] Excluir meta")
            print("[E] Sair")

            opc = input("\nDigite uma opção: ").strip().lower()

            if opc == "1":
                nome = input("Nome da meta: ").strip().lower()
                while True:
                    tempo = input("Tempo em minutos: ")
                    if tempo.isdecimal():
                        break
                    else:
                        print("Entrada inválida - Digite o tempo utilizando NÚMEROS")

                meta = Meta(nome=nome, minutos_diarios=int(tempo))
                self.usuario.adicionar_meta(meta)
                print(f"✅ Meta '{nome}' criada!")
                time.sleep(2)

            elif opc == "2":
                while True:
                    posicao = input("Digite o número da meta para abrir o painel: ")
                    if posicao.isdecimal():
                        break
                    else:
                        print("\nEntrada inválida - Digite o NÚMERO referente a meta")
                try:
                    self.usuario.get_metas()[int(posicao)]
                    self.rodar_meta(meta)
                except IndexError:
                    print("❌ Meta não encontrada.")
                    time.sleep(2)

            elif opc == "3":
                while True:
                    posicao = input("Digite o número da meta para excluir: ")
                    if posicao.isdecimal():
                        break
                    else:
                        print("\nEntrada inválida - Digite o NÚMERO referente a meta")
                try:
                    meta = self.usuario.get_metas()[int(posicao)]
                    self.usuario.excluir_meta(meta)
                    self.usuario.get_metas()
                except IndexError:
                    print("❌ Meta não encontrada.")
                    time.sleep(2)

            elif opc == "e":
                print("Saindo do sistema...")
                for m in self.usuario.get_metas():
                    m.parar()
                break

            else:
                print("❌ Comando inválido.")
                time.sleep(1)


if __name__ == "__main__":
    sistema = SistemaMetas()
    sistema.menu_principal()