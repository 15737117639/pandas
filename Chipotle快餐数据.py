import pandas as pd
chipo = pd.read_csv('D:/datas/bigdata/数据/data_analysis/chipotle.csv')
chipo.head()    # 显示数据前几行
chipo.shape[0]  # 显示行数
chipo.shape[1]  # 显示列数
chipo.columns  # 显示所有列标签
# 如何找到被下单最多的商品
# 需要用到分组+聚合（groupby+aggregate)
chipo.groupby('item_name').aggregate({'quantity':'sum'}).max()
# idxmax()返回最大值对应的索引名称。
chipo.groupby('item_name').aggregate({'quantity':'sum'}).idxmax()

# 在item_name这一列中一共有多少种类的商品被下单
# nunique() Return number of unique elements in the object.
chipo['item_name'].nunique()

# 一共有多少个商品被下单
# 直接对'quantity'列进行求和
chipo['quantity'].sum()

# ['order_id', 'quantity', 'item_name', 'choice_description', 'item_price']
# 将'item_price'转化为浮点数
chipo['item_price'] = chipo['item_price'].str[1:].astype(float)

# 在该数据集对应的时期内收入是多少
chipo['revenue'] = chipo['quantity']*chipo['item_price']

# 在该数据集对应的时期内订单有多少个
chipo['order_id'].nunique()

#每一个订单对应的平均总价
chipo['revenue'].sum()/chipo['order_id'].nunique()