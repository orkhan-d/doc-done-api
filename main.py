from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(CORSMiddleware,
                   allow_origins = ('*'),
                   allow_methods = ("*"),
                   allow_headers = ("*"),
                   allow_credentials = True)

main_router = APIRouter(prefix='/api')
app.include_router(main_router)