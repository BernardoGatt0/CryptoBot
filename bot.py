from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests
import locale

async def bitcoin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=brl'
    resposta = requests.get(url)
    dados = resposta.json()
    try: 
        if dados['status']['error_code'] == 429:
            await update.message.reply_text('Limite de requisições da API atingido, por favor aguarde e tente novamente')
    except:
        preco = dados['bitcoin']['brl']
        preco = locale.currency(preco, grouping=True)
        await update.message.reply_text(f'O preço do BTC é: {preco}')

async def ethereum(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=brl'
    resposta = requests.get(url)
    dados = resposta.json()
    print(dados)
    try: 
        if dados['status']['error_code'] == 429:
            await update.message.reply_text('Limite de requisições da API atingido, por favor aguarde e tente novamente')
    except:
        preco = dados['ethereum']['brl']
        preco = locale.currency(preco, grouping=True)
        await update.message.reply_text(f'O preço do ETH é: {preco}')

async def usdc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids=usd-coin&vs_currencies=brl'
    resposta = requests.get(url)
    dados = resposta.json()
    try: 
        if dados['status']['error_code'] == 429:
            await update.message.reply_text('Limite de requisições da API atingido, por favor aguarde e tente novamente')
    except:
        preco = dados['usd-coin']['brl']
        preco = locale.currency(preco, grouping=True)
        await update.message.reply_text(f'O preço do USDC é: {preco}')

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

if __name__ == "__main__":
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    TOKEN = "6629864176:AAFh8poTaPzKMjrkUfB5G0c779UrzSFMBpU"
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("btc", bitcoin))
    app.add_handler(CommandHandler("eth", ethereum))
    app.add_handler(CommandHandler("usdc", usdc))

    print('Polling...')
    app.run_polling()