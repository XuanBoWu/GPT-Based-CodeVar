import json
import os

def create_item(result_str, format, model):
    model_str = "格式：" + format + " 模型：" + model
    
    item_str = {
                "type": "default",
                "title": result_str,
                "subtitle": model_str,
                "arg": result_str
            }

    result_item = item_str


    return item_str

def create_items(result_str, model):
    format_list = {
        "snake_case": os.environ.get("snake_case"),
        "upper_camel_case": os.environ.get("upper_camel_case"),
        "camel_case": os.environ.get("camel_case")
    }
    
    
    if not "1" in format_list.values():
        return [{
                "type": "default",
                "title": "没有可用的输出格式",
                "subtitle": "请至少选择一个输出格式",
                "arg": ""
            }]
    
    result_dict = create_format(result_str, {k: v for k, v in format_list.items() if v == "1"}.keys())

    result_items = []
    for format, result in result_dict.items():
        result_items.append(create_item(result, format, model))

    return result_items
    

def create_format(result, format_list):
    # 创建一个字典，将格式化函数作为值，其对应的格式名称作为键
    format_functions = {
        "snake_case": format_snake_case,
        "upper_camel_case": format_upper_camel_case,
        "camel_case": format_camel_case
    }
    
    result_dict = {}
    for format_name in format_list:
        # 检查格式名称是否存在于我们的函数字典中
        if format_name in format_functions:
            # 调用相应的格式化函数，并将结果存储在result_dict中
            formatted_result = format_functions[format_name](result)
            result_dict[format_name] = formatted_result

    return result_dict

def format_preprocessing(result):
    """
    预处理字符串，移除字符串中的非字母和非数字字符，并将其转换为小写。
    :param result: 输入的字符串
    :return: 预处理后的字符串
    """
    
    if "_" in result:
        result = result.replace("_", " ").lower()
    elif " " in result:
        result = str.strip(result).lower()
    else:
        new_result = result[0]
        for i in range(1, len(result)):
            if result[i].isupper():
                if result[i-1].islower() or (i+1 < len(result)) and (result[i+1].islower()):
                    new_result += " "
            new_result += result[i] 
                
        result = new_result.lower()
    
    return result

def format_snake_case(result):
    """
    将字符串转换为蛇形命名（snake_case）。
    :param result: 输入的字符串
    :return: 转换为蛇形命名的字符串
    """
    
    return format_preprocessing(result).replace(" ", "_")

def format_upper_camel_case(result):
    """
    将字符串转换为大驼峰命名（UpperCamelCase）。
    :param result: 输入的字符串
    :return: 转换为大驼峰命名的字符串
    """
    return format_preprocessing(result).title().replace(" ", "")

def format_camel_case(result):
    """
    将字符串转换为小驼峰命名（camelCase）。
    :param result: 输入的字符串
    :return: 转换为小驼峰命名的字符串
    """
    result_list = format_preprocessing(result).title().split()
    result_list[0] = result_list[0][0].lower() + result_list[0][1:]
    return "".join(result_list)

# test
if __name__=="__main__":
    print(format_snake_case("is_Ture"))
