# ♿ KHUDA_CV_8th_DisabledParkingGuard
CCTV 영상 기반 보행 특성 분석을 통한 장애인 전용 주차구역 부정 이용 탐지 (Prototype)

---

## 🧾 프로젝트 개요
장애인 전용 주차구역 부정 이용은 지속적으로 발생하지만, 기존 단속은 표지·번호판 중심으로 이루어져  
“표지는 있으나 실제 보행상 장애인이 동승하지 않은 경우”를 구분하는 데 한계가 있습니다.

본 프로젝트는 CCTV 영상에서  
**장애인 전용 주차구역에 주차된 차량에서 하차하는 사람의 보행 특성(Gait)** 을 분석하여  
해당 차량에 **보행상 장애 이용자가 실제로 탑승했을 가능성**을 비식별적으로 추정하는  
컴퓨터 비전 기반 프로토타입 시스템입니다.

---

## 🎯 문제 정의 및 접근 배경
현장 단속에서 핵심적으로 확인해야 하는 정보는 다음 두 가지입니다.

1. 차량이 장애인 전용 주차구역에 주차했는가  
2. 보행상 장애인이 실제로 승하차했는가  

기존 시스템은 주로 **차량 중심(번호판, 표지 인식)** 판단에 머물러 있으며,  
실제 탑승자의 상태(보행 특성)는 반영하지 못합니다.

본 프로젝트는 개인정보(신원, 얼굴 등)가 아닌  
**행동 정보(보행 패턴)** 만을 활용하여  
보조적 판단 근거를 제공하는 것을 목표로 합니다.

---

## 🧩 System Pipeline

CCTV MP4 입력

↓

ROI 기반 차량 탐지 (YOLO)

↓

차량 하차 인원 감지

↓

Multi-object Tracking (BoT-SORT)

↓

하차 보행자 Crop 이미지 시퀀스 생성

↓

보행자별 영상 재구성

↓

3D Pose Estimation (MediaPipe Pose)

↓

Pose Sequence 전처리

↓

LSTM 기반 보행 분류 (Inference)


위 파이프라인 전 과정을 하나의 실행 파일(`MASTER_RUN.py`)로 연결한 구현을 포함하였습니다.

---

## 🛠 주요 구현 단계

### 1️⃣ 차량 탐지 및 하차 보행자 추적
- **ROI 지정**: 장애인 전용 주차구역을 사용자가 직접 지정
- **차량 탐지**: YOLO 기반 객체 탐지
- **보행자 추적**: BoT-SORT 기반 Multi-object Tracking
- **ID 안정화**: appearance + IoU + 거리 기반 ID 보정
- **결과**: 하차한 보행자만 사람별 이미지 시퀀스로 crop 저장

관련 코드:
  `roi_pick.py`
  `tracker.py`
  `id_fix.py`
  `utils.py`

---

### 2️⃣ 보행자 영상 생성
- 보행자 ID별 crop 이미지들을 하나의 영상(mp4)으로 재구성
- 마지막 프레임 기준 특정 구간을 선택하여 보행 구간만 사용
- 프레임 누락 시 이전 프레임으로 보간하여 자연스러운 재생

관련 코드:
`make_videos.py`

---

### 3️⃣ 3D Pose Estimation
- **MediaPipe Pose** 기반 3D skeleton 추출
- 입력: 보행자별 mp4 영상
- 출력: 프레임별 3D keypoint를 포함한 `.npz` 파일

관련 코드:
  `mediapipe_test.py`

---

### 4️⃣ Pose 데이터 전처리
MediaPipe Pose 출력과 보행 분류 모델 입력을 맞추기 위해 다음 전처리를 수행합니다.

- **Keypoint Selection**
  - Spine + Leg 중심 keypoint 사용 (총 11개 관절)
- **Translation 제거**
  - SpineBase를 원점으로 정렬
- **Scaling**
  - 뼈 길이 기반 scale normalization
- **Sequence Length 통일**
  - 모든 시퀀스를 고정 길이(기본 90 frame)로 통일
  - 부족한 경우 zero padding, 초과 시 crop

출력: LSTM 입력용 CSV 파일

관련 코드:
  `media_csv_v2.py`

---

### 5️⃣ 보행 분류 (Inference)
- 입력: 전처리된 pose sequence CSV
- 모델: **LSTM 기반 보행 분류 모델**
- 출력:
  - Normal Gait
  - Pathological Gait (의심)

※ 본 레포지토리에는 **학습 과정은 포함되어 있지 않으며**,  
사전 학습된 모델(`best.pt`)을 이용한 **추론(inference) 단계만 포함**됩니다.

관련 코드:
  `infinf.py`

---

## 🧠 보행 분류 모델 개요 (Prototype)
- 입력: (T × 33) pose keypoint sequence
- 구조:
  - LSTM Encoder
  - Fully Connected Layer
  - Softmax (2-class)
- 설정 예:
  - Hidden size: 256
  - LSTM layers: 4

---
## 🚀 실행 구조
전체 파이프라인은 아래 파일 하나로 실행됩니다.

```bash
python MASTER_RUN.py
```

MASTER_RUN.py 내부에서 다음을 제어합니다.

입력 영상 경로

ROI 설정

보행자 선택

전처리 및 inference 파라미터

---

## 📚 Acknowledgements
- Google MediaPipe Pose
- Pathological Gait Dataset
- Kinect v2 Skeleton Reference
- 보행 분석 관련 선행 연구

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
