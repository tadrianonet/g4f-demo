# Conheça o GPT4Free na prática: repositório demo para sala de aula

*Texto pronto para publicar (blog, LinkedIn ou README de divulgação). Ajuste o link do seu GitHub onde indicado.*

---

## Por que este repositório existe?

Grande parte dos cursos de programação e inteligência artificial hoje passa por **modelos de linguagem**. Muitos alunos ouvem falar de “API da OpenAI”, mas nem sempre têm budget para chave paga ou infraestrutura na primeira aula.

O **[GPT4Free (g4f)](https://github.com/xtekky/gpt4free)** é um projeto open source muito conhecido (dezenas de milhares de estrelas no GitHub) que organiza **vários provedores** e oferece:

- biblioteca **Python** com cliente parecido com a API OpenAI;
- **interface web** local;
- **API REST** compatível com OpenAI;
- imagens Docker prontas para subir em minutos.

Soa útil — mas na primeira vez que alguém clona o repositório principal, a curva pode assustar: dezenas de pastas, provedores diferentes, requisitos de navegador, cookies, documentação extensa.

Este repositório demo (**https://github.com/tadrianonet/g4f-demo**) existe para fechar essa lacuna: **cinco arquivos úteis, um comando, uma resposta na tela**. É o “Hello, world” do g4f para você mostrar aos alunos que *funciona de verdade*.

---

## O que este projeto faz

Em uma frase: **encapsula o uso oficial do pacote `g4f` em exemplos mínimos**, com duas formas de executar:

1. **Docker (recomendado em aula)** — sobe o container oficial do GPT4Free e aponta o script Python para `http://127.0.0.1:8080/v1`. Estável, visual (GUI no navegador) e alinhado ao que o projeto mantém.
2. **Python puro** — igual ao exemplo do README do g4f: `Client()` + `chat.completions.create`, ideal para quem já tem ambiente configurado.

Inclui ainda:

- **`exemplo_chat.py`** — roda no terminal; ótimo para projetar na TV da sala;
- **`app.py`** — interface Streamlit para alunos testarem prompts;
- **`listar_provedores.py`** — mostra o ecossistema de provedores instalados (conceito de “adaptadores”);
- **teste unitário com mock** — prova que o fluxo de código está correto sem depender da rede na CI.

Não há banco de dados, bateria de QA nem juiz automático: só o essencial para **demonstração pedagógica**.

---

## O que o GPT4Free (projeto original) pode fazer

Este demo usa só **chat de texto**, mas o ecossistema completo em [github.com/xtekky/gpt4free](https://github.com/xtekky/gpt4free) vai muito além:

| Capacidade | Uso típico |
|------------|------------|
| Chat com diversos modelos | Prototipar assistentes, tutores, bots |
| API OpenAI-compatível | Integrar apps existentes trocando a URL base |
| Geração de imagens / mídia | Experimentos de criatividade computacional |
| GUI local | Oficinas sem escrever código na primeira hora |
| Cliente JavaScript | Exemplos no navegador via g4f.dev |
| Docker | Laboratório reproduzível na faculdade |

Para quem ensina, o valor não é “substituir” serviços comerciais de forma opaca — é **mostrar arquitetura**: provedores, clientes, timeouts, erros de infraestrutura, limites legais e éticos.

---

## Roteiro sugerido para uma aula de 50 minutos

1. **Contexto (10 min)** — O que é um LLM? O que é uma API de chat? Mostre a documentação oficial: [g4f.dev/docs](https://g4f.dev/docs).
2. **Demo Docker (15 min)** — `docker compose up -d`, abrir `localhost:8080`, enviar uma pergunta na GUI.
3. **Código (15 min)** — Abrir `exemplo_chat.py` e `chat.py`; comparar com o snippet do README do g4f.
4. **Hands-on (10 min)** — Alunos rodam `streamlit run app.py` ou alteram o prompt no CLI.
5. **Fechamento (5 min)** — Limitações, [LEGAL_NOTICE](https://github.com/xtekky/gpt4free/blob/main/LEGAL_NOTICE.md), quando usar API paga oficial.

---

## Como reproduzir em casa (resumo)

```bash
git clone https://github.com/tadrianonet/g4f-demo.git
cd g4f-demo
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
docker compose up -d
echo 'G4F_API_BASE=http://127.0.0.1:8080/v1' >> .env
python exemplo_chat.py "Explique HTTP em duas frases."
```

Se aparecer resposta no terminal, a cadeia **Python → g4f → API local** está funcionando.

---

## Limitações honestas (importante para alunos)

- Provedores gratuitos **quebram, mudam e exigem login** com frequência; por isso recomendamos Docker em apresentações.
- **Não há garantia** de qual modelo está por trás de cada resposta; em produção use APIs contratadas e rastreáveis.
- Respeite termos de uso, direitos autorais e políticas da instituição de ensino.

---

## Conclusão

O GPT4Free é um **hub open source** para experimentar LLMs e APIs compatíveis com OpenAI. Este repositório demo não compete com o projeto original — **complementa**: tira o ruído, deixa só o caminho feliz e o roteiro de aula.

Se você leciona Python, APIs ou IA, clone, teste e adapte. Pull requests com traduções, exercícios para alunos ou integração com LMS são bem-vindas.

**Links**

- Projeto original: https://github.com/xtekky/gpt4free  
- Demo para aula: https://github.com/tadrianonet/g4f-demo  
- Documentação: https://g4f.dev/docs  

---
