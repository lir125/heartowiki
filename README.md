# 두타위키 - 데스크톱 앱 (EXE)

실행 시 **GitHub** 저장소의 **heartowiki.xlsx**를 다운로드해 파싱한 뒤, JSON 형태로 캐시해 UI에 표시합니다. 데이터 소스는 **GitHub만** 사용합니다.

---

## 0. 아래 내용이 이해가 안되면 exe 파일만 사용해도 문제 없습니다.

### 문제가 생기면 문의 주세요.

#### discord : lir_125

## 1. 데이터 준비 — GitHub의 heartowiki.xlsx

1. **GitHub 저장소 루트에 heartowiki.xlsx 올리기**  
   - 시트: **어류**, **곤충**, **조류**, (선택) **요리** / **미식 라이프**  
   - 열 머리글: `명칭`(또는 `이름`), `지역`(또는 `위치`), `레벨`, `날씨영향` 등

2. **config.json** (데이터 폴더: `문서\Heartowiki\data`)  
   ```json
   {
     "github_repo": "사용자명/저장소명",
     "github_data_branch": "main"
   }
   ```
   - 앱은 항상 해당 저장소의 **heartowiki.xlsx**만 받아 파싱한 뒤 **cache.json**으로 저장합니다.

3. **데이터 새로고침** 버튼으로 GitHub에서 heartowiki.xlsx를 다시 받아 JSON으로 반영합니다.

---

(구 드라이브/Dropbox 데이터 소스 설명 생략.)

2. **구글 드라이브에 업로드**  
   - `creatures_data.json` 을 구글 드라이브에 업로드합니다.  
   - 해당 파일 우클릭 → **공유** → **일반 액세스**를 **“링크가 있는 모든 사용자”**로 설정합니다.

3. **파일 ID 또는 스프레드시트 ID**  
   - **Drive 파일**: `https://drive.google.com/file/d/여기가파일ID/view` 에서 `d/` 와 `/view` 사이가 **파일 ID**입니다.  
   - **Google Sheets**: `https://docs.google.com/spreadsheets/d/여기가ID/edit` 에서 `d/` 와 `/edit` 사이가 **스프레드시트 ID**입니다.  
     시트는 **공유 → 링크가 있는 모든 사용자(보기)** 로 설정하고, **시트 이름**을 **어류**, **곤충**, **조류**로 두면 앱이 그 시트를 읽습니다.

4. **config.json 설정** (엑셀/JSON/Sheets 모두 동일)  
   - 앱 **최초 실행 후** `C:\Users\<사용자>\Documents\Heartowiki\data` 폴더가 생성됩니다.  
   - 그 안의 `config.json` 에 `drive_file_id` 를 넣습니다. (없으면 생성)
   ```json
   {
     "drive_file_id": "도감데이터_파일ID",
     "update_info_file_id": "앱업데이트정보_파일ID"
   }
   ```
   - `update_info_file_id`는 **앱 업데이트**를 쓸 때만 넣으면 됩니다. (선택)

### C. Dropbox(또는 직접 URL)에서 도감 데이터 사용

1. **Dropbox에 파일 올리기**
   - `heartowiki.xlsx` 또는 `creatures_data.json`을 Dropbox 폴더에 업로드합니다.
   - 해당 파일 **우클릭 → 공유 → 링크 만들기**를 선택해 **공유 링크**를 복사합니다.
   - 링크 예: `https://www.dropbox.com/s/xxxxxxxx/heartowiki.xlsx?dl=0`
   - **끝이 `?dl=0`이면 `?dl=1`로 바꿉니다.** (직접 다운로드용)  
     → `https://www.dropbox.com/s/xxxxxxxx/heartowiki.xlsx?dl=1`

2. **config.json 설정** (데이터 폴더: `문서\Heartowiki\data`)
   ```json
   {
     "data_source": "url",
     "data_url": "https://www.dropbox.com/s/여기에공유코드/heartowiki.xlsx?dl=1"
   }
   ```
   - 앱이 `data_source`가 `"url"`일 때 `data_url` 주소에서 파일을 받습니다.
   - Dropbox 말고 **다른 공개 다운로드 URL**도 그대로 넣으면 됩니다.

3. **데이터 업데이트**: Dropbox에서 파일만 새 버전으로 교체하면, 앱에서 **데이터 새로고침**으로 최신 내용을 받을 수 있습니다.

---

## 2. EXE 빌드

