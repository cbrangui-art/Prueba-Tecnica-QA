from pages.login_page import LoginPage
from pages.cotizantes_page import CotizantesPage

# Escenario exitoso
def test_completo(page):
    login = LoginPage(page)
    cotizantes = CotizantesPage(page)

    print("\n[LOG] ESCENARIO EXITOSO")
    login.navegar()
    login.login_completo("pruebasqa@enlace.com.co", "Prueba1234567890*")
    cotizantes.consultar_y_exportar("1143382658")
    print("[LOG] Caso exitoso")

# Escenario fallido 1 (contraseña incorrecta,genera error)
def test_login_incorrecto1(page):
    login = LoginPage(page)
    print("\n[LOG] CONTRASEÑA INCORRECTA")
    login.navegar()
    login.login_completo("pruebasqa@enlace.com.co", "prueba123*")
    
    assert login.obtener_mensaje_error(), " Usuario o contraseña incorrectos "
    print("[LOG] CREDENCIALES INCORRECTAS")
  
# Escenario fallido 2 (ingreso mal usuario y contraseña) 
def test_login_incorrecto2(page):
    login = LoginPage(page)
    print("\n[LOG] USUARIO Y CONTRASEÑA INCORRECTOS")
    login.navegar()
    login.login_completo("pruebasqa@enlace.com.co", "prueba123*")
    
    assert login.obtener_mensaje_error(), " Usuario o contraseña incorrectos "
    print("[LOG] CREDENCIALES INCORRECTAS")
  