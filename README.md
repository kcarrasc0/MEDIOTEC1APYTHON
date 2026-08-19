# Construindo Interfaces Mobile com Python e Flet

Bem-vindos, devs! Neste repositório, vamos transformar nossos protótipos visuais feitos no Figma em aplicativos reais utilizando a linguagem Python.

Para facilitar nosso trabalho no GitHub Codespaces, vamos utilizar a biblioteca **Flet**. Ela permite criar interfaces modernas usando a mesma lógica de design do Figma e roda o nosso aplicativo diretamente em uma aba do seu navegador, sem a necessidade de configurações complexas!

---

## Passo 1: Preparando o Ambiente (Terminal)

Antes de começar a programar, precisamos instalar a biblioteca Flet no nosso ambiente virtual. 

1. Abra o **Terminal** na parte inferior da tela do seu Codespaces.
2. Digite o comando abaixo e aperte **Enter**:

`pip install flet`

*Aguarde a barra de progresso terminar a instalação.*

## Passo 2: Organizando as Imagens (Assets)

Se o seu projeto utilizar imagens (como avatares, mapas, produtos ou a Caixa dos Devs), o Python precisa de um local específico para encontrá-las.

1. Crie uma pasta chamada **`assets`** (tudo em letras minúsculas) na raiz do seu projeto, no mesmo local onde está o seu arquivo `main.py`.
2. Arraste as suas imagens (`.png`, `.jpg`) para dentro dessa pasta.

## Passo 3: Executando o seu Aplicativo

Com o seu código escrito no arquivo `main.py`, é hora de dar vida ao projeto!
No terminal, digite o seguinte comando e aperte **Enter**:

`python main.py`

## Passo 4: Visualizando a Interface

Como o Codespaces é um servidor nas nuvens, ele vai criar um "túnel" de rede para enviar a tela do aplicativo para o seu computador.

1. Assim que você rodar o comando acima, o terminal vai ficar rodando continuamente.
2. Olhe para o canto inferior direito do Codespaces: um aviso azul vai aparecer dizendo que a aplicação está rodando em uma porta.
3. Clique no botão verde **"Open in Browser"** (Abrir no Navegador).
4. *Alternativa:* Se o aviso não aparecer, clique na aba **Portas (Ports)** ao lado do terminal e clique no ícone de "globo" para abrir a tela.

---

## Dicionário de Códigos (Flet vs Figma)

Para que você não se perca no código, aqui está uma tabela com os principais comandos e o que eles significam no mundo do design:

| Código Python / Flet | O que significa? / Equivalência no Figma |
| :--- | :--- |
| `def nome_da_funcao():` | É como criar um **Componente** no Figma. Você cria uma vez e pode reutilizar em várias partes do código. |
| `ft.Row([ ... ])` | **Auto Layout Horizontal**. Alinha os elementos lado a lado (esquerda para a direita). |
| `ft.Column([ ... ])` | **Auto Layout Vertical**. Empilha os elementos um embaixo do outro. |
| `ft.Container(...)` | **Frame ou Retângulo**. Cria uma "caixa" onde você pode adicionar cor, borda arredondada e margens. |
| `alignment=ft.MainAxisAlignment.CENTER` | Centraliza os elementos no **eixo principal** (ex: no meio exato da linha ou coluna). |
| `horizontal_alignment=ft.CrossAxisAlignment.CENTER` | Alinha os elementos ao centro no **eixo oposto** (ex: centraliza os textos verticalmente dentro de um Container). |
| `padding=...` | **Margem Interna**. Espaço entre a borda da caixa e o conteúdo que está dentro dela. |
| `bgcolor="..."` | **Fill / Cor de Fundo**. Define a cor do elemento (aceita cores como `"white"` ou códigos HEX como `"#185650"`). |
| `border_radius=...` | **Corner Radius**. Deixa as bordas da caixa ou botão arredondadas. |
| `expand=True` | **Fill Container**. Diz para o elemento crescer e ocupar todo o espaço vazio disponível na tela. |
| `weight=ft.FontWeight.BOLD` | Deixa a fonte do texto em **Negrito**. |
| `on_tap=...` | **Prototipagem (On Click)**. Define qual ação vai acontecer quando o usuário tocar em uma imagem ou área específica. |

---

## Dicas de Ouro

* **Sopa de letrinhas:** Fique sempre atento ao abrir e fechar de parênteses `()` e colchetes `[]` no Flet. Uma vírgula esquecida pode gerar um erro na tela toda!
* **Parando a execução:** Para testar uma nova versão do seu código, você precisa parar o programa atual. Vá no terminal, clique nele e pressione `Ctrl + C` para encerrar o servidor. Depois, digite `python main.py` novamente.
* **Tudo é uma caixa:** Se não souber como posicionar um elemento, coloque-o dentro de um `ft.Container()` e mude a cor de fundo dele provisoriamente para vermelho. Assim, você "enxerga" o espaço que ele está ocupando.

Boa aula e divirtam-se programando para o mundo real!