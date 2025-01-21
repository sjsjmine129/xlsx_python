import pandas as pd

# 엑셀 파일 읽기
df = pd.read_excel("output.xlsx")  # "example.xlsx" 파일을 읽음
print(df.head())  # 데이터프레임의 상위 5개 행 출력

df = pd.read_excel("output.xlsx", sheet_name="Sheet2") # "Sheet2" 시트를 읽음
print(df)



# "번호"와 "형식"이 동일한 행을 그룹화하고 "모델" 열 병합
result = (
    df.groupby(["번호", "형식"], as_index=False)
    .agg({"모델": lambda x: ", ".join(x)})
)

# 결과 저장
result.to_excel("merged_data.xlsx", index=False)