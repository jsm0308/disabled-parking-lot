# {{PROJECT_TITLE}}

{{BADGE_OR_TAGLINE}}

---

## 1. 개요 (Summary)

{{SUMMARY_PARAGRAPH}}

### 배경 · 문제 인식

{{PROBLEM_CONTEXT}}

![문제 인식]({{PROBLEM_IMAGE_URL_OR_PATH}})

### 본 프로젝트의 방향

- {{DIRECTION_BULLET_1}}
- {{DIRECTION_BULLET_2}}
- {{DIRECTION_BULLET_3}}

### 모델·시스템 요약

{{MODEL_SYSTEM_BULLETS_OR_SHORT_PARAGRAPH}}

---

## 2. 기술 스택 (Tech Stack)

| 구분 | 기술 |
|------|------|
| **Vision & AI** | {{STACK_VISION}} |
| **Backend / Infra** | {{STACK_BACKEND}} |
| **Model** | {{STACK_MODEL}} |
| **기타** | {{STACK_OTHER}} |

---

## 3. 시스템 파이프라인 (System Pipeline)

1. {{PIPELINE_STEP_1}}
2. {{PIPELINE_STEP_2}}
3. {{PIPELINE_STEP_3}}
4. {{PIPELINE_STEP_4}}
5. {{PIPELINE_STEP_5}}

### End-to-End 흐름 (Figma / 도식 이미지)

> Figma 등에서 내보낸 PNG/SVG를 `docs/`에 저장하고, 아래 파일명만 맞춥니다.

<p align="center">
  <img src="./docs/{{END_TO_END_DIAGRAM_FILENAME}}" alt="End-to-End pipeline" width="95%" />
</p>

### End-to-End 흐름 (Mermaid)

> GitHub `README` 미리보기에서 자동 렌더링됩니다.

```mermaid
flowchart TB
  A[{{NODE_A}}] --> B[{{NODE_B}}]
  B --> C[{{NODE_C}}]
```

### 참고 도식 (선택)

<p align="center">
  <img src="{{OPTIONAL_REFERENCE_IMAGE_URL}}" alt="Reference diagram" width="90%" />
</p>

---

## 4. 주요 엔지니어링 포인트 (Engineering Points)

### 4.1. {{ENG_POINT_1_TITLE}}

- **문제:** {{ENG_POINT_1_PROBLEM}}
- **해결:** {{ENG_POINT_1_SOLUTION}}
- **구현:** {{ENG_POINT_1_CODE_OR_FILE}}

### 4.2. {{ENG_POINT_2_TITLE}}

- **문제:** {{ENG_POINT_2_PROBLEM}}
- **해결:** {{ENG_POINT_2_SOLUTION}}

### 4.3. {{ENG_POINT_3_TITLE}}

{{ENG_POINT_3_BODY}}

---

## 5. 실행 방법

```bash
{{RUN_COMMAND}}
```

- 기본 설정: {{RUN_NOTES}}

---

## 6. 데모 (Demo)

| 항목 | 경로 |
|------|------|
| 데모 입력 / 샘플 | [`{{DEMO_ASSET_PATH}}`]({{DEMO_ASSET_PATH}}) |

{{DEMO_EXTRA_NOTES}}

---

## 7. Acknowledgements

- {{ACK_1}}
- {{ACK_2}}

---

## 8. Team

| Name |
|------|
| {{MEMBER_1}} |
| {{MEMBER_2}} |

---

## 템플릿 사용 방법

1. 새 프로젝트에 이 파일을 복사한 뒤 `README.md`로 이름을 바꾸거나, 내용만 붙여넣습니다.
2. `{{...}}` 플레이스홀더를 모두 실제 문구로 치환합니다.
3. Figma·도구에서 내보낸 이미지를 `docs/{{END_TO_END_DIAGRAM_FILENAME}}` 경로에 둡니다.
4. Mermaid 블록의 노드·연결을 프로젝트 구조에 맞게 수정합니다.
