# from fastapi import FastAPI
 
# app = FastAPI()
 
# @app.get("/")
# def read_root():
#    return {"Hello": "World"}

# @app.get("/about")
# def read_about():
#    return {
#       "title": "위니브 홈페이지",
#       "description": "위니브 홈페이지입니다.",
#       "content": "위니브는 ........."
#    }

# @app.get("/contact")
# def read_contact():
#    return {
#       "title": "위니브 본사",
#       "descriptoin": "위니브 본사입니다.",
#       "contents": "위니브 본사는 제주특별자치도 제주시 첨단로 330"
#    }

# 과제
'''
URL: http://localhost:8000
{
    'message': '위니브에 오신것을 환영합니다.',
    'thumbnail': ['위니브1.png', '위니브2.png', '위니브3.png']
}

URL: http://localhost:8000/about
{
    'message': '위니브는 위대한 회사입니다.',
    'employee': ['김철수', '홍길동', '김영희']
}

URL: http://localhost:8000/contact
{
    'message': '위니브에 문의하세요.',
    'phone': ['010-1234-5678'],
    'email': ['paullab@naver.com'],
    'address': ['제주시 첨단로 330']
}

URL: http://localhost:8000/a
{
    'message': 'A 페이지입니다.'
}

URL: http://localhost:8000/b
{
    'message': 'B 페이지입니다.'
}
'''

# thumnail = ["위니브1.png", "위니브2.png", "위니브3.png"]
# employee = ["김철수", "홍길동", "김영희"]

# contact = {
#     "phone": "010-1234-5678",
#     "email": "paullab@naver.com",
#     "address": "제주시 첨단로 330",
# }


# @app.get("/")
# def read_root():
#     return {"message": "위니브에 오신것을 환영합니다.", "thumbnail": thumnail}


# @app.get("/about")
# def read_about():
#     return {"message": "위니브는 위대한 회사입니다.", "employee": employee}


# @app.get("/contact")
# def read_contact():
#     return {
#         "message": "위니브에 문의하세요.",
#         "phone": contact["phone"],
#         "email": contact["email"],
#         "address": contact["address"],
#     }


# @app.get("/a")
# def read_a():
#     return {"message": "A 페이지입니다."}


# @app.get("/b")
# def read_b():
#     return {"message": "B 페이지입니다."}

# from fastapi import FastAPI
# from fastapi.responses import HTMLResponse

# app = FastAPI()


# @app.get("/", response_class=HTMLResponse)
# def index():
#     return """
# <!DOCTYPE html>
# <html>
# <head>
#     <style>
#         html, body {
#             margin: 0;
#             padding: 0;
#         }
#         div {
#             margin: 0;
#             padding: 0;
#         }
#         h1 {
#             margin: 0;
#             padding: 0;
#             background-color: #4267B2;
#             color: white;
#         }
#     </style>
# </head>
# <body>
#     <div>
#         <h1>facebook</h1>
#     </div>
# </body>
# </html>
# """


# @app.get("/about", response_class=HTMLResponse)
# def about():
#     return "<h1>hello world 2</h1>"


# @app.get("/contact", response_class=HTMLResponse)
# def contact():
#     return "<h1>hello world 3</h1>"


# @app.get("/notice", response_class=HTMLResponse)
# def notice():
#     return "<h1>hello world 4</h1>"

# blog_post = [
#     {
#         "title": "첫번째 포스트",
#         "contents": "첫번째 포스트 내용입니다.",
#         "author": "이호준",
#         "date": "2025-1-1",
#     },
#     {
#         "title": "두번째 포스트",
#         "contents": "두번째 포스트 내용입니다.",
#         "author": "이호준",
#         "date": "2025-1-2",
#     },
#     {
#         "title": "세번째 포스트",
#         "contents": "세번째 포스트 내용입니다.",
#         "author": "이호준",
#         "date": "2025-1-3",
#     },
# ]

# s = ""

# for i in blog_post:
#     s += f"""
#     <section>
#         <h2>{i['title']}</h2>
#         <p>{i['contents']}</p>
#         <p>{i['author']} | {i['date']}</p>
#     </section>
#     """


