import json
from typing import List

import discord

from infrastructure.apiclient import apiClient
from usecase.utils import ErrorStruct, send_info_message, send_error_message


class Process:
    def __init__(self, ctx):
        self.ctx = ctx

    async def start(self):
        query = {
            "status": "active"
        }
        response = apiClient.create_status(query)
        if response.status_code == 201:
            await send_info_message(ctx=self.ctx, description="Smart Watch IoT System Started!")
        else:
            raw_data = response.text
            data = json.loads(raw_data)
            errors = []
            for atr in data:
                for err in data[atr]:
                    err = ErrorStruct(key=atr, value=err)
                    errors.append(err)
            await send_error_message(ctx=self.ctx, errors=errors)

    async def stop(self):
        query = {
            "status": "inactive"
        }
        response = apiClient.create_status(query)
        if response.status_code == 201:
            await send_info_message(ctx=self.ctx, description="Smart Watch IoT System Stopped!")
        else:
            raw_data = response.text
            data = json.loads(raw_data)
            errors = []
            for atr in data:
                for err in data[atr]:
                    err = ErrorStruct(key=atr, value=err)
                    errors.append(err)
            await send_error_message(ctx=self.ctx, errors=errors)
