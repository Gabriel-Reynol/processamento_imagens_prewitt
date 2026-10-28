# Detecção de Bordas em Imagens com Python

Projeto desenvolvido para praticar conceitos de **Processamento Digital de Imagens**, utilizando Python e NumPy para implementar manualmente operações de conversão para escala de cinza, zero padding e detecção de bordas por meio dos filtros Prewitt.

O objetivo é compreender como os pixels de uma imagem são representados e manipulados em matrizes, além de explorar o funcionamento de filtros espaciais e operações utilizadas nos fundamentos de Visão Computacional e Redes Neurais Convolucionais (CNNs).

## Tecnologias utilizadas

- **Python** — Desenvolvimento do algoritmo.
- **NumPy** — Manipulação de matrizes e operações matemáticas.
- **Pillow (PIL)** — Carregamento e conversão do modo de cor das imagens.
- **Matplotlib** — Visualização dos resultados.

## Funcionamento

O processamento é dividido em cinco etapas principais.

### 1. Carregamento da imagem

A imagem é carregada utilizando Pillow e convertida para o modo RGB, garantindo três canais de cor.

Em seguida, é transformada em um array NumPy de dimensões `(altura, largura, 3)`, permitindo acessar individualmente as intensidades dos pixels.

### 2. Conversão para escala de cinza

A função `converter_cinza()` percorre os pixels da imagem e calcula uma intensidade de cinza por meio da combinação ponderada dos canais RGB:

\[
I = 0.299R + 0.587G + 0.114B
\]

O resultado é uma matriz bidimensional `(altura, largura)`.

### 3. Zero Padding

A função `padding()` adiciona uma borda de zeros ao redor da imagem em escala de cinza.

Para uma imagem de dimensões `(m, n)`, a matriz com padding passa a ter dimensões `(m+2, n+2)`.

Esse preenchimento permite aplicar o kernel 3 × 3 também nas regiões próximas às extremidades da imagem original.

### 4. Detecção de bordas com Prewitt

A função `aplicar_filtro()` percorre a imagem com padding e aplica dois kernels 3 × 3.

**Prewitt X — Bordas verticais**

```text
[-1   0   1]
[-1   0   1]
[-1   0   1]
```

Identifica principalmente variações de intensidade entre pixels à esquerda e à direita.

**Prewitt Y — Bordas horizontais**

```text
[-1  -1  -1]
[ 0   0   0]
[ 1   1   1]
```

Identifica principalmente variações de intensidade entre regiões superiores e inferiores.

Em cada posição, uma região 3 × 3 da imagem é multiplicada elemento a elemento pelo kernel, e os resultados são somados.

A implementação utiliza laços `for`, fatiamento de matrizes e `np.sum()`, sem recorrer a filtros prontos do OpenCV.

### 5. Combinação das bordas

Após calcular as respostas dos filtros Prewitt X e Y, o programa combina os resultados por meio da magnitude do gradiente:

\[
G = \sqrt{G_x^2 + G_y^2}
\]

Essa operação permite destacar bordas em diferentes orientações.

Para visualizar individualmente as respostas dos filtros, utiliza-se `np.abs()`, preservando a intensidade das bordas independentemente do sinal do gradiente.

## Resultados

O programa permite visualizar cinco representações da imagem:

1. Imagem original RGB.
2. Imagem convertida para escala de cinza.
3. Bordas verticais — Prewitt X.
4. Bordas horizontais — Prewitt Y.
5. Bordas combinadas — Magnitude do gradiente.

As imagens são exibidas utilizando Matplotlib.

## Estrutura do projeto

```text
PI_bordas/
├── img_conversor.py
├── Castelo.jpg
└── README.md
```

## Como executar

**1. Instale as dependências:**

```bash
python -m pip install numpy pillow matplotlib
```

**2. Coloque uma imagem na pasta do projeto.**

O código utiliza o arquivo `Castelo.jpg`. Para processar outra imagem, altere o nome do arquivo no comando `Image.open()`.

**3. Execute o programa:**

```bash
python img_conversor.py
```

As imagens processadas serão apresentadas em janelas do Matplotlib.

## Conceitos praticados

- Representação de imagens em matrizes RGB.
- Manipulação de arrays multidimensionais.
- Acesso e processamento de pixels.
- Conversão para escala de cinza.
- Zero padding.
- Filtros espaciais e operações de correlação.
- Detecção de bordas com Prewitt.
- Magnitude do gradiente.
- Organização do código em funções reutilizáveis.

## Possíveis melhorias

- Remover a borda externa adicional das matrizes filtradas.
- Salvar automaticamente os resultados em arquivos PNG.
- Implementar outros filtros, como Sobel e Canny.
- Comparar os resultados dos diferentes métodos.
- Desenvolver uma interface para carregar imagens e selecionar filtros.

---

Projeto de estudo prático voltado ao aprofundamento em **Processamento de Imagens, Visão Computacional e Desenvolvimento de Software com Python**.