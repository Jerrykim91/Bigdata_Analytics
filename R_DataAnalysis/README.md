
# [R-DataAnalysis](https://trello.com/b/ipqDKD9I/pnu20191216)

```bash
conda install -c anaconda pandas jupyter
conda install -c conda-forge jupyterlab glob2 opencv pytest-shutil tensorflow
pip install tensorflow-addons
```

## R URL

R-Base: <https://cran.rstudio.com>     
R-Studio: <https://rstudio.com/>

## 주피터 노트북 R 커널 설치

```bash

conda install -c anaconda ipython-notebook
conda install -c r r-irkernel

```

## R-base 도커 이미지 실행

```bash

docker pull mrsono0/devremotecontainers:r-base
docker run --rm --name r-base -itd -u vscode -p 8888:8888 -e JUPYTER_RUN=yes -v /c/Users/501_19/PNU_2019/10.R.주요업종별예측모델구축및분석:/home/vscode/notebooks/r mrsono0/devremotecontainers:r-base
docker logs --tail 30 r-base

```

## 도커 이미지 용량 확장 방법
기존 이미지 전체 삭제 돼므로 꼭 백업 후 실행!!!

```bash

docker-machine rm default
docker-machine create --driver virtualbox --virtualbox-cpu-count "2" --virtualbox-memory "2048" --virtualbox-disk-size "50000" default

```

## 주피터 R 커널이 동작하지 않을 경우

아나콘다 언인스톨 권장!!!  
아니면 아래 라이브러리 언인스톨 후 재 설치.  
*conda remove 패키지이름*
환경변수에서 R Path 정보 제일 아래로 이동

```bash

conda install -c anaconda ipython-notebook
conda install -c r r-base=3.5.1
conda install -c r r-recommended=3.5.1
conda install -c r r-irkernel

```