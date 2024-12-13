# from fastapi import FastAPI, Request, HTTPException
# from fastapi.templating import Jinja2Templates


'''
/
/blog/
/blog/1/
/blog/hojun/
/notice/
/notice/1/
'''

# app = FastAPI()

# templates = Jinja2Templates(directory="templates")

# 내가 짠 코드
# blog_posts = [
#     {
#         "id": 1,
#         "title": "첫 블로그 작성",
#         "contents": "블로그 첫 작성입니다.",
#         "author": "이주성"
#     },
#     {
#         "id": 2,
#         "title": "첫 블로그 작성",
#         "contents": "블로그 첫 작성입니다.",
#         "author": "이주성"
#     },
#     {
#         "id": 3,
#         "title": "첫 블로그 작성",
#         "contents": "블로그 첫 작성입니다.",
#         "author": "이주성"
#     },
# ]

# @app.get('/')
# async def index(request: Request):
#     context = {
#         "request": request,
#         "title": "Welcome to My Blog",
#         "recent_posts": blog_posts[-3:],  # 최신 포스트 3개만 전달
#         }
#     return templates.TemplateResponse("index.html", context)

# @app.get('/blog')
# async def blog_list(request: Request):
#     context = {
#         "request": request,
#         "title": "Blog Posts",
#         "posts": blog_posts[::-1],  # 최신 글이 위로 오도록 역순 정렬
#     }
#     return templates.TemplateResponse("blog.html", context)

# 원래는 이렇게 작성하지 않음. 후에 방법에 대해서 배울 예정.
# @app.get('/blog/{post_id}')
# async def blog_post(request: Request, post_id):
#     if post_id is int:
#         post = blog_posts[post_id - 1]
#         context = {
#             "request": request,
#             "title": post["title"],
#             "post": post,
#             "post_id": post_id,
#         }
#         print(post)
#         return templates.TemplateResponse('post.html', context)
#     else:
#         post_personal_list = [post for post in blog_posts if post["author"] == post_id]
#         context = {
#             "request": request,
#             "title": "개인 블로그 글 리스트입니다.",
#             "posts": post_personal_list,
#             "author": post_id,
#         }
#         print(post_personal_list)
#         return templates.TemplateResponse('post.html', context)


# @app.get('/blog/{post_author}')
# async def blog_personal_list(request: Request, post_author: str):
#     post_personal_list = [x for post in blog_posts if post["author"] == post_author]
#     context = {
#         "request": request,
#         "title": "개인 블로그 글 리스트입니다.",
#         "posts": post_personal_list,
#         "author": post_author,
#     }
#     return templates.TemplateResponse('post.html', context)

# notices = [
#     {
#         "title": "첫번째 공지입니다.",
#         "content": "내용입니다."
#     }
# ]

# @app.get('/notice')
# async def notice_list(request: Request):
#     context = {
#         "request": request,
#         "title": "Notices",
#         "notices": notices[::-1],  # 최신 글이 위로 오도록 역순 정렬
#     }
#     return templates.TemplateResponse("notice.html", context)

# @app.get('/notice/{notice_id}')
# async def notice_detail(request: Request, notice_id: int):
#     notice = notices[notice_id - 1]
#     context = {
#         "request": request,
#         "title": notice["title"],
#         "post": notice,
#         "post_id": notice_id,
#     }
#     return templates.TemplateResponse('notice_detail.html', context)


# 호준 강사님 코드
# from fastapi import FastAPI, Request, HTTPException
# from fastapi.templating import Jinja2Templates

# # 블로그 포스트 데이터
# blog_posts = [
#     {
#         "id": 1,
#         "title": "첫번째 포스트",
#         "contents": "첫번째 포스트 내용입니다.",
#         "author": "이호준",
#         "date": "2025-1-1",
#     },
#     {
#         "id": 2,
#         "title": "두번째 포스트",
#         "contents": "두번째 포스트 내용입니다.",
#         "author": "이호준",
#         "date": "2025-1-2",
#     },
#     {
#         "id": 3,
#         "title": "세번째 포스트",
#         "contents": "세번째 포스트 내용입니다.",
#         "author": "이호준",
#         "date": "2025-1-3",
#     },
# ]

# blog_notice = [
#     {
#         "id": 1,
#         "title": "첫번째 공지",
#         "contents": "첫번째 공지 내용입니다.",
#         "author": "이호준",
#         "date": "2025-1-1",
#     },
#     {
#         "id": 2,
#         "title": "두번째 공지",
#         "contents": "두번째 공지 내용입니다.",
#         "author": "이호준",
#         "date": "2025-1-2",
#     },
# ]

# # FastAPI 애플리케이션 설정
# app = FastAPI(
#     title="Blog Application",
#     description="FastAPI와 Jinja2를 사용한 블로그 애플리케이션",
#     docs_url="/documentation",
#     redoc_url=None,
# )

# # Jinja2 템플릿 설정
# templates = Jinja2Templates(directory="templates")


# @app.get("/")
# async def index(request: Request):
#     return templates.TemplateResponse(
#         "index.html", {"request": request, "recent_posts": blog_posts[-3:]}
#     )


# @app.get("/blog")
# async def blog_list(request: Request):
#     return templates.TemplateResponse(
#         "blog.html", {"request": request, "posts": blog_posts[::-1], "title": "blog"}
#     )


# # 나중에 배웁니다. 함께 수정해봐요.
# @app.get("/blog/{post_author}")
# async def blog_post(request: Request, post_author: str):
#     print(post_author)
#     if post_author.isdigit():
#         post = blog_posts[int(post_author) - 1]
#         return templates.TemplateResponse(
#             "post.html", {"request": request, "post": post}
#         )
#     else:
#         filter_post = list(
#             filter(lambda post: post["author"] == post_author, blog_posts)
#         )[::-1]
#         return templates.TemplateResponse(
#             "blog.html", {"request": request, "posts": filter_post}
#         )


# @app.get("/blog/{post_id}")
# async def blog_post(request: Request, post_id: int):
#     post = blog_posts[post_id - 1]
#     return templates.TemplateResponse("post.html", {"request": request, "post": post})


# @app.get("/notice")
# async def notice_list(request: Request):
#     return templates.TemplateResponse(
#         "blog.html",
#         {"request": request, "posts": blog_notice[::-1], "title": "notice"},
#     )


# @app.get("/notice/{post_id}")
# async def notice_post(request: Request, post_id: int):
#     post = blog_notice[post_id - 1]
#     return templates.TemplateResponse("post.html", {"request": request, "post": post})