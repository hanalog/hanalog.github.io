
def pipeline(*funcs):
    def helper(arg):
        for func in funcs:
            arg = func(arg)
        return arg
    return helper
            
fun = pipeline(lambda x: x * 3, lambda x: x + 1, lambda x: x / 2)
print(fun(3)) #should print 5.0


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