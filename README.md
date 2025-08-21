1. 탐색기에서 E:\2025,NBO,biz,pro\nbo,11-14 > 우클릭 > open git bash
2. 🔑 GitHub HTTPS 방식으로 비밀번호(토큰) 설정 방법

GitHub에서 Personal Access Token 발급

GitHub 로그인 → 오른쪽 상단 프로필 → Settings

왼쪽 메뉴에서 Developer settings → Personal access tokens → Tokens (classic)

Generate new token 클릭

이름, 기간 설정 후 권한(repo 체크) 선택

발급된 <TOKEN>을 복사해둡니다. (다시 못 보니 꼭 저장!)

git remote set-url origin https://<TOKEN>@github.com/gyeongjuhs2025/nbo.git

//////////////
3. 깃허브 레포에 푸시할 로컬 소스코드를 탐색기로 열고 > 우클릭 > Open bash here > git bash 창이 열림.

user@▒▒▒▒▒▒ MINGW64 /e/2025,NBO,biz,pro/nbo,11-14

$ git init

$ git remote add origin https://github.com/gyeongjuhs2025/nbo.git

$ git add .

$ git commit -m "first commit"

$ git branch -M main

$ git remote set-url origin https://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@github.com/gyeongjuhs2025/nbo.git

$ git push -u origin main

4. GitHub 웹사이트에서 삭제하기

레포지토리 페이지로 이동합니다.

상단 메뉴에서 ⚙️ Settings 탭 클릭.

아래쪽으로 스크롤해서 Danger Zone 섹션을 찾습니다.

Delete this repository 버튼 클릭.

확인을 위해 gyeongjuhs2025/nbo20250902 라는 저장소 이름을 입력.

"I understand the consequences, delete this repository" 버튼 클릭.
