class LoginPage:
    def __init__(self, page):
        self.page = page
        # Definimos los selectores de forma más flexible
        self.input_usuario = page.locator('input[name="usuario"], input[placeholder*="Usuario"], input[type="text"]')
        self.input_password = page.locator('input[name="password"], input[type="password"]')
        self.btn_login = page.locator('button[type="submit"], button:has-text("Ingresar")')

    def navegar(self):
        print("[LOG] Abriendo portal...")
        self.page.goto("https://pruebasportaldatos.enlace.com.co/login", wait_until="networkidle")

    def login_completo(self, usuario, clave):
        print(f"[LOG] Intentando ingresar con: {usuario}")
        
        # Esperamos explícitamente a que el campo aparezca
        self.input_usuario.first.wait_for(state="visible", timeout=10000)
        
        # Escribimos usando el primer elemento que coincida
        self.input_usuario.first.fill(usuario)
        self.input_password.first.fill(clave)
        
        print("[LOG] Haciendo clic en el botón de ingreso...")
        self.btn_login.first.click()