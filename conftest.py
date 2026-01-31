import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def page(request):
    
    with sync_playwright() as p:
        # Abre navegador 
        headed = request.config.getoption("--headed", default=False)
        browser = p.chromium.launch(headless=not headed) 
        context = browser.new_context()
        page = context.new_page()
        
        yield page 
        
        # Cierre navegador
        browser.close()

# Ocultar Environment del reporte
def pytest_configure(config):
    config._metadata = None

# Agregar CSS para ocultar Environment
def pytest_html_report_title(report):
    report.title = "Reporte"
    
@pytest.hookimpl(hookwrapper=True)
def pytest_html_results_table_html(report, data):
    outcome = yield
    
def pytest_html_results_summary(prefix, summary, postfix):
    # Oculta Environment con CSS
    prefix.append('<style>#environment-header, #environment { display: none !important; }</style>')