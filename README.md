# Zuul Routes Parser

Pequena ferramenta para fazer parse de arquivos *.properties contendo rotas do Zuul

## Requisitos

- Que as rotas estejam no formato Java Properties, ex\:\
```zuul.routes.ROUTE-NAME.PROPERTY = VALUE```
- Python 3.6 ou superior

## Modo de uso

1. Clone o repositório localmente e entre no diretório
2. Instale o pacote usando o comando `pip install -e .` (usando o pip equivalente a uma versão suportada do Python, como pip3.9)
3. Vá até a pasta com os arquivos `*.properties` e execute `zuul_parser`

Também é possível exportar para JSON e CSV:

- `zuul_parser json`
- `zuul_parser csv`
- `zuul_parser csv filename.csv`

## Atualizando

Para atualizar o pacote é só fazer `git pull` no repositório local quando houver um update.

Se você instalou usando a opção `-e` no `pip`, ele atualizará o pacote automaticamente após o `git pull`.

## Observações

- O script ignora rotas comentadas com # nos arquivos
- O script procura por arquivos cujos nomes fazem match com `*.properties`, só na pasta atual (cwd)
