# KHUDA_CV_8th_DisabledParkingGuard

## 🧾 프로젝트 설명 (3줄)

장애인 전용 주차구역 불법 주차는 계속 증가하지만, 단속은 표지·번호판 중심이라 오남용을 잡기 어렵다.  
본 프로젝트는 주차된 차량에서 하차하는 사람의 보행 특성을 분석해, 실제 보행상 장애인 탑승 여부를 비식별적으로 추정한다.  
이를 통해 단속의 핵심 공백인 “표지는 있는데 실제 장애인은 없었던 상황”을 기술적으로 보완한다.

---

## 🧭 주제 선정 동기

### 1) 장애인 주차 구역이란?

장애인 주차 구역은 장애인 출입이 가능한 건축물의 **출입구**와 장애인용 **승강설비**에 가장 가까운 곳에 설치한다.  
대중교통 이용이 어려운 상황에서 장애인은 차량 이용이 필수인 경우가 많다.  
따라서 장애인 주차 구역은 **접근권 확보**를 위한 기반 시설이다.

> 🖼️ **[이미지 추가 예정]** 장애인 주차구역 예시 사진  
> 아래 “이미지 넣는 법” 참고해서 붙이면 된다.

---

### 2) 장애인 주차 구역 관련 법

#### [장애인복지법 시행규칙]

지자체는 장애인사용자동차등표지를 발급할 때  
**보행상 장애 여부를 표지에 따로 표시**해야 한다.  
(개정: 2012. 7. 27., 2019. 6. 4.)

#### [장애인사용자동차 표지 발급 대상]

아래 중 하나에 해당하면 장애인사용자동차 표지 발급이 가능하다.

- 「장애인복지법」에 따라 등록한 장애인  
- 장애인과 주소를 같이 하며 함께 거주하는 보호자 범위  
  (배우자, 직계혈족, 형제자매, 배우자 직계혈족 등)  
- 재외동포 국내거소신고자 또는 외국인등록자 중  
  보건복지부장관 고시에 따른 **보행상 장애인**

#### [장애인전용주차구역 과태료 및 단속 기준]

원칙적으로 표지 부착 차량이라도  
**장애인이 함께 탑승해야** 주차가 가능하다.

다만 공동주택 등 주거지역 특성은 고려해  
단속 기준을 **탄력 적용**할 필요가 있다고 명시된다.

핵심 규칙은 아래다.

- **보행상 장애인과 보호자에게 표지 발급**  
- **장애인 승하차 시에만 주차 가능**

> 🖼️ **[이미지 추가 예정]** 법/표지 관련 시각 자료  
> “표지 발급 조건”과 “동승 원칙”을 이미지로 넣으면 이해가 빨라진다.

---

### 2-1) 이 문제를 “시각 정보”로 처리해도 되는 이유

현장 단속의 핵심은 결국 아래 사실 확인이다.

- 차량이 전용 구역에 주차했는가  
- 장애인이 실제로 승하차했는가  

이 둘은 **CCTV 영상만으로도 관찰 가능한 사건**이다.  
특히 “장애인 실제 탑승 여부”는 표지 자체가 아니라  
**하차한 사람의 보행 특성**에서 단서가 나온다.

즉, 본 문제는 개인정보(신원) 대신  
**행동(보행 패턴) 기반의 비식별 판단**으로 접근할 타당성이 있다.

---

### 2-2) 문제 상황: 불법 주차 증가

장애인 주차 구역 불법 주차 건수 증가는  
정작 그 공간이 필요한 장애인의 이용을 막는다.  
이는 장애인의 **완전한 사회 참여**와 **사회 통합**을 저해한다.

- 장애인전용주차구역 위반은 실제 이용자를 배제한다.  
- 불법 주차·방해 행위는 지속되며 증가 추세다.  

> 📊 **[표 추가 예정]** 연도별 불법 주차(또는 신고) 건수 표/그래프  
> 표를 넣으면 “문제의 크기”가 한 번에 전달된다.

---

### 3) 불법 주정차 단속 과정의 문제점

#### ✔ 신고 처리 문제

- 전담 인력·예산 부족으로 단속이 체계적이지 않다.  
- 스티커 위조 등은 육안으로 진위 판별이 어렵다.

#### ✔ 주차 표지 관리 문제

- 소유권 변동으로 자격이 상실되어도 표지 반납을 강제하기 어렵다.  
- 장애인 등록 취소(사망 등) 시 표지 반납 의무 규정이 불명확한 경우가 있다.

> 🖼️ **[이미지 추가 예정]** 실제 사례 사진  
> “표지 오남용”이나 “자격 상실 후 표지 사용” 같은 사례를 붙이면 설득력이 커진다.

---

### 4) 선행 연구 한계와 본 접근

#### 선행 연구 사례(요약)

선행 연구는 딥러닝 기반 단속 시스템을 제안한다.  
예를 들어, **YOLOv5 객체 인식 모델**로 장애인 주차구역 불법 행위를 감지하고,  
**초음파 센서**로 물체를 확인한 뒤 이미지를 서버로 전송한다.  
이후 **차량 번호판**을 인식해 등록 차량인지 비교하여 위반 여부를 판단한다.

#### 선행 연구의 공통 한계

선행 연구는 주로 **차량 번호 기반 등록 여부**로 위반을 판단한다.  
그러나 번호판·표지 중심 단속은 아래 한계가 남는다.

- 표지 오남용을 구분하기 어렵다.  
- **실제 탑승자(장애인 동승 여부)**를 반영하지 못한다.

#### 본 프로젝트의 접근

이를 보완하기 위해 본 프로젝트는  
장애인 주차구역에 주차된 차량에서  
**하차하는 인원의 보행 특성**을 분석한다.

목표는 아래다.

- 해당 차량에 **보행상 장애 이용자가 실제로 탑승했는지** 추정  
- 이를 **비식별적으로 판단**  

## Gait Classification for Accessible Parking Enforcement

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
