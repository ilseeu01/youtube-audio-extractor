# 🎵 YouTube to MP3 Extractor (macOS용)

Python과 yt-dlp를 활용하여 YouTube에서 mp3 음원만 간편하게 추출하는 스크립트입니다.  
macOS 환경에서 최적화되어 있으며, ffmpeg을 사용하여 고음질 mp3 파일로 저장됩니다.

---

## ✅ 설치 방법

### 1. 필수 도구 설치

#### 1-1. Homebrew 설치 (이미 설치되어 있다면 생략)

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

#### 1-2. Python3 설치

```bash
brew install python
```

#### 1-3. ffmpeg 설치 (mp3 추출에 필수)

```bash
brew install ffmpeg
```

#### 1-4. yt-dlp 설치

```bash
pip3 install -U yt-dlp
```

---

## 🚀 사용 방법

1. `youtube_to_mp3.py` 파일을 원하는 폴더에 저장합니다.
2. 터미널을 열고 해당 폴더로 이동합니다.

```bash
cd /path/to/your/folder
```

3. 스크립트 실행:

```bash
python3 youtube_to_mp3.py
```

4. YouTube URL을 입력하면 같은 폴더에 `.mp3` 파일이 저장됩니다.

---

## 💡 추가 팁

- 여러 개 URL을 한 번에 다운로드하고 싶다면, 코드에서 `url`을 리스트 형태로 수정하면 됩니다.
- GUI 버전이 필요하다면 [youtube-dl-gui](https://github.com/MrS0m30n3/youtube-dl-gui) 등의 앱도 참고하세요.

---

## 🛠️ 의존성

- Python 3.x
- ffmpeg
- yt-dlp

---

## 📄 라이선스

MIT License
