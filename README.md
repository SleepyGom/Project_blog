# 하루 한곡
  * 자신이 좋아하는 노래를 업로드 후 공유하거나, 자신의 기분이나 행동, 상황에 맞춰 듣고 싶은 음악을 검색해보고 서로 공유해보는 블로그

# 1. 목표와 기능
## 1.1 목표
    * 회원가입 기능과 로그인 글쓰기 기능을 통해 유저가 직접 자신이 좋아하는 음악을 공유하는 블로그
    * 검색기능을 통해 유저가 찾고 싶은 음악을 찾아 공유 받을 수 있는 블로그
## 1.2 기능
    * 유저용 기능
      - 회원가입, 로그인, 로그아웃
    * 게시판 기능
      - 글 쓰기, 글 삭제, 글 수정, 삭제

# 2. 개발 환경 및 배포 URL
## 2.1 개발 환경
```
gitasgiref==3.7.2
Django==4.2.3
sqlparse==0.4.4
tzdata==2023.3
```
## 2.2 개발 기간
    * 2023년 07월 17일 ~ 2023년 07월 20일

## 2.3 배포 URL
    * 추후에 추가

# 3. 프로젝트 구조
```
Mini_project_Blog
├─ .git
│  ├─ COMMIT_EDITMSG
│  ├─ config
│  ├─ description
│  ├─ FETCH_HEAD
│  ├─ HEAD
│  ├─ hooks
│  │  ├─ applypatch-msg.sample
│  │  ├─ commit-msg.sample
│  │  ├─ fsmonitor-watchman.sample
│  │  ├─ post-update.sample
│  │  ├─ pre-applypatch.sample
│  │  ├─ pre-commit.sample
│  │  ├─ pre-merge-commit.sample
│  │  ├─ pre-push.sample
│  │  ├─ pre-rebase.sample
│  │  ├─ pre-receive.sample
│  │  ├─ prepare-commit-msg.sample
│  │  ├─ push-to-checkout.sample
│  │  └─ update.sample
│  ├─ index
│  ├─ info
│  │  └─ exclude
│  ├─ logs
│  │  ├─ HEAD
│  │  └─ refs
│  │     ├─ heads
│  │     │  └─ main
│  │     └─ remotes
│  │        └─ origin
│  │           └─ main
├─ .gitignore
├─ myapp
│  ├─ account
│  │  ├─ admin.py
│  │  ├─ apps.py
│  │  ├─ migrations
│  │  │  ├─ __init__.py
│  │  │  └─ __pycache__
│  │  │     └─ __init__.cpython-311.pyc
│  │  ├─ models.py
│  │  ├─ templates
│  │  │  └─ account
│  │  │     ├─ login.html
│  │  │     └─ signin.html
│  │  ├─ tests.py
│  │  ├─ views.py
│  │  ├─ __init__.py
│  │  └─ __pycache__
│  │     ├─ admin.cpython-311.pyc
│  │     ├─ apps.cpython-311.pyc
│  │     ├─ models.cpython-311.pyc
│  │     ├─ views.cpython-311.pyc
│  │     └─ __init__.cpython-311.pyc
│  ├─ app
│  │  ├─ asgi.py
│  │  ├─ settings.py
│  │  ├─ urls.py
│  │  ├─ wsgi.py
│  │  ├─ __init__.py
│  │  └─ __pycache__
│  │     ├─ settings.cpython-311.pyc
│  │     ├─ urls.cpython-311.pyc
│  │     ├─ wsgi.cpython-311.pyc
│  │     └─ __init__.cpython-311.pyc
│  ├─ blog
│  │  ├─ .ipynb_checkpoints
│  │  │  └─ Untitled-checkpoint.ipynb
│  │  ├─ admin.py
│  │  ├─ apps.py
│  │  ├─ migrations
│  │  │  ├─ 0001_initial.py
│  │  │  ├─ __init__.py
│  │  │  └─ __pycache__
│  │  │     ├─ 0001_initial.cpython-311.pyc
│  │  │     └─ __init__.cpython-311.pyc
│  │  ├─ models.py
│  │  ├─ templates
│  │  │  └─ blog
│  │  │     ├─ base.html
│  │  │     ├─ blogdetail.html
│  │  │     ├─ bloglist.html
│  │  │     ├─ edit.html
│  │  │     ├─ index.html
│  │  │     ├─ search.html
│  │  │     └─ write.html
│  │  ├─ tests.py
│  │  ├─ Untitled.ipynb
│  │  ├─ views.py
│  │  ├─ __init__.py
│  │  └─ __pycache__
│  │     ├─ admin.cpython-311.pyc
│  │     ├─ apps.cpython-311.pyc
│  │     ├─ models.cpython-311.pyc
│  │     ├─ views.cpython-311.pyc
│  │     └─ __init__.cpython-311.pyc
│  ├─ db.sqlite3
│  ├─ manage.py
│  ├─ requirements.txt
│  └─ static
│     ├─ css
│     │  ├─ base.css
│     │  ├─ login.css
│     │  ├─ register.css
│     │  └─ reset.css
│     ├─ img
│     └─ js
└─ README.md
```
# 4. 실행 화면
