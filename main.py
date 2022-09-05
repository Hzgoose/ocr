# -*- coding: utf-8 -*-
from sanic import Sanic
from sanic.response import json
from config import config
from apps import controller
from datetime import datetime

app = Sanic(name='ocr')


@app.route("/")
async def status(request):
    return json({"API": "OK", "time": str(datetime.now())})


@app.route("/v1/parse-resume", methods=['POST', 'OPTIONS'])
async def parse_resume(request):
    if request.method == "OPTIONS":
        return json(None, status=200)
    return controller.parse_resume(request)


if __name__ == "__main__":
    app.run(
        host=config.config_service['host'], 
        port=int(config.config_service['port']), 
        workers=int(config.config_service['workers'])
        )
