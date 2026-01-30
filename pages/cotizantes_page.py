class CotizantesPage:
    def __init__(self, page):
        self.page = page
        self.menu_rci = page.get_by_text("Cotizantes RCI").nth(1)
        self.tipo_doc_select = page.get_by_label("Default select example")
        self.doc_input = page.get_by_role("textbox", name="Número de documento *")
        self.btn_buscar = page.get_by_role("button", name="Buscar")
        self.btn_exportar = page.get_by_role("button", name="Exportar a CSV")

    def consultar_y_exportar(self, numero_doc):
        print(f"[LOG] Navegando a Cotizantes RCI...")
        self.menu_rci.click()
        
        print(f"[LOG] Consultando documento: {numero_doc}")
        self.tipo_doc_select.select_option("CC")
        self.doc_input.fill(numero_doc)
        self.btn_buscar.click()

        print("[LOG] Iniciando descarga de CSV...")
        with self.page.expect_download() as download_info:
            self.btn_exportar.click()
        
        download = download_info.value
        # Guardar archivo
        path = f"./downloads/{download.suggested_filename}"
        download.save_as(path)
        print(f"[LOG] Archivo guardado en: {path}")