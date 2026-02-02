# 📄 Guia de Documentação e Estudo - Python Mundo 1

Este guia define o padrão para as anotações diárias, documentação de código e commits da equipe LaboraDev.

---

## 📝 1. Anotações Diárias de Estudo

As anotações devem ser salvas em `docs/anotacoes_diarias/YYYY-MM-DD_estudo.md`.

### O que incluir:
- **Tópico do dia**: Ex: Aula 07 - Operadores Aritméticos.
- **Principais conceitos**: O que você aprendeu de mais importante? (Ex: Divisão inteira `//` vs real `/`).
- **Dificuldades encontradas**: Onde você travou? Como resolveu?
- **Exemplos práticos rápidos**: Pequenos trechos de código que testou.
- **Links úteis**: Artigos ou vídeos extras consultados.

### Modelo Sugerido:
```markdown
# Estudo Diário - [DATA]
**Aula:** [Número e Título]

## 🎯 Conceitos Chave
- [Conceito 1]
- [Conceito 2]

## 💡 Aprendizados
- Resumo do que foi fixado hoje.

## 🚧 Desafios/Dúvidas
- O que foi difícil e como superei.
```

---

## 🛠️ 2. Documentação do Código (Final da Semana)

Toda sexta-feira/sábado, devemos consolidar a documentação técnica em `docs/CONSOLDIDADO_SEMANA_X.md`.

### Estrutura Padrão:
1. **Visão Geral**: O que foi construído na semana.
2. **Componentes/Módulos**: Descrição das funções criadas em `src/`.
3. **Instruções de Uso**: Como rodar os scripts da semana.
4. **Dependências**: Se algum módulo extra foi necessário.

---

## 🚀 3. Padrão de Commits (Git)

Para manter o histórico limpo, usaremos o padrão **Conventional Commits**.

### Formato do Título:
`<tipo>(escopo): <descrição curta em português>`

### Tipos permitidos:
- `feat`: Novo recurso (ex: nova aula, novo exercício).
- `fix`: Correção de bug no código.
- `docs`: Mudanças na documentação.
- `style`: Formatação, pontos e vírgulas (sem mudança de lógica).
- `refactor`: Refatoração de código.
- `test`: Adição ou correção de testes.

### Exemplos:
- `feat(aula07): adicionar exercícios de operadores`
- `docs(readme): atualizar cronograma da equipe`
- `fix(aula06): corrigir erro de conversão de tipo`

---

## 📅 4. Alinhamento com Trello

- **Cartão no Trello**: O link do arquivo de anotação diária deve ser anexado ao cartão correspondente da Daily.
- **Checklist**: Marque o item "Documentação" no Trello apenas após o commit no GitHub.
- **Status**: Mova para "✅ Concluído" apenas quando o código e a documentação estiverem no repositório.

---

**Atualizado em:** 02 de Fevereiro de 2026
**Equipe:** Amélia, Ana, Isaura
