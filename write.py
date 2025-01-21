import pandas as pd

# 데이터프레임 생성
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}

df = pd.DataFrame(data)

# 엑셀 파일로 저장
df.to_excel("output.xlsx", index=False)  # index=False로 행 번호 저장 안 함
print("엑셀 파일로 저장 완료!")
