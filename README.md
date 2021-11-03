# cuai
CUAI -cau machine&amp;deep learning circle

## CUAI 하계 컨퍼런스

webtoon-recommendation
콘텐츠의 특성과 사용자의 선호도를 고려한 웹툰 추천 시스템

### 1. data

all-webtoons.csv: 제목, 장르, 스토리, 썸네일 등 크롤링

네이버 웹툰 (21.07.22 기준)

다음 웹툰 (21.07.25 기준)

카카오 페이지 (21.08.13 기준)

레진코믹스 (21.08.14 기준)

선호도.csv: 구글 Forms를 이용해 선호장르와 취향에 맞는 웹툰, 취향에 맞지 않는 웹툰 조사

104 개의 응답, 303 개의 웹툰

### 2. src

#### 콘텐츠 기반 추천 시스템

스토리 기반 추천: 스토리에서 textrank로 추출한 키워드와 코사인 유사도를 이용하여 웹툰간 유사도 출력

그림체 기반 추천: 미리 학습된 CNN 네트워크를 이용해 썸네일의 feature 추출 후 비교

#### 협업 필터링

아이템 기반 추천: 각 아이템에 대한 사용자들의 선호도를 기반으로 유사도를 계산해 추천 진행

잠재요인 기반 추천: 행렬분해와 잠재요인으로 인한 사용자 선호 웹툰 예측

## IMC 3월

노트북 가격을 예측하는 동아리 내 공모전

### Determine the Problem

There are 1260 given data sets. With these sets, we need to predict the price of laptop.

From this machine learning, we will make a model that solves this question 

: "A laptop with these specifications, how much will this be?"

Ridge, Lasso Model Used

## Kaggle Dacon Study

Commonly Known : Titanic and Voting

## Pytorch Study

### Deep Learning Zero To ALL : Pytorch

Official Github: https://github.com/deeplearningzerotoall/PyTorch

Official YouTube: http://bit.ly/2UVk3kn

Official Slide: http://bit.ly/2VrZcWM

### Index

#### PART 1: Machine Learning & PyTorch Basic

Lab-01-1 Tensor Manipulation 1

Lab-01-2 Tensor Manipulation 2

Lab-02 Linear regression

Lab-03 Deeper Look at GD

Lab-04-1 Multivariable Linear regression

Lab-04-2 Loading Data

Lab-05 Logistic Regression

Lab-06 Softmax Classification

Lab-07-1 Tips

Lab-07-2 MNIST Introduction


#### PART 2: Neural Network

Lab-08-1 Perceptron

Lab-08-2 Multi Layer Perceptron

Lab-09-1 ReLU

Lab-09-2 Weight initialization

Lab-09-3 Dropout

Lab-09-4 Batch Normalization


#### PART 3: Convolutional Neural Network

Lab-10-0 Convolution Neural Networkintro

Lab-10-1 Convolution

Lab-10-2 mnist cnn

Lab-10-3 visdom

Lab-10-4-1 ImageFolder1

Lab-10-4-2 ImageFolder2

Lab-10-5 Advance CNN(VGG)

Lab-10-6-1 Advanced CNN(RESNET-1)

Lab-10-6-2 Advanced CNN(RESNET-2)

Lab-10-7 Next step of CNN


#### PART 4: Recurrent Neural Network

Lab-11-0 RNN intro

Lab-11-1 RNN basics

Lab-11-2 RNN hihello and charseq

Lab-11-3 Long sequence

Lab-11-4 RNN timeseries

Lab-11-5 RNN seq2seq

Lab-11-6 PackedSequence



## 전주시 빅데이터 공모전

전주시 공용 자전거 꽃싱이의 이용률을 높이기 위해 적합한 대여소 위치를 제안

### 1. data 

(버스정책과)버스이용자 수.xlsx

2019_2021년 대여현황.xlsx

ffffinal_data.csv

유동인구.xlsx

자전거.hwp

자전거도로유무.xlsx

전국사업체조사_2_산업소분류 및 읍면동별 사업체수, 종사자수.xlsx

전주_202007_202012_행정동별집계.xlsx

전주시_동별인구_1.xlsx

20년말연령별인구통계_전주시.xlsx

20년말인구 및 세대현황_전주시.xlsx

21년4월말연령별인구통계_전주시.xlsx

21년4월말인구 및 세대현황_전주시.xlsx
