# -*- coding: utf-8 -*-
from sanic.response import json
from config import config
import textract
import os


def save_file(file):
    file_name = file.name
    f = open(config.config_file['path_file'] + file_name, 'wb')
    f.write(file.body)
    f.close()

    return config.config_file['path_file'] + file_name


def delete_file(path_file):
    os.remove(path_file)


def parse_resume(request):
    file = request.files.get('file')
    if file is None:
        return json({
            "errors": [
                {
                    "file": "Missing data for required field."
                }
            ]
        })
    path_file = save_file(file)
    text = textract.process(
        path_file,
        method='tesseract',
        language='vie+eng',
        encoding='ascii'
    )

    delete_file(path_file)
    return json({
        "data": text.decode("utf-8")
    })
