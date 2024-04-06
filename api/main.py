from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from api.modules.auth.routes import router as auth_router

app = FastAPI()

app.add_middleware(CORSMiddleware,
                   allow_origins = ('*'),
                   allow_methods = ("*"),
                   allow_headers = ("*"),
                   allow_credentials = True)

main_router = APIRouter(prefix='/api')
main_router.include_router(auth_router)

app.include_router(main_router)