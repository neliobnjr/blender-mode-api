# Movimento Espiral no Blender usando Flask API

## Descrição

Este experimento demonstra como controlar a posição de um objeto no Blender (neste caso, um Cube) usando um servidor Flask API. O objetivo é fazer o Cube mover-se em uma trajetória espiral no plano XY, com a trajetória sendo calculada pelo servidor Flask e o Cube no Blender buscando sua posição atualizada periodicamente.

## Requisitos

- **Blender**: Versão utilizada durante o desenvolvimento: 2.9x.
- **Python**: Versão utilizada durante o desenvolvimento: 3.8+.
- **Flask**: Instale via pip com o comando `pip install Flask`.

## Configuração e Uso

1. **Configuração do servidor Flask**:

   - Clone este repositório ou copie o código do servidor Flask.
   - Execute o servidor Flask com o comando:
     ```
     python nome_do_arquivo_do_servidor.py
     ```

   Após a execução, o servidor estará disponível em `http://localhost:5000/position`.

2. **Configuração no Blender**:

   - Abra o Blender e importe o script Python.
   - Execute o script no Blender. Isso fará com que o Blender faça consultas contínuas ao servidor Flask para obter a posição atualizada do Cube.

3. **Movimento Espiral**:

   - Com o servidor em execução e o script no Blender ativado, o Cube começará a mover-se em uma trajetória espiral no plano XY.

## Como Funciona

1. **Cálculo da Espiral**:
   - Utilizamos a espiral de Arquimedes para calcular a trajetória do Cube.
   - A cada requisição ao servidor Flask, ele calcula a próxima posição na trajetória e retorna as coordenadas para o Blender.

2. **Comunicação Blender-Flask**:
   - O Blender consulta o servidor Flask periodicamente. Ao receber uma nova posição, move o Cube para essa nova posição.

## Limitações e Melhorias Futuras

- Atualmente, o movimento é restrito ao plano XY. Poderíamos estender isso para 3D.
- Estamos usando `polling` para obter as atualizações. Uma abordagem baseada em WebSockets poderia ser mais eficiente.

## Contribuições

Contribuições são bem-vindas! Seja para aprimorar o movimento, otimizar o código ou introduzir novas funcionalidades.

## Licença

Este projeto está licenciado sob a licença MIT.
