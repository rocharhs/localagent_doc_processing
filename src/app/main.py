from fastapi import FastAPI
from app.controller.doc_router import router

app = FastAPI()

#include the router
app.include_router(router, prefix="/doc-processing", tags=["documents"])
