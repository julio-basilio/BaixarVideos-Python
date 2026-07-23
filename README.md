<div align="center">

  <h1>📺BaixarVideos-Pytho </h1>
  <p><strong>Uma aplicação de linha de comando elegante para download de vídeos do YouTube com suporte a autenticação e histórico de downloads.</strong></p>

  <p>
    <a href="#-recursos">Recursos</a> •
    <a href="#-pré-requisitos">Pré-requisitos</a> •
    <a href="#-instalação">Instalação</a> •
    <a href="#-como-usar">Como Usar</a> •
    <a href="#-estrutura-do-json">Estrutura do JSON</a>
  </p>

  <p>
    <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Version" />
    <img src="https://img.shields.io/badge/PytubeFix-Latest-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Pytubefix" />
    <img src="https://img.shields.io/badge/Colorama-Terminal-000000?style=for-the-badge" alt="Colorama" />
  </p>

</div>

<hr />

## 🚀 Recursos

<ul>
  <li><b>🔐 Autenticação de Usuários:</b> Sistema simples de login e cadastro.</li>
  <li><b>🎬 Download em Alta Qualidade:</b> Obtém e baixa automaticamente a maior resolução disponível do vídeo.</li>
  <li><b>📊 Barra de Progresso no Terminal:</b> Feedback visual em tempo real do download em andamento.</li>
  <li><b>💾 Histórico Persistente:</b> Mapeia e salva automaticamente todas as URLs baixadas por cada usuário no <code>usuarios.json</code>.</li>
  <li><b>🎨 Interface Estilizada:</b> Uso de cores dinâmicas no terminal via <code>colorama</code>.</li>
</ul>

<hr />

## 🛠️ Pré-requisitos

Certifique-se de ter instalado em sua máquina:
* **Python 3.10** ou superior.
* Gerenciador de pacotes **pip**.

<hr />

## 📦 Instalação

1. <b>Clone o repositório:</b>
   <pre><code>git clone https://github.com/julio-basilio/BaixarVideos-Python/tree/main </code></pre>

2. <b>Instale as dependências:</b>
   <pre><code>pip install colorama pytubefix</code></pre>

3. <b>Crie o arquivo de banco de dados inicial:</b><br />
   Crie o arquivo <code>usuarios.json</code> no diretório raiz do projeto com o conteúdo:
   <pre><code>[]</code></pre>

<hr />

## 📁 Estrutura do Projeto

<table>
  <thead>
    <tr>
      <th>Arquivo / Pasta</th>
      <th>Descrição</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>main.py</code></td>
      <td>Código principal contendo o fluxo de login, cadastro e download de vídeos.</td>
    </tr>
    <tr>
      <td><code>usuarios.json</code></td>
      <td>Base de dados local contendo os usuários e seus históricos de links baixados.</td>
    </tr>
    <tr>
      <td><code>Video/</code></td>
      <td>Diretório gerado automaticamente onde os vídeos baixados são salvos.</td>
    </tr>
  </tbody>
</table>

<hr />

## 💻 Como Usar

1. Execute o script principal:
   <pre><code>python main.py</code></pre>

2. Escolha uma das opções no menu:
   <ul>
     <li><code>1</code> — <b>Entrar:</b> Realiza o login com usuário e senha já cadastrados.</li>
     <li><code>2</code> — <b>Cadastrar:</b> Registra uma nova conta e inicia a sessão.</li>
   </ul>

3. Cole a URL do vídeo do YouTube quando solicitado.

4. O vídeo será baixado automaticamente na pasta <code>Video/</code>.

<hr />

## 📄 Estrutura do JSON

O arquivo `usuarios.json` mantém os dados organizados no seguinte formato:

```json
[
    {
        "nome": "usuario_exemplo",
        "senha": "123",
        "links_baixados": [
            "[https://www.youtube.com/watch?v=dQw4w9WgXcQ](https://www.youtube.com/watch?v=dQw4w9WgXcQ)"
        ]
    }
]
