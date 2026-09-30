# g4f-demo

Demonstração educacional em Python para integrar modelos de linguagem via **[GPT4Free (g4f)](https://github.com/xtekky/gpt4free)** — cliente compatível com a API OpenAI, múltiplos provedores e stack Docker oficial.

Este repositório **não é um fork** do g4f. É um projeto mínimo, focado em **aula e prototipagem**: instalar, executar, obter resposta na tela e discutir limites reais de provedores gratuitos.

**Repositório:** [github.com/tadrianonet/g4f-demo](https://github.com/tadrianonet/g4f-demo)

---

## Objetivo

- Mostrar o fluxo **Python → g4f → modelo** com poucos arquivos e código legível.
- Oferecer interface **Streamlit** e script **CLI** para laboratório.
- Tratar respostas em **HTML** e erros de **RetryProvider** de forma didática (sem despejar logs brutos na UI).
- Recomendar **Docker** como caminho estável quando provedores públicos falham (auth, pagamento, indisponibilidade).

---

## Requisitos

| Requisito | Observação |
|-----------|------------|
| Python **3.10+** | Recomendado **3.11** (`g4f` não roda em 3.9) |
| pip / venv | Ambiente isolado obrigatório |
| Docker Desktop | Opcional; **recomendado** para apresentações |
| Navegador | Streamlit em `localhost:8501`; GUI g4f em `localhost:8080` (com Docker) |

Leia o [aviso legal do g4f](https://github.com/xtekky/gpt4free/blob/main/LEGAL_NOTICE.md) antes de usar em instituição de ensino.

---

## Instalação

No macOS, o `python3` do sistema costuma ser **3.9** (Streamlit pode abrir em branco ou o CLI encerra). Use 3.11 explicitamente:

```bash
git clone https://github.com/tadrianonet/g4f-demo.git
cd g4f-demo

python3.11 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate

pip install -r requirements.txt
cp .env.example .env
```

Se não tiver Python 3.11: `brew install python@3.11` (macOS).

O `requirements.txt` já inclui `g4f[all]` (dependências extras dos provedores).

---

## Configuração (`.env`)

| Variável | Padrão | Descrição |
|----------|--------|-----------|
| `G4F_MODEL` | `gpt-4o-mini` | Nome do modelo reconhecido pelo g4f |
| `G4F_PROVIDER` | vazio | Provedor fixo (nome exato; veja `listar_provedores.py`) |
| `G4F_API_BASE` | vazio | URL da API OpenAI-compatível (ex.: container local) |

Exemplo para **API local via Docker**:

```env
G4F_MODEL=gpt-4o-mini
G4F_API_BASE=http://127.0.0.1:8080/v1
```

---

## Modos de execução

### Modo A — Docker (recomendado em sala de aula)

Sobe a imagem mantida pelo ecossistema g4f:

```bash
docker compose up -d
```

| Serviço | URL |
|---------|-----|
| GUI / API g4f | http://localhost:8080 |
| Demo Streamlit (separado) | http://localhost:8501 |

Defina `G4F_API_BASE` no `.env` (acima) e teste:

```bash
python exemplo_chat.py "Explique o que é um LLM em duas frases."
streamlit run app.py
```

### Modo B — Cliente Python direto

Sem Docker, o `Client()` do g4f pode alternar entre provedores públicos (comportamento documentado no projeto original):

```bash
python exemplo_chat.py "Olá"
python listar_provedores.py --model gpt-4o-mini
```

Falhas de autenticação ou assinatura são esperadas neste modo; a interface resume o erro e sugere Docker.

---

## Estrutura do projeto

| Módulo | Responsabilidade |
|--------|------------------|
| `chat.py` | `enviar_mensagem()` — integração com `g4f.client.Client` |
| `exemplo_chat.py` | Entrada CLI para demonstrações |
| `app.py` | Interface Streamlit |
| `config.py` | Leitura de variáveis de ambiente |
| `formatar_resposta.py` | Converte HTML de provedores em Markdown legível |
| `formatar_erro.py` | Resume falhas agregadas (`RetryProviderError`, etc.) |
| `listar_provedores.py` | Catálogo estático de provedores instalados |
| `verificar_python.py` | Garante Python 3.10+ |
| `docker-compose.yml` | Serviço `hlohaus789/g4f:latest` |

---

## Testes

Testes unitários com mocks (sem chamadas de rede):

```bash
pytest
```

---

## Solução de problemas

| Sintoma | Causa provável | Ação |
|---------|----------------|------|
| Streamlit em tela vazia | Python 3.9 no venv | Recrie o venv com `python3.11` |
| `exige Python 3.10` no terminal | Mesmo caso | `brew install python@3.11` e novo venv |
| Parede de erros de provedores | Modo automático sem Docker | `docker compose up -d` + `G4F_API_BASE` |
| Tags HTML na resposta | Provedor devolve HTML | Já tratado em `formatar_resposta` no app |
| `ModuleNotFoundError` g4f | Instalação incompleta | `pip install -r requirements.txt` |

---

## Possibilidades de extensão

- Integrar o mesmo `chat.enviar_mensagem()` em bot, API Flask/FastAPI ou atividade no LMS.
- Comparar provedores com `listar_provedores.py` em aula de arquitetura de software.
- Evoluir para o ecossistema completo do g4f: geração de mídia, Interference API, GUI em [g4f.dev/docs](https://g4f.dev/docs).

---

## Referências

- GPT4Free (upstream): [github.com/xtekky/gpt4free](https://github.com/xtekky/gpt4free)
- Documentação: [g4f.dev/docs](https://g4f.dev/docs)
- Cliente Python: [g4f.dev/docs/client](https://g4f.dev/docs/client)

---

## Uso responsável

O g4f é distribuído sob **GPL-3.0**. Utilize este demo apenas para **ensino e experimentação**. Provedores terceiros podem exigir credenciais, impor limites ou alterar comportamento sem aviso. Não utilize para contornar pagamentos ou termos de serviço. Em produção, prefira APIs contratadas, rastreáveis e alinhadas à política da sua organização.
