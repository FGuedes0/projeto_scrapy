# projeto_scrapy
- scrapy crawleia 10 páginas do mercado livre e salva em um arquivo json

- para rodar o scrapy: 

```bash 
    scrapy crawl mercadolivre -o ../data/data.jsonl
```   
- pandas lê o arquivo json, trata e salva em um banco de dados
- para rodar o pandas: 
```bash
    python transformacao/main.py
```
- Streamlit lê o banco de dados e gera um dashboard com as informações

- para rodar o streamlit:

```bash
    streamlit rum dashboar/app.py
```

