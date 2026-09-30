# g4f-demo

Repositório educacional que mostra como usar o **[GPT4Free (g4f)](https://github.com/xtekky/gpt4free)** — projeto open source que reúne vários provedores e uma API compatível com OpenAI.

Não é um fork do g4f: é um **exemplo mínimo** para você instalar, executar na sala de aula e provar que a integração funciona.

## Requisitos

- **Python 3.10+** (recomendado 3.11)
- **Docker** (opcional, mas recomendado para demo estável)
- Leia também o [aviso legal do g4f](https://github.com/xtekky/gpt4free/blob/main/LEGAL_NOTICE.md)

## Instalação rápida

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
```

Para todos os recursos dos provedores (navegador, etc.):

```bash
pip install -U "g4f[all]"
```

## Forma 1 — Docker (melhor para apresentar aos alunos)

Sobe a imagem oficial do projeto:

```bash
docker compose up -d
```

Abra no navegador: **http://localhost:8080**

Configure o `.env`:

```env
G4F_API_BASE=http://127.0.0.1:8080/v1
G4F_MODEL=gpt-4o-mini
```

Teste no terminal:

```bash
python exemplo_chat.py "Olá, responda em uma frase."
```

Interface Streamlit deste repositório:

```bash
streamlit run app.py
```

## Forma 2 — Python direto (como no README do g4f)

Sem Docker, o cliente Python escolhe um provedor automaticamente:

```bash
python exemplo_chat.py
```

Se der erro de dependência ou autenticação, liste opções:

```bash
python listar_provedores.py --model gpt-4o-mini
```

Fixar um provedor no `.env`:

```env
G4F_PROVIDER=OpenaiChat
```

## Arquivos

| Arquivo | Função |
|---------|--------|
| `exemplo_chat.py` | Script de demonstração na linha de comando |
| `chat.py` | Função reutilizável `enviar_mensagem` |
| `app.py` | Interface web simples (Streamlit) |
| `listar_provedores.py` | Lista provedores do pacote instalado |
| `docker-compose.yml` | Container oficial `hlohaus789/g4f` |
| `ARTIGO.md` | Texto pronto para blog / LinkedIn sobre este repo |

## Teste automatizado (sem internet)

```bash
pip install pytest
pytest
```

## Links oficiais

- Repositório: https://github.com/xtekky/gpt4free  
- Documentação: https://g4f.dev/docs  
- Cliente Python: https://g4f.dev/docs/client  

## Licença e uso em aula

O g4f é software comunitário (GPL-3.0). Use este demo apenas para **ensino** e deixe claro que provedores terceiros podem exigir login, ter limites ou mudar a qualquer momento. Não use para burlar pagamentos ou termos de serviço.
