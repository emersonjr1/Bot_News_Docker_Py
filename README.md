# 🤖 News Bot - Web Scraper com Selenium e Docker
Este projeto é um bot automatizado desenvolvido em Python para coletar notícias de forma eficiente. Ele utiliza Selenium com Chromium em um ambiente Docker, garantindo que o bot funcione de forma idêntica em qualquer servidor ou máquina local.

## 🚀 Funcionalidades
Extração automática: Coleta de notícias de forma programada ou sob demanda.

Modo Headless: Execução em segundo plano (sem interface gráfica), ideal para servidores.

Isolamento total: Ambiente configurado via Docker para evitar conflitos de dependências.

Gestão de pacotes: Gerenciamento simplificado via requirements.txt.

## 🛠️ Tecnologias Utilizadas
Python 3.9+: Linguagem base.

Selenium: Automação da navegação web.

Chromium & Chromium-Driver: Navegador e motor de renderização.

Docker: Containerização e padronização do ambiente.

## 📋 Pré-requisitos
Antes de começar, você precisará ter instalado em sua máquina:

Docker

Docker Compose (opcional, mas recomendado)

## 🔧 Instalação e Execução
1. Clonar o repositório
Bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

2. Construir a Imagem Docker
O Docker lerá o Dockerfile, instalará o Chromium, as dependências do Python e configurará todo o ambiente.

Bash
docker build -t news-bot .

3. Rodar o Container
Bash
docker run news-bot

## 📁 Estrutura do Projeto
Plaintext
|
├── Dockerfile  # Configuração da imagem Docker (Chromium + Python)
|
├── requirements.txt  # Lista de dependências do Python (Selenium, etc)
|
├── bot.py  # Código-fonte principal do bot
|
└── README.md  # Documentação do projeto


## 💡 Detalhes Técnicos Importantes
O bloco if __name__ == "__main__":
O bot utiliza esta estrutura para garantir que a função run_news_bot() seja executada apenas quando o script for chamado diretamente. Isso permite que suas funções sejam importadas por outros módulos ou testes unitários sem disparar a execução do bot acidentalmente.

Configuração do Selenium no Docker
Para rodar dentro de um container Linux de forma estável, o Selenium utiliza as seguintes flags:

--headless: Roda o navegador sem interface visual.

--no-sandbox: Necessário para permissões de execução como root no container.

--disable-dev-shm-usage: Utiliza a memória do sistema em vez de /dev/shm para evitar crashes em partições pequenas.

## 📝 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para detalhes.

### Desenvolvido por Emerson M. Junior 🚀
