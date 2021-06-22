import typing
from threading import Thread

import orjson
import uvicorn
import subprocess
from subprocess import Popen
from fastapi import FastAPI
from starlette.responses import JSONResponse


def exec_script(sh: str):
    proc = Popen(args=[sh], shell=True, stdout=subprocess.PIPE)
    return proc.stdout.read().decode('utf-8').split('\n')


class AsyncThread(Thread):
    def __init__(self, task_id, env, sh):
        super().__init__()
        self.task_id = task_id
        self.sh = f'{env} {sh}'

    def run(self) -> None:
        res = exec_script(sh=self.sh)
        print(res)


class ORJSONResponse(JSONResponse):
    media_type = "application/json"

    def render(self, content: typing.Any) -> bytes:
        return orjson.dumps(content, option=orjson.OPT_SERIALIZE_NUMPY)


app = FastAPI(default_response_class=ORJSONResponse)


@app.get("/{task_id}")
async def read_root(task_id, env, sh):
    AsyncThread(task_id=task_id, env=env, sh=sh).start()
    return {
        "task_id": task_id,
        "sh": f'{env} {sh}',
        "code": 200
    }


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=10009)
