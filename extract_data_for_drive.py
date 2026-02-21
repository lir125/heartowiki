# -*- coding: utf-8 -*-
"""
원본 HTML(도감_웹브라우저로_열기.html)에서 어류/곤충/조류 JSON만 추출합니다.
출력된 creatures_data.json은 GitHub 저장소에 올리거나 구글 드라이브에 업로드해 사용할 수 있습니다.
- GitHub: 저장소에 올린 뒤 config.json에 data_source: "github", github_repo: "owner/repo" 설정.
- 드라이브: 공유를 '링크가 있는 모든 사용자'로 하고 config.json에 drive_file_id 입력.
"""

import json
import re
import sys
from pathlib import Path

# 상위 폴더의 원본 HTML
ORIGINAL_HTML = Path(__file__).parent.parent / "도감_웹브라우저로_열기.html"
OUTPUT_JSON = Path(__file__).parent / "creatures_data.json"


def extract_creatures_data(html: str) -> dict:
    """HTML에서 CREATURES_DATA = { ... }; 블록 추출 후 JSON 파싱."""
    start_marker = "const CREATURES_DATA = "
    start = html.find(start_marker)
    if start == -1:
        raise ValueError("CREATURES_DATA를 찾을 수 없습니다.")
    start += len(start_marker)
    depth = 0
    i = html.index("{", start)
    end = i
    for j in range(i, len(html)):
        if html[j] == "{":
            depth += 1
        elif html[j] == "}":
            depth -= 1
            if depth == 0:
                end = j + 1
                break
    json_str = html[start:end]
    # 이미지 base64 제거하여 용량 축소 (드라이브 업로드용)
    json_str = re.sub(r'"이미지": "data:image[^"]*"', '"이미지": ""', json_str)
    return json.loads(json_str)


def main():
    if not ORIGINAL_HTML.exists():
        print(f"오류: 원본 파일이 없습니다. {ORIGINAL_HTML}")
        sys.exit(1)
    html = ORIGINAL_HTML.read_text(encoding="utf-8")
    data = extract_creatures_data(html)
    if "data_version" not in data:
        data = {"data_version": "1.0.1", **data}
    OUTPUT_JSON.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    counts = {k: len(v) for k, v in data.items() if isinstance(v, list)}
    print(f"저장 완료: {OUTPUT_JSON}")
    print(f"  어류: {counts.get('어류', 0)}개, 곤충: {counts.get('곤충', 0)}개, 조류: {counts.get('조류', 0)}개")
    print("\n다음 단계 (GitHub):")
    print("  1. creatures_data.json을 GitHub 저장소에 올림 (data_version 수정 가능)")
    print("  2. config.json에 data_source: \"github\", github_repo: \"owner/repo\" 설정")
    print("\n또는 (구글 드라이브):")
    print("  1. creatures_data.json을 드라이브에 업로드 → 공유 '링크가 있는 모든 사용자'")
    print("  2. config.json의 drive_file_id에 파일 ID 입력")


if __name__ == "__main__":
    main()
