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