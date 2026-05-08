from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def run_news_bot():
    print("--- 🤖 Iniciando Bot de Notícias ---")
    
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.binary_location = "/usr/bin/chromium"
    
    service = Service("/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    try:
        print("🌍 Acessando o portal G1...")
        driver.get("https://g1.globo.com/")
        
        # Espera até 10 segundos para os títulos das notícias aparecerem
        wait = WebDriverWait(driver, 10)
        noticias = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "feed-post-link")))

        print(f"\n✅ Sucesso! Encontrei {len(noticias[:5])} notícias principais:\n")
        
        # Pega as 5 primeiras notícias e imprime o texto e o link
        for i, noticia in enumerate(noticias[:5], 1):
            titulo = noticia.text
            link = noticia.get_attribute("href")
            print(f"{i}. {titulo}")
            print(f"   🔗 {link}\n")

    except Exception as e:
        print(f"❌ Erro durante a execução: {e}")
        
    finally:
        driver.quit()
        print("--- 🏁 Bot finalizado e navegador fechado ---")

if __name__ == "__main__":
    run_news_bot()