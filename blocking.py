# "threading is for working in parallel, and async is for waiting in parallel".
import requests
from time import perf_counter

start = perf_counter()

urls = [
    "https://example.com",
    "https://google.com",
    "https://github.com",
    "https://stackoverflow.com",
    "https://python.org"
]


for url in urls:
    r = requests.get(url)
    print(f"Status Code: {r.status_code}")
    # print(f"Response Content: {r.text}")
    # if r.text:
    #     try:
    #         print(r.json())
    #     except requests.exceptions.JSONDecodeError as e:
    #         print(f"Failed to parse JSON: {e}")
    # else:
    #     print("Response body is empty")

    # print(r.json())

stop = perf_counter()
print("time taken:", stop - start)


# for x in range(1, 2500):
#     r = requests.get(f'http://127.0.0.1:8000/items/{x}')
#     print(r.json())

# stop = perf_counter()
# print("time taken:", stop - start)
# time taken: 58.477935733004415
# time taken: 2.490471332999732