
# n번째로 가장 낮은 판매책 id를 찾아라
# sales의 각 요소는 나타낸다 책의 ID를 가진 책의 단일 판매
# 책 판매량에 중복은 없음
from collections import defaultdict
import time
def nth_lowest_selling_1(sales, n):
    """
    :param elements: (list) List of book sales.
    :param n: (int) The n-th lowest selling element the function should return.
    :returns: (int) The n-th lowest selling book id in the book sales list.
    """
    # Use dictionary to save id and sales
    sales_cnt = dict()
    for s in sales:
        if not sales_cnt.get(s):
            sales_cnt[s] = 1
        else:
            sales_cnt[s] += 1
    # Sort by sales
    sales_cnt = sorted(sales_cnt.items(), key=lambda x: x[1])
    # Return the id of nth lowest selling book
    return sales_cnt[n-1][0]

def nth_lowest_selling_2(sales, n):
    """
    :param elements: (list) List of book sales.
    :param n: (int) The n-th lowest selling element the function should return.
    :returns: (int) The n-th lowest selling book id in the book sales list.
    """
    sales_cnt = defaultdict(int)
    for s in sales:
        print(sales_cnt[s])
        sales_cnt[s] += 1
    sales_cnt = sorted(sales_cnt.items(), key=lambda x: x[1])
    return sales_cnt[n-1][0]


if __name__ == "__main__":
    test = [5, 4, 3, 2, 1, 5, 4, 3, 2, 5, 4, 3, 5, 4, 5, 4, 4]
    a1 = time.time()
    print(nth_lowest_selling_1(test, 2))
    a2 = time.time()
    print(nth_lowest_selling_2(test, 2))
    a3 = time.time()
    print(a2-a1, a3-a2)


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