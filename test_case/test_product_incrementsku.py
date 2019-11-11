from tools.api import request_tool


def test_product_incrementSku(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "商品库存模块"  # allure报告中一级分类
    story = '增量调整单个商品库存'  # allure报告中二级分类
    title = "增量调整单个商品库存_全字段正常流_1"  # allure报告中用例名字
    uri = "/product/incrementSku"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    data = {"skuCode":'bbcc_银白色_plus', "qty":20}
    headers={"token": pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,data=data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)



def test_product_getSkuRepertory(pub_data):
    method = "GET"  #请求方法，全部大写
    feature = "商品库存模块"  # allure报告中一级分类
    story = '查询单个库存'  # allure报告中二级分类
    title = "查询单个库存_全字段正常流_1"  # allure报告中用例名字
    uri = "/product/getSkuRepertory"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    params = {"skuCode":'bbcc_银白色_plus'}
    headers={"token":pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,params=params,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)

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
      "skuCode": "bbcc_银白色_plus"
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
















