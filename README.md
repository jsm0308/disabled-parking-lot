# KHUDA_CV_8th_DisabledParkingGuard


# Gait Classification for Accessible Parking Enforcement

CCTV 영상 기반으로 차량에서 하차한 보행자의 보행 형태를 분석하여  
정상 보행 / 보행 장애(의심) 여부를 분류하는 딥러닝 기반 시스템입니다.

## 🔍 Overview

본 프로젝트는 장애인 전용 주차구역에서의 부정 이용을 방지하기 위해  
하차 보행자의 보행 패턴을 정량적으로 분석하는 것을 목표로 합니다.

전체 파이프라인은 다음과 같은 단계로 구성됩니다.

1. 차량 정차 감지 (Car Detection)
2. 사람 하차 감지
3. Multi-object Tracking을 통한 보행자 추적
4. Pose Estimation (3D Skeleton)
5. Pose Sequence Classification
6. 경고 알림 전송

## 🧩 System Pipeline

Car Detection
↓
Person Getting Off
↓
Multi-object Tracking
↓
Pose Estimation (3D Skeleton)
↓
Gait Classification
↓
Warning Alert

## 🧠 Classification Model Structure

Multi-object tracking을 통해 하차한 보행자만 crop한 뒤  
연속된 pose sequence를 입력으로 받아 분류를 수행합니다.

### Model Flow

- 입력: 연속된 pose keypoint sequence (t ~ t+N)
- Pose Encoder (LSTM 기반)
- Pose Decoder
- Vector Representation of Pose Sequence
- Linear Layer
- Softmax (2-class classification)

### Classification Output

- Class 0: 정상 보행 (Normal Gait)
- Class 1: 보행 장애 (Pathological Gait)

Model Configuration
- Hidden vector size: 256  
- LSTM layers: 4  

## 🛠 Data Preprocessing

### 1. Keypoint Selection
- MediaPipe 또는 Kinect Skeleton 기반 keypoint 사용
- 최종적으로 spine + leg keypoint만 사용
- 관련 논문에서 leg keypoint만 사용했을 때 가장 높은 성능** 확인

### 2. Translation 제거
- `SpineBase`를 원점 `(0, 0, 0)`으로 고정
- 나머지 keypoint를 상대 좌표로 정렬

### 3. Scaling
- 뼈 길이 평균을 기준으로 scale normalization
- 개인별 체형 차이 제거 목적

### 4. Sequence Length 통일
- 모든 영상 길이를 **100 frame**으로 통일
- 짧은 경우: 뒤에 zero padding
- 긴 경우: 앞부분 crop

## 📊 Training Dataset

### Pathological Gait Dataset
다음과 같은 보행 유형을 포함한 skeleton 기반 데이터셋을 사용합니다.

- Normal Gait
- Antalgic Gait
- Stiff-legged Gait
- Lurching Gait
- Steppage Gait
- Trendelenburg Gait

### Keypoint Format
- Kinect v2 기반 25개 keypoint
- 각 keypoint는 3D 좌표 (x, y, z)로 구성

## 🧍 Pose Estimation Model

### MediaPipe Pose
- Google MediaPipe 기반 3D Pose Estimation 모델 사용
- 총 33개의 keypoint 출력
- 눈, 코, 입, 손, 발 등 세밀한 관절 포함

#### 주요 특징
- 빠른 추론 속도
- 별도 depth sensor 없이 3D 추정 가능
- CCTV 환경에 적합

## 🚀 Expected Output

- 보행자별 분류 결과 확률
- 정상 / 보행 장애 여부 판정
- 조건 충족 시 관리자 또는 시스템에 경고 알림 전송

## 📌 Notes

- 본 프로젝트는 연구 및 프로토타입 목적으로 설계되었습니다.
- 실제 서비스 적용 시 법적·윤리적 검토가 필요합니다.
- 분류 결과는 보조 판단 지표로 활용되어야 합니다.

## 📚 Acknowledgements

- MediaPipe Pose (Google)
- Pathological Gait Dataset
- Kinect v2 Skeleton Reference
- 관련 보행 분석 연구 논문들
