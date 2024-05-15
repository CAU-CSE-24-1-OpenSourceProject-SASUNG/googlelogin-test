from fastapi import FastAPI, Query
from database.connection import conn
from routes.users import user_router
from fastapi.responses import JSONResponse
from starlette.requests import Request
from starlette.responses import RedirectResponse, JSONResponse
from starlette.middleware.sessions import SessionMiddleware
from fastapi.middleware.cors import CORSMiddleware  # CORS

from starlette.requests import Request

# FastAPI
app = FastAPI()

#middleware
app.add_middleware(SessionMiddleware, secret_key="akjsfdashfd")


# CORS
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 등록
app.include_router(user_router, prefix="/user")

#애플리케이션이 시작 될 때 데이터베이스를 생성하도록 만듬
@app.on_event("startup")
def on_startup():
	conn()

if __name__ == "__main__":
	import uvicorn
	uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
    #python main.py를 실행하면 uvicorn을 실행한다


recent_games = [
        {'gameId': '1', 'gameTitle': '아이는 10층에 산다 (1)'},
        {'gameId': '2', 'gameTitle': '더운 방 속 한 사람 (2)'},
        {'gameId': '3', 'gameTitle': '더운 방 속 한 사람 (1)'}
        ]

@app.get('/recentgames')
async def reaccess(request: Request):
    return JSONResponse(content=recent_games)

riddle_items = [
        {'riddleId': '1', 'riddleTitle': '아이는 10층에 산다.'},
        {'riddleId': '2', 'riddleTitle': '도청하는 사람 A'},
        {'riddleId': '3', 'riddleTitle': '더운 방 속 한 사람'}
        ]

@app.get('/riddles')
async def show_all_riddle():
    return JSONResponse(content=riddle_items)


@app.post('/newgame')
async def create_game():
    return JSONResponse(content={'newGameId': '3'})



game_info = [
        {'gameTitle' : '아이는 10층에 산다. (1)', 'problem': '어떤 아이가 아파트 10층에 살고 있다. 아이는 맑은 날 ~'},
        {'queryId' : '1', 'query' : '안녕' , 'response' : '상관 없습니다.'},
        {'queryId' : '2', 'query' : '아이는 키가 작아?' , 'response' : '맞습니다.'},
        {'queryId' : '3', 'query' : '아이는 우산을 가지고 있어?' , 'response' : '맞습니다.'},
        {'queryId' : '4', 'query' : '아이는 운동하는 걸 좋아해?' , 'response' : '아닙니다.'},
        {'queryId' : '5', 'query' : '아이는 비오는 날 우산으로 10층 버튼을 누를 수 있는거야!' , 'response' : '정확한 정답을 맞추셨습니다!'},
        ]


@app.get('/gameinfo')
async def access_game(gameid: int = Query(...)):
    return JSONResponse(content=game_info)
