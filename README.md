# Zuul Routes Parser

Pequena ferramenta para fazer parse de arquivos *.properties contendo rotas do Zuul

## Requisitos
- Que as rotas estejam no formato Java Properties, ex\:\
```zuul.routes.ROUTE-NAME.PROPERTY = VALUE```
- Python 3.6 ou superior

## Modo de uso
1. Clone o repositório localmente e entre no diretório
2. Instale o pacote usando o comando `pip install -e .`
3. Vá até a pasta com os arquivos `*.properties` e execute `zuul_parser`

Também é possível exportar para JSON e CSV:
- `zuul_parser json`
- `zuul_parser csv`

## Observações
- O script ignora rotas comentadas com # nos arquivos
- O script procura por arquivos seguindo o pattern `*.properties`, só na pasta atual (cwd)
