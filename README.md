# ♿ KHUDA_CV_8th_DisabledParkingGuard

CCTV 기반 보행 특성 분석을 활용한 장애인 전용 주차구역 부정 이용 탐지(프로토타입)

---

## 🧾 프로젝트 소개
장애인 전용 주차구역 부정 이용은 지속적으로 발생하지만, 기존 단속은 표지/번호판 중심이라 **“표지는 있으나 실제 보행상 장애인은 동승하지 않은 상황”**을 충분히 반영하기 어렵습니다.  
본 프로젝트는 CCTV 영상에서 **주차된 차량에서 하차하는 사람의 보행 특성(Gait)** 을 분석해, **실제 보행상 장애 이용자 탑승 여부를 비식별적으로 추정**하는 시스템을 제안합니다.  
이를 통해 단속의 핵심 공백인 **표지 오남용/부정 이용**을 기술적으로 보완하는 것을 목표로 합니다.

---

## 🎯 주제 선정 동기
- 장애인 전용 주차구역은 이동·접근권 확보를 위한 핵심 인프라이지만, 부정 이용이 잦아 실제 이용자의 접근을 방해합니다.
- 단속 인력·예산 한계로 체계적 단속이 어렵고, 표지 위조·오남용 등은 육안 판별이 쉽지 않습니다.
- 무엇보다 기존 번호판/표지 중심 단속은 **“실제 탑승자(보행상 장애인 동승 여부)”**를 직접 반영하기 어렵습니다.

---

## 🔍 문제 정의
현장에서 확인해야 하는 핵심은 다음 두 가지입니다.

1) **차량이 장애인 전용 구역에 주차했는가**  
2) **보행상 장애인이 실제로 승하차(동승)했는가**

본 프로젝트는 2)에서 발생하는 공백을 줄이기 위해, 신원(개인정보)이 아닌 **행동(보행 패턴)** 기반의 비식별 분석으로 접근합니다.

---

## 💡 제안 방식 (Our Approach)
- CCTV 영상 기반으로 전용구역에 정차한 차량을 탐지하고,
- 해당 차량에서 하차한 인원을 추적하여,
- 보행자의 3D pose sequence로부터 정상 보행/보행 장애(의심) 여부를 분류합니다.

---

## 🧩 System Pipeline
Car Detection (ROI)

↓

Person Getting Off
↓

Multi-object Tracking + Crop

↓

Pose Estimation (3D Skeleton)

↓

Gait Classification (Sequence Model)

↓

Warning / Report (Prototype)


---

## 🛠 구현 구성 (Implementation Overview)

### 1) Detection & Tracking
- **Car Detection**: 장애인 전용 주차 구역 ROI 내부 정차 차량 탐지
- **Person Tracking**: Multi-object Tracking으로 하차 인원 추적
- **Crop 생성**: 하차 보행자만 프레임 시퀀스로 crop 저장 → 사람별 clip 생성

### 2) Pose Estimation
- **MediaPipe Pose (3D)** 기반
- 프레임 단위 pose keypoints(33개) 추출

### 3) Preprocessing
- **Keypoint Selection**: 보행 분석에 핵심인 spine + leg 중심 keypoints 사용
- **Translation 제거**: SpineBase를 원점으로 정렬(상대좌표화)
- **Scaling**: 뼈 길이 기반 scale normalization(체형 차이 완화)
- **Sequence Length 통일**: N frame 고정(짧으면 padding, 길면 crop)

### 4) Gait Classification
- 입력: pose keypoint sequence (t ~ t+N)
- 모델: **LSTM 기반 sequence classifier**
- 출력:
  - Class 0: **Normal Gait**
  - Class 1: **Pathological Gait (Suspicious)**

---

## 🧠 Classification Model (Prototype)
**Model Flow**
- Pose Sequence → LSTM Encoder → Vector Representation → Linear → Softmax(2-class)

**Config (prototype)**
- Hidden size: 256
- LSTM layers: 4

---

## 📊 Training Dataset
- Skeleton 기반 **Pathological Gait Dataset** 활용
- 포함 보행 유형 예시:
  - Normal Gait
  - Antalgic / Stiff-legged / Lurching / Steppage / Trendelenburg gait 등
- Keypoint format:
  - Kinect v2 기반 3D keypoints(x, y, z)

---

## 🚀 Expected Output
- 보행자별 분류 결과 확률(정상/보행 장애 의심)
- 조건 충족 시 관리자/시스템에 경고 알림(프로토타입)
- 단속의 최종 판정이 아닌 **보조 판단 지표**로 활용

---

## 📌 Notes
- 본 프로젝트는 **연구 및 프로토타입 목적**으로 설계되었습니다.
- 실제 서비스 적용 시 데이터 품질, 오탐/미탐, 운영 정책 및 윤리적 고려가 필요합니다.
- 결과는 의사결정을 돕는 **보조 지표**로 사용되어야 합니다.

---

## 📚 Acknowledgements
- Google MediaPipe Pose
- Pathological Gait Dataset
- Kinect v2 Skeleton reference 및 관련 보행 분석 연구

---

## 👥 Team
| Name |
|---|
| 이승준 |
| 표지훈 |
| 박지연 |
| 장승민 |
| 이지민 |
| 송민선 |
| 탁진형 |
| 박진오 |