# @app.get("/blog", response_class=HTMLResponse)
# def notice():
#     return f"""
# <!DOCTYPE html>
# <html>
# <head>
#     <style>
#         html, body {{
#             margin: 0;
#             padding: 0;
#         }}
#         div {{
#             margin: 0;
#             padding: 0;
#         }}
#         h1 {{
#             margin: 0;
#             padding: 0;
#             background-color: #4267B2;
#             color: white;
#         }}
#     </style>
# </head>
# <body>
#     <header>
#         <h1>hojun blog</h1>
#     </header>
#     <main>
#         {s}
#     </main>
#     <footer>
#         이호준 | 010-1234-1234 | hojun@gmail.com
#     </footer>
# </body>
# </html>
# """

# from fastapi import FastAPI
# from fastapi import Request
# from fastapi.templating import Jinja2Templates

# blog_post = [
#     {
#         "title": "첫번째 포스트",
#         "contents": "첫번째 포스트 내용입니다.",
#         "author": "이호준",
#         "date": "2025-1-1",
#     },
#     {
#         "title": "두번째 포스트",
#         "contents": "두번째 포스트 내용입니다.",
#         "author": "이호준",
#         "date": "2025-1-2",
#     },
#     {
#         "title": "세번째 포스트",
#         "contents": "세번째 포스트 내용입니다.",
#         "author": "이호준",
#         "date": "2025-1-3",
#     },
# ]

"""
/ -> index.html, 소개가 들어갑니다.
/blog -> blog.html, 블로그 포스트 목록이 들어갑니다.
/blog/{post_id} -> post.html, 블로그 포스트 내용이 들어갑니다. post_id는 1부터 시작합니다. blog/1이라고 입력하면 0번째 게시물이 나옵니다.

jinja2사용해서 웹 페이지를 만들려고 하는데 아래 코드가 기본 코드야. 이 코드를 기반으로 우선 main.py를 작성해줘.
"""
 
# app = FastAPI(docs_url="/documentation", redoc_url=None)
 
# templates = Jinja2Templates(directory="templates")
 
 
# # 소개가 들어갑니다.
# @app.get("/")
# def index(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request})

# @app.get("/blog")

from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates

# 블로그 포스트 데이터
blog_posts = [
    {
        "id": 1,
        "title": "첫번째 포스트",
        "contents": "첫번째 포스트 내용입니다.",
        "author": "이호준",
        "date": "2025-1-1",
    },
    {
        "id": 2,
        "title": "두번째 포스트",
        "contents": "두번째 포스트 내용입니다.",
        "author": "이호준",
        "date": "2025-1-2",
    },
    {
        "id": 3,
        "title": "세번째 포스트",
        "contents": "세번째 포스트 내용입니다.",
        "author": "이호준",
        "date": "2025-1-3",
    },
]

# FastAPI 애플리케이션 설정
app = FastAPI(
    title="Blog Application",
    description="FastAPI와 Jinja2를 사용한 블로그 애플리케이션",
    docs_url="/documentation",
    redoc_url=None,
)

# Jinja2 템플릿 설정
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def index(request: Request):
    """
    메인 페이지를 렌더링합니다.
    템플릿에는 최신 블로그 포스트 3개가 전달됩니다.
    """
    context = {
        "request": request,
        "title": "Welcome to My Blog",
        "recent_posts": blog_posts[-3:],  # 최신 포스트 3개만 전달
    }
    return templates.TemplateResponse("index.html", context)


@app.get("/blog")
async def blog_list(request: Request):
    """
    블로그 포스트 목록 페이지를 렌더링합니다.
    모든 블로그 포스트가 시간 역순으로 표시됩니다.
    """
    context = {
        "request": request,
        "title": "Blog Posts",
        "posts": blog_posts[::-1],  # 최신 글이 위로 오도록 역순 정렬
    }
    return templates.TemplateResponse("blog.html", context)


@app.get("/blog/{post_id}")
async def blog_post(request: Request, post_id: int):
    """
    특정 블로그 포스트의 상세 페이지를 렌더링합니다.
    post_id는 1부터 시작하며, 실제 리스트의 인덱스는 post_id - 1 입니다.
    """
    try:
        # post_id가 1부터 시작하므로 1을 빼서 실제 인덱스로 변환
        post = blog_posts[post_id - 1]
        context = {
            "request": request,
            "title": post["title"],
            "post": post,
            "post_id": post_id,
        }
        return templates.TemplateResponse("post.html", context)
    except IndexError:
        raise HTTPException(status_code=404, detail="Post not found")