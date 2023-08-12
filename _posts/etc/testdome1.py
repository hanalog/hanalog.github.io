
# 병원에서 대기 중인 펫들 추적에 사용
# 시간에 있어서 효율적이어야 함
# accept() : 줄 끝점에 펫 놓기
# heal() : 줄 시작점의 펫 제거 후 반환, 없으면 IndexError 예외

from collections import deque

class Veterinarian:
	def __init__(self):
		self.names = deque()

	def accept(self, Name):
		self.names.append(Name)

	def heal(self):
		if not self.names:
			raise IndexError("No pets waiting")
		return self.names.popleft()

if __name__ == "__main__":
    v1 = Veterinarian()
    v1.accept("Barkley")
    v1.accept("Mittens")
    print(v1.heal())
    v2 = Veterinarian()
    v2.accept('c')
    v2.accept(1)
    print(v2.heal())
    print(v2.heal())
    print(v2.heal())


"""
import json

# json 문자열 > python 객체
json_str = '''{}'''
json_obj = json.loads(json_str)

# json 파일 > python 객체
with open('path.json') as f:
    json_obj = json.load(f)

# python 객체 > json 문자열
json_str = json.dumps(json_obj, indent=2)

# python 객체 > json 파일
with open('path.json', 'w') as f:
    json.dump(json_obj, f, indent=2)
"""

"""
/*
출처 : 
조회
- name : 모든 지역 이름
- average : 평균판매 (지역별 판매량/지역별 고용인)
- difference : 평균판매 차이 (가장 높은 지역의 평균 판매 - 해당 지역의 평균 판매)
*/

WITH avgs AS (
	SELECT A.name, IFNULL(ROUND(SUM(d.amount)/COUNT(*)), 0) as average
	FROM regions AS a
		LEFT JOIN states AS b
		ON a.id = b.regionID
		LEFT JOIN employees AS c
		ON b.id = c.stateID
		LEFT JOIN sales AS d
		ON c.id = d.employeeID
	GROUP BY a.name
)

SELECT name, average, (max_average - average) AS difference
FROM (
	SELECT name, average, MAX(average) OVER() AS max_average
    FROM avgs
) AS avgs_max;
"""