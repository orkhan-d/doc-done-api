from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from api.modules.auth.routes import router as auth_router
from api.modules.docrules.routes import router as docrules_router
from api.modules.documents.routes import router as queue_router

app = FastAPI()

app.add_middleware(CORSMiddleware,
                   allow_origins = ('*'),
                   allow_methods = ("*"),
                   allow_headers = ("*"),
                   allow_credentials = True)

main_router = APIRouter(prefix='/api')
main_router.include_router(auth_router)
main_router.include_router(docrules_router)
main_router.include_router(queue_router)

app.include_router(main_router)