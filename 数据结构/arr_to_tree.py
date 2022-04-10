# 扁平数组转换成树形结构
# exampl: [{"id": 1, "pid": '0'}, {"id": 11, "pid": '1'}, {"id": 12, "pid": '1'}, {"id": 21, "pid": '12'}]
from typing import List
import json


def arr_to_tree(arr: List) -> List:
    root_id = 0
    result = []
    m = {}
    for i in range(len(arr)):
        arr[i]["children"] = []
        m[arr[i]["id"]] = arr[i]

    for i in range(len(arr)):
        node = arr[i]
        if int(node["pid"]) != root_id:
            m[int(node["pid"])]["children"].append(node)
        else:
            result.append(node)

    return result


if __name__ == "__main__":
    arr = [{"id": 1, "pid": '0'}, {"id": 11, "pid": '1'}, {"id": 12, "pid": '1'}, {"id": 21, "pid": '12'}]
    result = arr_to_tree(arr)
    print(json.dumps(result, indent=4))

# [
#     {
#         "id": 1,
#         "pid": "0",
#         "children": [
#             {
#                 "id": 11,
#                 "pid": "1",
#                 "children": []
#             },
#             {
#                 "id": 12,
#                 "pid": "1",
#                 "children": [
#                     {
#                         "id": 21,
#                         "pid": "12",
#                         "children": []
#                     }
#                 ]
#             }
#         ]
#     }
# ]
