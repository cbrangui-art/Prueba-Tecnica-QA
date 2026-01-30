from pages.login_pages import LoginPage
from pages.cotizantes_page import CotizantesPage

def test_escenarios(page):
   
    login = LoginPage(page)
    cotizantes = CotizantesPage(page)

    
    print("\n[log] inicio")
    
    # Login
    login.navegar()
    login.login_completo("pruebasqa@enlace.com.co", "Prueba1234567890*")
    
    # Consulta y descarga
    cotizantes.consultar_y_exportar("1143382658")
    
    print("[log] Exitoso")



    