**Windows에서 exe 빌드 시**: pywebview가 pythonnet을 사용하므로 **Python 3.12**가 필요합니다 (3.14는 pythonnet 미지원).  
[Python 3.12 다운로드](https://www.python.org/downloads/) 후 설치하고, `venv` 폴더를 삭제한 뒤 아래를 실행하세요.

**실행 방법**: `cmd`를 연 뒤 `cd heartowiki` 후 `build_exe.bat` 입력. 또는 탐색기에서 `build_exe.bat` 더블클릭.  
(`cmd /c "build_exe.bat"` 처럼 따옴표로 감싸면 배치가 깨질 수 있으니 피하세요.)

```bash
cd heartowiki
build_exe.bat
```

또는 수동:

```bash
cd heartowiki
python -m venv venv
venv\Scripts\activate
pip install pywebview requests pyinstaller
pyinstaller --noconfirm --onedir --windowed --name "Heartowiki" --icon icon.png --add-data "index.html;." main.py
```

빌드 결과: `dist/Heartowiki/Heartowiki.exe` (폴더 형태. pywebview/pythonnet DLL 오류 방지를 위해 `--onedir` 사용. 배포 시 `Heartowiki` 폴더 전체를 압축해 전달하면 됩니다.)

---

## 3. EXE 실행 및 배포

- **실행**: `dist\Heartowiki\Heartowiki.exe` 를 더블클릭합니다. (폴더 안의 exe를 실행해야 하며, Heartowiki 폴더 전체를 이동해도 됩니다.)
- **데이터 폴더**: 앱 최초 실행 시 `C:\Users\<사용자>\Documents\Heartowiki\data` 폴더가 자동 생성됩니다.
- **저장 위치** (모두 위 데이터 폴더):
  - `config.json` — data_source, github_repo(또는 drive_file_id), 앱 업데이트 설정 (`config.example.json` 참고)
  - `collection.json` — 개인 수집 정보 (별 갯수 = 몇 성까지 잡았는지, 사용자 추가 생물)
  - `settings.json` — 현재 탭, 정렬, 색상 등
  - `cache.json` — 도감 데이터 캐시 (GitHub/드라이브에서 받은 데이터)
- exe만 배포해도 되며, 사용자에게 **문서\Heartowiki\data\config.json** 에 `data_source`·`github_repo`(또는 `drive_file_id`) 설정을 안내하면 됩니다.

---

## 4. 데이터 업데이트 방법

- **GitHub**: 저장소의 `creatures_data.json`(또는 `github_data_path`)을 수정하고 `data_version`을 올리면, 사용자가 **업데이트 확인** 시 새 버전 안내를 보고 **데이터 새로고침**으로 적용할 수 있습니다.
- **구글 드라이브**: 드라이브의 **heartowiki.xlsx** 또는 `creatures_data.json` 내용을 수정·교체합니다.
- 사용자는 앱에서 **“데이터 새로고침”** 버튼을 누르면 최신 데이터를 다시 받아옵니다.

---

## 5. 앱(EXE) 업데이트 — 구글 드라이브 또는 GitHub

앱 업데이트는 **구글 드라이브** 또는 **GitHub Releases** 중 하나로 설정할 수 있습니다.  
사용자가 **「업데이트 적용」** 버튼을 누르면 새 exe를 받아 **자동으로 교체·재시작**됩니다.

### A. GitHub 사용 (권장)

1. **GitHub 저장소**에 exe를 올리고 **Releases**로 버전 관리합니다.
2. **Releases** → **Create a new release** → 태그 예: `v1.0.1`, 제목/설명 입력 후 **exe 파일을 첨부**하여 발행합니다.
3. 데이터 폴더 `config.json` 에 다음을 넣습니다.
   ```json
   {
     "drive_file_id": "도감데이터_파일ID",
     "update_source": "github",
     "github_repo": "사용자명/저장소명"
   }
   ```
4. 사용자는 앱에서 **「앱 업데이트 확인」** → **「업데이트 적용」** 클릭 시 새 exe가 다운로드되고, 앱이 종료된 뒤 새 버전이 자동 실행됩니다.

- `update_source`가 `"github"`이면 **최신 Release**의 태그 버전과 exe 첨부 파일을 사용합니다.
- **버전**: `main.py`의 `APP_VERSION`을 올리고 exe를 빌드한 뒤, GitHub에 새 Release(태그 예: v1.0.2)와 exe를 올리면 됩니다.

### B. 구글 드라이브 사용

1. **app_update.json** 준비 (형식은 `app_update.example.json` 참고):
   - `version`: 새 버전 (예: 1.0.1)
   - `exe_file_id`: 구글 드라이브에 업로드한 **새 exe 파일**의 파일 ID
   - `message`: 업데이트 안내 문구
2. **app_update.json**과 **새 exe**를 구글 드라이브에 업로드하고, **링크가 있는 모든 사용자**로 공유합니다.
3. `config.json` 에서:
   ```json
   {
     "drive_file_id": "도감데이터_파일ID",
     "update_source": "google_drive",
     "update_info_file_id": "app_update.json_파일ID"
   }
   ```
4. 사용자는 **「앱 업데이트 확인」** → **「업데이트 적용」**으로 바로 업데이트하거나, **「브라우저로 다운로드」**로 수동 설치할 수 있습니다.

---

## 6. 구조 요약

| 항목 | 설명 |
|------|------|
| `main.py` | 데이터 폴더 생성, 구글 드라이브 다운로드, collection/settings/cache JSON 저장, pywebview 창 |
| `index.html` | 도감 UI (탭, 검색, 필터, 카드, 수집 성수, 생물 추가). 데이터는 Python API로 주입 |
| **데이터 폴더** `문서\Heartowiki\data` | |
| `config.json` | `data_source`(github/google_drive), `github_repo`, `github_data_branch`, `github_data_path`, `drive_file_id`, `update_source`, `update_info_file_id` (`config.example.json` 참고) |
| `collection.json` | 개인 수집 정보: 별 갯수(몇 성까지 잡았는지), 사용자 추가 생물 |
| `settings.json` | 현재 탭, 정렬, 색상 등 |
| `cache.json` | 도감 데이터 캐시 (드라이브 연동 실패 시 사용) |
| `extract_data_for_drive.py` | 원본 HTML에서 어류/곤충/조류 JSON 추출 → 구글 드라이브 업로드용 |
| `app_update.example.json` | 앱 업데이트용 JSON 예시 (드라이브에 업로드 후 `app_update.json` 등으로 사용) |

---

## 7. 요구 사항

- **Windows**: Python 3.8+ (빌드 시), WebView2(Edge) (exe 실행 시, Windows 10/11에는 보통 포함)
- **패키지**: pywebview, requests (PyInstaller로 exe에 포함됨)
