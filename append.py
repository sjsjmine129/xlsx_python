from openpyxl import load_workbook

# 기존 엑셀 파일 열기
workbook = load_workbook("output.xlsx")
sheet = workbook.active

# 데이터 추가
sheet.append(["David", 40, "San Francisco"])

# 파일 저장
workbook.save("output.xlsx")
print("데이터 추가 완료!")
