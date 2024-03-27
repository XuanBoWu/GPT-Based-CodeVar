import json
import os

def create_item(result_str, format, query=""):
    model_str = "格式：" + format + " 模型：" + os.environ.get("model")
    
    item_str = {
                "type": "default",
                "title": result_str,
                "subtitle": model_str,
                "arg": result_str
            }

    result_item = [item_str]


    return result_item

if __name__=="__main__":
    str = create_item("apple")
    print(str)
