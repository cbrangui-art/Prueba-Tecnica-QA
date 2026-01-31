class LoginPage:
    def __init__(self, page):
        self.page = page
        # Selectores
        self.input_usuario = page.locator('input[name="usuario"], input[placeholder*="Usuario"], input[type="text"]')
        self.input_password = page.locator('input[name="password"], input[type="password"]')
        self.btn_login = page.locator('button[type="submit"], button:has-text("Ingresar")')

    def navegar(self):
        print("[LOG] Abriendo página")
        self.page.goto("https://pruebasportaldatos.enlace.com.co/login", wait_until="networkidle")

    def login_completo(self, usuario, clave):
        print(f"[LOG] Ingresamos con: {usuario}")
        
        self.input_usuario.first.wait_for(state="visible", timeout=10000)
        
        # Datos usuario y contraseña
        self.input_usuario.first.fill(usuario)
        self.input_password.first.fill(clave)
        
        print("[LOG] Botón de ingreso")
        self.btn_login.first.click()

    def obtener_mensaje_error(self):
       
        selector_error = "div[role='alert'].alert-danger"
        try:
            self.page.wait_for_selector(selector_error, state="visible", timeout=5000)
            print(f"[LOG] Mensaje de error: {self.page.locator(selector_error).inner_text()}")
            return True
        except:
            print("[LOG] No se detectó el mensaje de alerta.")
            return False