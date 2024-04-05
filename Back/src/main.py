from fastapi import FastAPI
from Back.src.http_client import CMCHTTPClient
from Back.src.config import settings


app = FastAPI()


cmc_client = CMCHTTPClient(
    base_url='https://pro-api.coinmarketcap.com',
    api_key=settings.CMC_API_KEY
)

@app.get('/cryptocurrencies/')
async def get_cryptocurrencies():
    return await cmc_client.get_listings()
    

@app.get('/cryptocurrencies/{currency_id}')
async def get_cryptocurrency(currency_id: int):
    return cmc_client.get_currency(currency_id)