from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def configurar_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    # Caminhos padrão para Chromium no Docker (ajuste se necessário)
    chrome_options.binary_location = "/usr/bin/chromium"
    
    service = Service("/usr/bin/chromedriver")
    return webdriver.Chrome(service=service, options=chrome_options)

def run_news_bot():
    print("--- 🤖 Iniciando Bot Multi-Notícias ---")
    
    # Mapeamento de sites e seus seletores CSS
    portais = [
        {
            "nome": "G1 Globo",
            "url": "https://g1.globo.com/",
            "seletor": ".feed-post-link"
        },
        {
            "nome": "CNN Brasil",
            "url": "https://www.cnnbrasil.com.br/",
            "seletor": ".home__post" # Seletor principal da home da CNN
        },
        {
            "nome": "BBC Brasil",
            "url": "https://www.bbc.com/portuguese",
            "seletor": "h3 a" # Títulos com links na BBC
        }
    ]

    driver = configurar_driver()
    
    try:
        for portal in portais:
            print(f"\n🌍 Acessando: {portal['nome']}...")
            driver.get(portal['url'])
            
            # Espera carregar os elementos
            wait = WebDriverWait(driver, 10)
            
            try:
                noticias = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, portal['seletor'])))
                
                print(f"✅ Encontrei {len(noticias[:3])} notícias principais no {portal['nome']}:")
                
                for i, noticia in enumerate(noticias[:3], 1):
                    titulo = noticia.text.strip()
                    link = noticia.get_attribute("href")
                    
                    # Garante que não imprima linhas vazias (comum em alguns layouts)
                    if titulo:
                        print(f"  {i}. {titulo}")
                        print(f"     🔗 {link}")
            
            except Exception as e:
                print(f"⚠️ Não foi possível carregar notícias de {portal['nome']}.")

    except Exception as e:
        print(f"❌ Erro crítico: {e}")
        
    finally:
        driver.quit()
        print("\n--- 🏁 Bot finalizado e navegador fechado ---")

if __name__ == "__main__":
    run_news_bot()