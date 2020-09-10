### migrate 실행시키기

1. [app 명]/models.py에서 모델을 변경한다.

2. 변경사항에 대한 migrations를 만든다.

   python manage.py makemigrations

3. 변경사항을 데이터베이스에 적용한다.

   python manage.py migrate

### 가상환경 저장 및 공유

1. 가상환경 export

   conda env export > [파일이름].yaml

2. 공유받은 yaml 파일로부터 가상환경 생성

   conda env create -f [파일이름].yaml

3. 가상환경 목록 확인

   conda env list

4. 가상환경 제거하기

   conda env remove -n [가상환경 명]

### AWS Anaconda 설치하기

1. 아나콘다에서 리눅스버전으로 설치

2. install anaconda

   ```
   bash ~/anaconda.sh -b -p $HOME/anaconda
   ```

3. update anaconda path

   ```
   echo -e '\nexport PATH=$HOME/anaconda/bin:$PATH' >> $HOME/.bashrc && source $HOME/.bashrc
   ```

4. 혹시 conda를 입력하면 menu들이 나와야 하는데 정상적으로 $PATH등록이 안되었다면, PATH를 export를 해준다.

   ```
   export PATH=~/anaconda3/bin:$PATH
   ```

### AWS 시작하기

1. ssh -i cert.pem ubuntu@j3b105.p.ssafy.io

2. 가상환경 만들기

   conda create -n [가상환경 명] python=3.7

3. 가상환경 실행하기 (만약 root이면 ubuntu로 바꿔야된다. su - ubuntu)

   source activate [가상환경 명]

4. Django Server 실행하기

   python manage.py  runserver 0:8080

5. pip3 install -r requirements.txt

6. 가상환경 종료하기

   source deactivate [가상환경 명]

### Django Server 시작하기





#### 가상환경에 install

conda install -c anaconda mysql

conda install -c bioconda mysqlclient