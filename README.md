# todo_app

# ropesitory 만들 때 처음부터 파일이 존재하게 만들 생성   
(ex.README.md 또는 License등)
# Sourcetree 사용 시 고려할 사항 (git command line도 동일)
## 1. clone으로 시작하기(원격지[ex. github repo]있는 파일부터 시작해서 로컬 레포지토리에 프로젝트를 시작하면 OK)
## 2. 그런데 이미 로컬 레포지토리에 이미 파일이 존재하면 Sourcetree로 pull(fetch)부터 시작해도 브랜치(remote name)가 나뉘어 있다.
*2번과 같은 경우에는 git bash(terminal)로 git cli환경에서 명령어(command)로 처리해야 한다.)*

```bash
git init # local에서 작업한 root위치의 폴더

git remote add origin(upstream) <원격지 주소> # git에게 remote repo를 등록

git pull(fetch) origin main # remote repo로부터 파일을 취득

git add -A(.)   # git한테 현재 git bash위치에 모든 파일을 등록

git commit -m '<commit message(commit convention)>' # 작업한 내용을 메시지로 등록

git push origin main    # local repo의 변경 사항을 remote repo로 백업
```
