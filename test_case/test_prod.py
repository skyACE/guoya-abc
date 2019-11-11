from tools.api import request_tool
from tools.security.md5_tool import md5_passwd

'''
自动生成 数字 20,80   #生成20到80之间的数字 例：56
自动生成 字符串 5 中文数字字母特殊字符 xuepl        #生成以xuepl开头加上长度2到5位包含中文数字字母特殊字符的字符串，例子：xuepl我1
自动生成 地址
自动生成 姓名
自动生成 手机号
自动生成 邮箱
自动生成 身份证号
'''

def test_add_prod(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "商品模块"  # allure报告中一级分类
    story = '商品'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/addProd"  # 接口地址
    headers = {"token": pub_data["token"]}
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
  {
  "brand": "耐克c",
  "colors": [
    "银白色","粉白色","种红色","土豪金"
  ],
  "price": 5012,
  "productCode": "自动生成 字符串 6 数字字母  ",
  "productName": "耐克abc",
  "sizes": [
    "plus"
  ],
  "type": "手机"
}
    '''
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    #json_path=[{"skuCode":'$.data[0].skuCode'}]
    # json path，参数类型为列表 根据jsonpath提取响应正文中的数据
    json_path = [{"skuCode": '$.data[0].skuCode'}]
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(json_path=json_path,headers=headers,method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)

   # pub_data["skuCode"] = r.json()["data"][0]["skuCode"]


def test_change_price(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "商品模块"  # allure报告中一级分类
    story = '修改商品金额'  # allure报告中二级分类
    title = "_全字段正常流_1"  # allure报告中用例名字
    uri = "/product/changePrice"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    data = {"SKU":pub_data["skuCode"],"price":8888}
    headers = {"token": pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,data=data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)



def test_product_incrementSku(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "商品库存模块"  # allure报告中一级分类
    story = '增量调整单个商品库存'  # allure报告中二级分类
    title = "增量调整单个商品库存_全字段正常流_1"  # allure报告中用例名字
    uri = "/product/incrementSku"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    data = {"skuCode":pub_data["skuCode"], "qty":20}
    headers={"token": pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,data=data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)



def test_order_addOrder(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "订单模块"  # allure报告中一级分类
    story = '无秘下单'  # allure报告中二级分类
    title = "无秘下单_全字段正常流_1"  # allure报告中用例名字
    uri = "/order/addOrder"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    headers={"token":pub_data["token"]}
    json_data = '''
   {
  "ordeerPrice": 5012,
  "orderLineList": [
    {
      "qty": 1,
      "skuCode":"${skuCode}"
    }
  ],
  "receiver": "str55585",
  "receiverPhone": "13681662512",
  "receivingAddress": "上海浦东新区11路",
   "sign": "",
  "userName": "str55585"
}
    '''
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(headers=headers,method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)






def test_order_addOrder_sign(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "订单模块"  # allure报告中一级分类
    story = '无秘下单'  # allure报告中二级分类
    title = "无秘下单_全字段正常流_1"  # allure报告中用例名字
    uri = "/order/addOrderSignBody"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    headers={"token":pub_data["token"]}
    s="receiver=str55585&ordeerPrice=5012&receiverPhone=13681662512&key=guoya"
    sign=md5_passwd(s,key="")
    pub_data["sign"]=sign
    json_data = '''
   {
  "ordeerPrice": 5012,
  "orderLineList": [
    {
      "qty": 1,
      "skuCode":"${skuCode}"
    }
  ],
  "receiver": "str55585",
  "receiverPhone": "13681662512",
  "receivingAddress": "上海浦东新区11路",
   "sign": " pub_data["sign"]",
  "userName": "str55585"
}
    '''
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(headers=headers,method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)

