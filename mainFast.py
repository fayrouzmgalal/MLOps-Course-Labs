#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

# Instrument the FastAPI app for Prometheus metrics
Instrumentator().instrument(app).expose(app)

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

