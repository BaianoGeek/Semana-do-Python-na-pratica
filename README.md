## Projeto 1: Geração de Documento PDF

### Descrição
O código cria um arquivo PDF contendo informações de um projeto, como descrição, horas previstas, valor da hora trabalhada e prazo estimado. Utiliza a biblioteca `fpdf` para gerar o documento PDF.

### Arquivo
- **Nome do Arquivo**: `gerador.py`
- **Dependências**: `fpdf`

### Funcionamento
- Solicita ao usuário informações sobre o projeto.
- Calcula o valor total do projeto com base nas horas previstas e valor da hora.
- Gera um documento PDF com as informações fornecidas.

## Projeto 2: Envio de Mensagem no WhatsApp

### Descrição
O código automatiza o envio de mensagens para contatos no WhatsApp. Obtém cotações de criptomoedas usando `yfinance` e envia as informações formatadas para os contatos especificados.

### Arquivo
- **Nome do Arquivo**: `buscaYahoo.py`
- **Dependências**: `yfinance`, `pyautogui`, `pyperclip`

### Funcionamento
- Obtém dados de fechamento de criptomoedas especificadas.
- Formata as informações em uma mensagem de texto.
- Utiliza `pyautogui` para automatizar a interação com o WhatsApp e enviar as mensagens.

## Projeto 3: Geração de Histograma Interativo

### Descrição
O código lê dados de vendas de um arquivo Excel e gera um histograma interativo usando `plotly.express`. O gráfico mostra o faturamento por loja e forma de pagamento.

### Arquivo
- **Nome do Arquivo**: `analiseDados.py`
- **Dependências**: `pandas`, `plotly`

### Funcionamento
- Lê dados de vendas de um arquivo Excel.
- Usa `plotly.express` para criar um histograma interativo com informações de faturamento por loja.

## Projeto 4: Detecção de Mãos com OpenCV

### Descrição
O código inicializa a webcam, detecta mãos em tempo real usando `cv2` e `cvzone`, e exibe um vídeo com marcações das mãos detectadas. É útil para projetos de interação humano-computador baseados em visão computacional.

### Arquivo
- **Nome do Arquivo**: `ia.py`
- **Dependências**: `cv2`, `cvzone`

### Funcionamento
- Inicializa a webcam do computador.
- Utiliza `cvzone` para detectar e rastrear mãos na imagem da webcam.
- Exibe um vídeo da webcam com marcações das mãos detectadas em uma janela POP-UP.

## Observações Gerais
- Certifique-se de ter todas as dependências instaladas antes de executar cada código.
- Ajuste parâmetros e configurações conforme necessário, como localizações de arquivos, coordenadas de cliques, entre outros.
- Cada projeto oferece funcionalidades específicas que podem ser adaptadas e expandidas para atender a diferentes requisitos e necessidades.

Esses códigos são exemplos práticos de aplicação de Python em diferentes contextos, desde automação de tarefas até visualização de dados e interação com dispositivos de entrada como webcam e WhatsApp.
