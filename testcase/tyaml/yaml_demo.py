import yaml

# with open("./data.yml", "r",encoding="utf-8") as f:
#     data = yaml.safe_load(f)
#     print(data)

# with open('./data.yml','r',encoding='utf-8') as f:
    # data = yaml.safe_load_all(f)
    # for i in data:
    #     print(i)
    # data = list(yaml.safe_load_all(f))
    # print(data)


from utils.yamlutil import YamlRead
yr=YamlRead('./data.yml')
data = yr.yaml_read_single() # 读取单个内容
# data = yr.yaml_read_more()  # 读取多段内容
print(data)

