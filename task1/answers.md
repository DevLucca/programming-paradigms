1. Se você fosse classificar este código em algum dos paradigmas de programação existentes, em qual você classificaria e por quê? 

> R: Imperativo, por que o código dita explicitamente o que deve ser executado em cada passo para se atingir o objetivo final.

2. Altere o código existente para que ele possa seguir mais as regras do Paradigma Procedural. Indique no código o que você fez:

> R: Primeiro abstrai as funções para possuir funções reutilizáveis e utilizei o `module.exports` como se fosse a função `main` do código. [Código aqui](./procedural.js)

3. Altere o código existente para que ele possa seguir mais as regras do Paradigma Funcional. Indique no código o que você fez:

> R: Além de abstrair as funções, tentei fazer com que elas seguissem o padrão funcional, de que a função não deve nunca alterar informações externas a ela, somente produz o mesmo resultado com os mesmos inputs. Utilizei o `module.exports` como se fosse a função `main` do código. [Código aqui](./functional.js)
