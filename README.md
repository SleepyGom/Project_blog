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
## 4.1 유저 기능
   * 회원가입
![127 0 0 1_8000_signin_](https://github.com/SleepyGom/Project_blog/assets/93717960/d2dbfb4b-3b8b-4622-bb1c-454c3b92b018)
   * 로그인      
![127 0 0 1_8000_login_](https://github.com/SleepyGom/Project_blog/assets/93717960/800ef31b-0595-4470-a222-f82eb5af4ddc)
  * 메인 및 로그아웃
![127 0 0 1_8000_](https://github.com/SleepyGom/Project_blog/assets/93717960/ff716e5e-e2ba-496d-b592-6e713d1edd7e)

## 4.2 게시판 기능
  * 디테일
![127 0 0 1_8000_bloglist_9](https://github.com/SleepyGom/Project_blog/assets/93717960/49643e03-2c8c-4410-93c8-b9f89bca3225)

  * 글 쓰기
![127 0 0 1_8000_blogwrite_](https://github.com/SleepyGom/Project_blog/assets/93717960/c20d06a3-471e-4fde-96fb-38d4e2937323)

  * 글 수정
![127 0 0 1_8000_bloglist_9_edit_](https://github.com/SleepyGom/Project_blog/assets/93717960/46f7d9f8-78dd-4de3-88f2-a640c4b69c32)

  * SEARCH 기능
![127 0 0 1_8000_bloglist_serach__csrfmiddlewaretoken=WhYJfQGkNHnIpSz3783uilWdZ2J6m8d55lq3F8s7oE1ScPmp47RjLgp99QdL8AO4 search=%EC%B0%BE%EC%95%84](https://github.com/SleepyGom/Project_blog/assets/93717960/b26244b7-cbec-4ff4-a48b-2c2456bc5bef)
```Django
from django.db.models import Q

def search(request):
    content_list = Content.objects.all().order_by('-id')
    search = request.GET.get('search',"")
    print(search)
    if search:
        content_list = content_list.filter(
                Q(title__icontains=search) |
                Q(content__icontains=search)
                )
        return render(request, 'blog/search.html', {'content_list':content_list,'search':search})
    else:
        return render(request, 'blog/search.html')
```

# 5. 오류 사항
 * pk 값 오류 (해결 완료)
   ```Django
   def edit(request,pk):
    content = Content.objects.get(pk=pk)
    if request.method == 'POST':
        content.title = request.POST['title']
        content.content = request.POST['content']

        content.save()
        return redirect('/bloglist/' + str(content.pk))
    else:
        content = Content.objects.get(pk=pk)
        return render(request, 'blog/edit.html', {'content':content})
   ```
   위 코드에서 return 값 중에 'content' : content 값을 넘겨주기 전 content= Content.objects.all()로 파일을 넘겨서 html로 값들을 넘겨 받을 시 pk에는 아무 값이 들어가지 않았다.
   현재는 get(pk=pk)를 이용하여 content로 넘겨주고 그 값들을 "{% url 'edit' content.id %}" 이런식으로 넘겨주어 해결하였다.



