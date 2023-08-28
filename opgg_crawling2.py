import pandas as pd
import re

# 파일 경로 설정
file_path = 'faker.txt'  # 실제 파일 경로로 변경하세요

# 파일을 읽어ㅇ옵니다.
with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

data = [] # 결과를 담을 빈 리스트
current_record = {} # 현재 데이터 레코드
current_title = None

now = 0 # 0일때 시작 1일때 아레나 모드, 2일때 솔랭 모드

for line in lines:
    line = line.strip()
    # 빈 문자열일경우 패스
    if not line:
        continue
    # 아레나 모드일때 조건에 맞는 정보 데이터 레코드에 추가
    if now == 1:
        if line == '승리':
            current_record['승패'] = line
        elif line == '패배':
            current_record['승패'] = line
        elif line == '다시하기':
            current_record['승패'] = line
        elif line.endswith('초'):
            current_record['게임 시간'] = line
        elif re.match(r'^\d+$', line):
            current_record['레벨'] = line
        elif re.search(r'\d+ \/\s*\d+ \/\s*\d+', line):
            current_record['K/D/A'] = line
        elif line.endswith('평점'):
            current_record['평점'] = line[:-2]
        elif line.endswith('킬'):
            current_record['연속킬'] = line
        elif line.startswith('킬관여'):
            current_record['킬관여'] = line[4:]
        elif line.startswith('제어'):
            current_record['제어 와드'] = line[6:]
        elif line.startswith('CS'):
            current_record['CS'] = line[3:]
        elif line == 'iron':
            current_record['평균티어'] = line
        elif line == 'bronze':
            current_record['평균티어'] = line
        elif line == 'silver':
            current_record['평균티어'] = line
        elif line == 'gold':
            current_record['평균티어'] = line
        elif line == 'platinum':
            current_record['평균티어'] = line
        elif line == 'diamond':
            current_record['평균티어'] = line
        elif line == 'master':
            current_record['평균티어'] = line
        elif line == 'grandmaster':
            current_record['평균티어'] = line
        elif line == 'challenger':
            current_record['평균티어'] = line
            
    # 솔랭 모드일때 조건에 맞는 정보 데이터 레코드에 추가
    if now == 2:
        if line == '승리':
            current_record['승패'] = line
        elif line == '패배':
            current_record['승패'] = line
        elif line == '다시하기':
            current_record['승패'] = line
        elif line.endswith('초'):
            current_record['게임 시간'] = line
        elif re.match(r'^\d+$', line):
            current_record['레벨'] = line
        elif re.search(r'\d+ \/\s*\d+ \/\s*\d+', line):
            current_record['K/D/A'] = line
        elif line.endswith('평점'):
            current_record['평점'] = line[:-2]
        elif line.endswith('킬'):
            current_record['연속킬'] = line
        elif line.startswith('킬관여'):
            current_record['킬관여'] = line[4:]
        elif line.startswith('제어'):
            current_record['제어 와드'] = line[6:]
        elif line.startswith('CS'):
            current_record['CS'] = line[3:]
        elif line == 'iron':
            current_record['평균티어'] = line
        elif line == 'bronze':
            current_record['평균티어'] = line
        elif line == 'silver':
            current_record['평균티어'] = line
        elif line == 'gold':
            current_record['평균티어'] = line
        elif line == 'platinum':
            current_record['평균티어'] = line
        elif line == 'diamond':
            current_record['평균티어'] = line
        elif line == 'master':
            current_record['평균티어'] = line
        elif line == 'grandmaster':
            current_record['평균티어'] = line
        elif line == 'challenger':
            current_record['평균티어'] = line

            
        
    
    # '아레나' 또는 '솔랭'이 나올 때마다 새로운 데이터 레코드 시작
    if line == '아레나':
        if now != 0:
            data.append(current_record)
            current_record = {}
        now = 1
        current_title = '아레나'
        current_record = {'타이틀': current_title}
    elif line == '솔랭':
        data.append(current_record)
        current_record = {}
        now = 2
        current_title = '솔랭'
        current_record = {'타이틀': current_title}
        

# 데이터를 DataFrame으로 변환
df = pd.DataFrame(data)

# DataFrame 출력
print(df)
