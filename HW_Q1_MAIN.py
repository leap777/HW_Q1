import requests
import pandas as pd
import random
import time as t
import geopandas as gpd
import json
import ast
import matplotlib.pyplot as plt
import  numpy as np
import  math
from matplotlib.ticker import MaxNLocator
from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType
from pyecharts.commons.utils import JsCode
from pyecharts.globals import CurrentConfig

# 在程序初始化时添加

import datetime
from matplotlib.table import Table
from matplotlib.patches import Rectangle
# 定义一级行业分类映射（简化版）
CurrentConfig.extra_coordinates = {
    "鹿港": [120.434, 24.058],
    "台北": [121.565, 25.033],
    # 添加其他需要的城市...
}
primary_industry_map = {
    # 科技与互联网
    '互联网服务': '科技与互联网',
    '特种计算机': '科技与互联网',
    '上网平台': '科技与互联网',
    '网络信息服务': '科技与互联网',
    '信息服务': '科技与互联网',
    '电子商务': '科技与互联网',
    '计算机技术': '科技与互联网',
    '购物网站': '科技与互联网',
    '新零售': '科技与互联网',
    '生活服务平台': '科技与互联网',
    '电商': '科技与互联网',
    '社交媒体': '科技与互联网',
    '游戏': '科技与互联网',
    '网络游戏': '科技与互联网',
    '网游': '科技与互联网',
    '电竞游戏': '科技与互联网',
    '半导体': '科技与互联网',
    '芯片': '科技与互联网',
    'CMOS图像传感器': '科技与互联网',
    '集成电路': '科技与互联网',
    '人工智能': '科技与互联网',
    '智能硬件': '科技与互联网',
    '智能芯片': '科技与互联网',
    '智能家电': '科技与互联网',
    '机器人': '科技与互联网',
'电网自动化': '科技与互联网',
'视频弹幕网站': '科技与互联网',
    '软件': '科技与互联网',
'智能终端操作系统': '科技与互联网',
    'SaaS': '科技与互联网',
    '财税软件': '科技与互联网',
    '金融软件': '科技与互联网','电子': '科技与互联网',
    '信息技术': '科技与互联网',
    '区块链': '科技与互联网','自动驾驶技术': '科技与互联网',
    '虚拟货币交易所': '科技与互联网',
    '数字货币': '科技与互联网',
    '互联网技术':'科技与互联网',
    '网络安全':"科技与互联网",
    '网路安全':"科技与互联网",
    '特种计算机,':'科技与互联网',
    '电信':'科技与互联网',
    '数字新媒体':'科技与互联网','航天':'科技与互联网',
    '声学及多媒体产品':'科技与互联网',  '智能硬件与技术技术':'科技与互联网','通信':'科技与互联网',

    # 制造业
    '家电制造': '制造业',
    '小家电': '制造业',
    '家用电器': '制造业',
    '汽车制造': '制造业',
    '新能源汽车': '制造业',
    '电动车': '制造业',
    '汽车零配件': '制造业',
    '汽车配件': '制造业',
    '电子制造': '制造业',
    '消费电子': '制造业',
    '电子元件': '制造业',
    '电子烟': '制造业',
    '电子部件': '制造业',
    '医疗器械': '制造业',
    '医疗设备': '制造业',
    '医疗机械': '制造业',
    '光伏设备': '制造业',
    '太阳能电池': '制造业',
'卫星导航设备': '制造业',
'汽车服务': '制造业',
'产业园区': '制造业',
'LED': '制造业',
    '锂电池': '制造业',
    '锂电新能源材料': '制造业',
    '电池': '制造业',
    '重型机械': '制造业',
    '工程机械': '制造业',
    '设备制造': '制造业',
    '电子器件制造':'制造业',
    '高压油缸':'制造业',
    '天华超净':'制造业',
    '工业品':'制造业',
    '汽车零部件制造':'制造业',
    '无人机':'制造业','打印设备':'制造业',
    '电器零部件制造':'制造业','电动工具':'制造业','金属结构制造业':'制造业',
   '汽车':'制造业',
   '工业产品':'制造业',
 '电脑产品':'制造业',
  '印染':'制造业','地板':'制造业',
    '橱柜':'制造业','印刷':'制造业',
'厨具':'制造业',
'工业机械': '制造业',
'钛合金': '制造业','制造业': '制造业','空调设备': '制造业','电子配件': '制造业',
'保温容器': '制造业',
'机械制造': '制造业','摩托车': '制造业','机械配件': '制造业',
'压缩机': '制造业',
'热电元件': '制造业',



'精密铸件': '制造业','淋浴设备': '制造业','塑料设备': '制造业','工业电机': '制造业',
'防水材料': '制造业','变压器': '制造业','机械装备制造': '制造业','金属增材制造': '制造业',
'儿童用品连锁': '制造业','文具用品制造': '制造业','石英制品': '制造业','新材料': '制造业',
'环保造纸':'制造业','光纤光缆':'制造业',
'电气设备':'制造业','母婴产品':'制造业','电器机械和器材':'制造业','微波电子器件':'制造业',
'不锈钢':'制造业','生活卫生产品':'制造业','重型工程用车':'制造业','陶瓷材料':'制造业',
'视频监控产品':'制造业','机械':'制造业','生物材料':'制造业','机电设备':'制造业',
'工具制造':'制造业','输配电设备':'制造业','激光设备':'制造业','印刷电路板':'制造业','输送带':'制造业',
'工业设备':'制造业','矿机':'制造业','控制电机':'制造业','床垫':'制造业',
'通信设备':'制造业','珠光材料':'制造业','工业自动化产品':'制造业','制造':'制造业',
'电动自行车':'制造业','电讯':'制造业','五金配件':'制造业','涂料':'制造业','制糖业':'制造业',
'汽车灯具':'制造业','自动化设备':'制造业','印制电路板':'制造业','节能灯':'制造业','耐火材料':'制造业',
'电子通讯产品':'制造业','通信部件':'制造业','电子元器件':'制造业','智能制造':'制造业','铜加工':'制造业','包装':'制造业','造船':'制造业',
'休闲沙发':'制造业','造纸':'制造业','注塑机':'制造业','通讯产品':'制造业','工业制造':'制造业','轮胎':'制造业','工业电器':'制造业','超净产品':'制造业',
    # 房地产与建筑
    '房地产': '房地产与建筑',
    '地产': '房地产与建筑',
    '建筑工程': '房地产与建筑',
    '基础建设': '房地产与建筑','石材': '房地产与建筑',
    '基础设施建设': '房地产与建筑',
    '建筑': '房地产与建筑',
    '装修': '房地产与建筑',
    '装饰': '房地产与建筑',
    '建材家居': '房地产与建筑',
    '家居': '房地产与建筑',
'绿色建材': '房地产与建筑','钢结构产品': '房地产与建筑',
'玻璃': '房地产与建筑','园林': '房地产与建筑',
'路桥': '房地产与建筑','水泥': '房地产与建筑','电梯': '房地产与建筑','锅炉': '房地产与建筑',

    # 金融与投资
    '金融服务': '金融与投资',
'贸易': '金融与投资',
    '金融科技': '金融与投资',
    '银行业': '金融与投资',
    '金融': '金融与投资',
    '投资': '金融与投资',
    '保险': '金融与投资',
'商业连锁': '金融与投资',
'拍卖': '金融与投资',
'商业': '金融与投资',
'信息': '金融与投资','北京': '金融与投资',
    # 医疗健康
    '医药': '医疗健康',
'肿瘤检测': '医疗健康',
    '生物制药': '医疗健康',
    '制药': '医疗健康',
    '生物医药': '医疗健康',
    '生物科技': '医疗健康',
    '医疗服务': '医疗健康', '快速诊断试剂': '医疗健康',
    '医疗保健': '医疗健康',
    '互联网医院': '医疗健康', '原料药': '医疗健康',
    '医院': '医疗健康','基因检测': '医疗健康','医疗大数据': '医疗健康',
'医疗用品': '医疗健康',
    '医械': '医疗健康',
    '疫苗':'医疗健康',
    # 消费品
    '食品饮料': '消费品',
    '饮料': '消费品',
    '白酒': '消费品',
    '乳制品': '消费品',
'保健品': '消费品',
    '服装': '消费品',
    '鞋业': '消费品',
    '纺织': '消费品',
    '服饰': '消费品',
    '日化用品': '消费品',
    '化妆品': '消费品',
    '护肤品': '消费品',
    '日化': '消费品',
    '轻纺': '消费品',
     '羊绒': '消费品',
    '家具': '消费品',
    '家电': '消费品',
    '家装': '消费品',
'个人护理用品': '消费品',
'文具': '消费品',
    '消费品':'消费品',
    '生活用纸': '消费品',
     '插座': '消费品',
    '周大福':'消费品',
    '玩具':'消费品',
'香精香料':'消费品',
'烟草':'消费品','珠宝':'消费品','服饰与配饰':'消费品','个人护理产品':'消费品','服装与配饰':'消费品',
    # 能源与化工
    '能源': '能源与化工',
    '煤炭': '能源与化工',
    '石油化工': '能源与化工',
    '煤化工': '能源与化工',
    '石油': '能源与化工','钨矿': '能源与化工',
    '天然气': '能源与化工',
    '新能源': '能源与化工',
    '太阳能': '能源与化工',
    '合金材料': '能源与化工',
'矿业开发': '能源与化工',
    '光伏': '能源与化工',
    '风电': '能源与化工',
    '充电桩': '能源与化工',
    '化工': '能源与化工','热电': '能源与化工',
    '化纤': '能源与化工',
    '钛白粉': '能源与化工',
    '化学': '能源与化工',
    '钢铁': '能源与化工',
    '有色金属': '能源与化工',
    '铝业': '能源与化工', '金属回收': '能源与化工', '高分子材料': '能源与化工',
    '钼矿': '能源与化工',
    '铜业': '能源与化工',
    '电解铝':'能源与化工',
    '氧化铝':'能源与化工',
    '充电电池':'能源与化工',
    '重化工':'能源与化工',
    '硅材料':'能源与化工','机械电气':'能源与化工',
    '矿业':'能源与化工','塑胶产品':'能源与化工',
    '碳素':'能源与化工','稀散金属':'能源与化工',
    '煤焦':'能源与化工','垃圾发电':'能源与化工','铝合金':'能源与化工','石化':'能源与化工','铁矿石进出口':'能源与化工',
'电力':'能源与化工',
'钒钛磁铁矿':'能源与化工','光学光电':'能源与化工',
'水电':'能源与化工',
'发电厂':'能源与化工',
'电缆':'能源与化工',
'热能电力':'能源与化工',
'电子新材料':'能源与化工',
'橡胶':'能源与化工','锂矿':'能源与化工','矿产':'能源与化工','金矿':'能源与化工',
    '铁矿石与进出口':'能源与化工','煤电':'能源与化工','冶金':'能源与化工','液态气体':'能源与化工',
    # 物流与交通
    '物流': '物流与交通',
    '快递': '物流与交通',
    '运输': '物流与交通',
    '货运': '物流与交通',
    '航空': '物流与交通',
    '航运': '物流与交通',
'供应链': '物流与交通',
    '交通': '物流与交通',
'钢材贸易': '物流与交通',
    '船运': '物流与交通',
    # 农业与食品
    '农业': '农业与食品',
    '畜牧': '农业与食品',
    '饲料': '农业与食品',
    '养殖': '农业与食品',
    '食品': '农业与食品',
    '调味品': '农业与食品','面粉': '农业与食品',
    '乳业': '农业与食品','农药化肥': '农业与食品',
    '农产品': '农业与食品', '香料': '农业与食品',
     '酒业': '农业与食品','保健酒': '农业与食品','种业': '农业与食品','食用油': '农业与食品',
    # 文化娱乐
    '影视娱乐': '文化娱乐',
    '传媒': '文化娱乐',
    '动漫': '文化娱乐',
    '娱乐': '文化娱乐',
'文娱': '文化娱乐',
    '影视': '文化娱乐',
    '收藏': '文化娱乐',
    '手游': '文化娱乐',
    '体育用品': '文化娱乐',
    '体育': '文化娱乐',
    '文化':'文化娱乐',
    # 服务业
    '生活服务': '服务业',
    '餐饮': '服务业',
    '物业管理': '服务业',
    '服务': '服务业',
    '教育': '服务业',
    '旅游': '服务业',
    '零售':'服务业',
    '博彩':'服务业',
'美妆日用品连锁店':'服务业',
    '紫檀博物馆':'服务业','销售':'服务业','污水处理':'服务业','环保':'服务业',
'汽车销售':'服务业',
'杂货':'服务业',
'连锁酒店':'服务业','招聘网站':'服务业','酒店':'服务业','卫星导航':'服务业',
    # 其他
    '多元化': '其他',
    '其他': '其他'
}



def classify_industry(industry_str):
    if pd.isna(industry_str) or industry_str.strip() == "":
        return []

    # 分割复合行业
    industries = []
    for sep in ['、', ',', '，',  ' ']:
        industry_str = industry_str.replace(sep, '|')
    industries = [i.strip() for i in industry_str.split('|') if i.strip()]

    # 分类
    primary_industries = []
    for industry in industries:
        matched = False
        # 尝试完全匹配
        for kw, primary in primary_industry_map.items():
            if industry == kw:
                primary_industries.append(primary)
                matched = True
                break

        # 如果没有匹配到，尝试部分匹配
        if not matched:
            for kw, primary in primary_industry_map.items():
                if kw in industry:
                    primary_industries.append(primary)
                    matched = True
                    break

        # 如果仍然没有匹配到，标记为"其他"
        if not matched:
            primary_industries.append("其他")

    # 去重并返回
    return list(set(primary_industries))

def get_hurun_rich_list():
    all_data = []
    for a in range(1, 7):  # 表单过长，让每页为200，遍历所有页数
        sleep_seconds = random.uniform(1, 3)
        print(f'开始等待{sleep_seconds}秒')
        t.sleep(sleep_seconds)
        print(f'开始爬取第{a}页')

        offset = (a - 1) * 200
        url = f"https://www.hurun.net/zh-CN/Rank/HsRankDetailsList?num=ODBYW2BI&search=&offset={offset}&limit=200"

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Content-Type': 'application/json',
            'Cookie': '__utmz=245691549.1751346291.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); Hm_lvt_2b09927a5895e3946dc6de8526befc81=1751346291,1751420810; HMACCOUNT=DBD136D159063D6E; __utma=245691549.1385465549.1751346291.1751354545.1751420810.4; __utmc=245691549; __utmt=1; __utmb=245691549.5.10.1751420810; Hm_lpvt_2b09927a5895e3946dc6de8526befc81=1751421696'
        }

        try:
            response = requests.get(url, headers=headers, timeout=50)
            if response.status_code == 200:
                json_data = response.json()
                rows = json_data.get('rows', [])

                for item in rows:
                    hs_Character = item.get('hs_Character', [{}])[0] if item.get('hs_Character') else {}
                    all_data.append({
                        '名字': item.get('hs_Rank_Rich_ChaName_Cn', ''),
                        '性别': hs_Character.get('hs_Character_Gender', ''),
                        '年龄': hs_Character.get('hs_Character_Age', ''),
                        'birthplace': hs_Character.get('hs_Character_BirthPlace_Cn', ''),
                        '财富估值(亿人民币)': item.get('hs_Rank_Rich_Wealth_USD', ''),
                        '公司名称': item.get('hs_Rank_Rich_ComName_Cn', ''),
                        '公司位置': item.get('hs_Rank_Rich_ComHeadquarters_Cn', ''),
                        '富豪榜排名': item.get('hs_Rank_Rich_Ranking', ''),
                        '公司类型': item.get('hs_Rank_Rich_Industry_Cn', ''),
                        '财富变化': item.get('hs_Rank_Rich_Wealth_Change', '')
                    })
            else:
                print(f"第{a}页请求失败，状态码: {response.status_code}")
        except Exception as e:
            print(f"第{a}页请求异常: {str(e)}")

    return all_data






def prediect(file_path):
    # 读取CSV文件
    de = pd.read_csv(file_path)

    # 查看财富变化列中的唯一值，以检查是否有非数字内容
    print("原始财富变化数据中的唯一值：", de['财富变化'].unique())

    # 数据清理和转换逻辑
    def clean_percentage(x):
        if isinstance(x, str):
            x = x.replace('%', '')
            if x.upper() == 'NEW':
                return 0.0  # 对于'NEW'，其财富变化百分比视作0%
            try:
                return float(x)
            except ValueError:
                return None  # 如果有其他不可处理的异常值
        return x

    # 应用数据清理函数
    de['财富变化'] = de['财富变化'].apply(clean_percentage)

    # 检查是否有未处理的值并填补空值
    if de['财富变化'].isnull().any():
        print("存在未处理的财富变化数据项，请进一步检查数据源。")
        # 填补空值，一般选择逻辑来填充，比如使用中位数、平均数或0
        de['财富变化'].fillna(0.0, inplace=True)

    # 展开多行业的数据
    expanded_rows = []

    for index, row in de.iterrows():
        industries = ast.literal_eval(row['一级行业'])
        num_industries = len(industries)
        wealth_share = row['财富估值(亿人民币)'] / num_industries

        for industry in industries:
            expanded_row = row.copy()
            expanded_row['一级行业'] = industry.strip()
            expanded_row['财富估值(亿人民币)'] = wealth_share
            expanded_rows.append(expanded_row)

    # 转换为DataFrame
    expanded_df = pd.DataFrame(expanded_rows)

    # 使用每个富豪的财富变化百分比来计算23年的财富值
    expanded_df['23年财富估值(亿人民币)'] = expanded_df['财富估值(亿人民币)'] / (1 + expanded_df['财富变化'] / 100)

    # 按'一级行业'分组，汇总23年和24年的财富值
    grouped_de = expanded_df.groupby('一级行业').agg({
        '23年财富估值(亿人民币)': 'sum',
        '财富估值(亿人民币)': 'sum',
        '名字': 'nunique'
    }).reset_index()

    grouped_de.rename(columns={'名字': '富豪数量'}, inplace=True)

    # 查看分组后的数据
    print(grouped_de)

    # 保存处理后的数据到CSV
    grouped_de.to_csv('processed_file.csv', index=False)

    # 计算增长率
    grouped_de['增长率(%)'] = ((grouped_de['财富估值(亿人民币)'] - grouped_de['23年财富估值(亿人民币)']) / grouped_de[
        '23年财富估值(亿人民币)']) * 100

    # 预测25年行业财富值（线性外推）
    grouped_de['预测25年财富值(亿人民币)'] = grouped_de['财富估值(亿人民币)'] * (1 + grouped_de['增长率(%)'] / 100)

    # 输出结果
    print(grouped_de[
              ['一级行业', '23年财富估值(亿人民币)', '财富估值(亿人民币)', '预测25年财富值(亿人民币)', '增长率(%)']])

    return grouped_de


def load_data(file_path):
    """从CSV文件加载数据并处理"""
    try:
        df = pd.read_csv(file_path)
        print(f"成功加载数据: {len(df)}条记录")
        print("数据列名:", df.columns.tolist())

        # 检查必要的列是否存在
        if 'birthplace' not in df.columns:
            raise ValueError("CSV文件中缺少'birthplace'列")

        return df
    except Exception as e:
        print(f"加载数据失败: {e}")
        exit()


# 2. 处理出生地数据
def process_birthplace_data(df):
    """处理出生地数据，返回城市统计和省份统计"""
    city_counts = {}
    province_counts = {}
    missing_cities = set()

    # 确保数据是字符串类型
    df['birthplace'] = df['birthplace'].astype(str)

    # 处理空值
    df = df[df['birthplace'].notna()]
    df = df[df['birthplace'].str.strip() != '']

    # 打印原始数据的前几条，用于调试
    print("\n原始数据示例:")
    for record in df['birthplace'].head(10):
        print(f"  {record}")

    for record in df['birthplace']:
        try:
            if record in ['nan', 'NaN']:
                continue

            # 处理格式："中国-省-市"
            parts = record.split('-')
            if len(parts) >= 3:
                province = parts[1].strip()
                city = parts[2].strip()

                # 打印处理后的城市名称，用于调试
                print(f"处理城市: {city}")

                # 统计省份数据
                province_counts[province] = province_counts.get(province, 0) + 1

                # 统计城市数据
                city_counts[city] = city_counts.get(city, 0) + 1
            else:
                missing_cities.add(record)
        except Exception as e:
            print(f"处理数据时出错: {record}, 错误: {e}")
            continue

    # 打印数据处理结果
    print("\n最终统计结果:")
    print(f"涉及省份: {len(province_counts)}个")
    print(f"涉及城市: {len(city_counts)}个")

    # 打印所有省份数据
    print("\n省份数据:")
    for province, count in sorted(province_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"  {province}: {count}位富豪")

    # 打印所有城市数据
    print("\n城市数据:")
    for city, count in sorted(city_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"  {city}: {count}位富豪")

    return city_counts, province_counts

def standardize_city_names(city_counts):
    # 创建历史地名到现代地名的映射
    historical_name_map = {
        "沂州": "临沂",  # 山东临沂
        "鹿港": "彰化",  # 台湾彰化县鹿港镇
        "蚌阜": "蚌埠",
        # 添加其他历史地名映射
    }

    standardized_counts = {}
    for city, count in city_counts.items():
        # 使用现代标准地名替换历史地名
        standard_name = historical_name_map.get(city, city)
        standardized_counts[standard_name] = standardized_counts.get(standard_name, 0) + count

    return standardized_counts

def create_heat_map(city_counts, province_counts):
    """创建富豪出生地热力图"""
    geo = Geo(init_opts=opts.InitOpts(
        width="1400px",
        height="800px",
        bg_color="#0f1c2d",
        page_title="中国富豪出生地分布 - 增强视图"
    ))

    # ===== 添加缺失坐标 =====
    # 添加已知城市的精确坐标
    custom_coords = {
        "鹿港": (120.434, 24.058),
        "台北": (121.51, 25.03),
        "高雄": (120.667, 22.633),
        # 其他城市坐标...
        # 在这里添加所有可能的城市坐标
    }



    # ===== 1. 定义自定义坐标 =====
    custom_coords = {

        "杭州": (120.19, 30.26),
        "绍兴": (120.58, 30.02),
        "泉州": (118.58, 24.91),
        "温州": (120.65, 28.03),
        "宁波": (121.56, 29.88),
        "汕头": (116.68, 23.35),
        "无锡": (120.30, 31.59),
        "广州": (113.27, 23.13),
        "梅州": (116.12, 24.29),
        "苏州": (120.62, 31.32),
        "成都": (104.06, 30.67),
        "佛山": (113.11, 23.02),
        "南通": (120.86, 32.00),
        "台州": (121.42, 28.68),
        "长沙": (112.98, 28.23),
        "揭阳": (116.36, 23.55),
        "东莞": (113.75, 23.04),
        "深圳": (114.06, 22.54),
        "武汉": (114.31, 30.60),
        "合肥": (117.28, 31.86),
        "潮州": (116.62, 23.67),
        "南京": (118.78, 32.04),
        "宁德": (119.52, 26.67),
        "新乡": (113.92, 35.32),
        "眉山": (103.85, 30.07),
        "娄底": (112.01, 27.73),
        "福州": (119.30, 26.08),
        "嘉兴": (120.75, 30.75),
        "汕尾": (115.36, 22.78),
        "南昌": (115.89, 28.68),
        "常州": (119.95, 31.79),
        "黄冈": (114.89, 30.45),
        "龙岩": (117.02, 25.10),
        "芜湖": (118.38, 31.34),
        "连云港": (119.16, 34.59),
        "金华": (119.65, 29.09),
        "西安": (108.95, 34.27),
        "鄂尔多斯": (109.78, 39.61),
        "商丘": (115.64, 34.45),
        "昆明": (102.71, 25.04),
        "邢台": (114.50, 37.07),
        "九江": (115.99, 29.71),
        "上饶": (117.95, 28.45),
        "宜春": (114.38, 27.82),
        "益阳": (112.34, 28.57),
        "淮安": (119.15, 33.58),
        "河源": (114.70, 23.74),
        "济南": (117.00, 36.67),
        "荆门": (112.20, 31.04),
        "镇江": (119.44, 32.20),
        "湘潭": (112.94, 27.83),
        "廊坊": (116.70, 39.53),
        "衡水": (115.72, 37.73),
        "沈阳": (123.43, 41.80),
        "黄石": (115.04, 30.22),
        "盐城": (120.13, 33.35),
        "资阳": (104.65, 30.12),
        "泰安": (117.09, 36.19),
        "绵阳": (104.73, 31.47),
        "兰州": (103.83, 36.06),
        "邯郸": (114.47, 36.62),
        "天水": (105.73, 34.58),
        "石家庄": (114.48, 38.04),
        "济宁": (116.59, 35.42),
        "大连": (121.62, 38.92),
        "常德": (111.69, 29.05),
        "安庆": (117.02, 30.53),
        "陇南": (104.93, 33.38),
        "茂名": (110.92, 21.68),
        "中山": (113.39, 22.52),
        "南宁": (108.33, 22.84),
        "岳阳": (113.12, 29.37),
        "湖州": (120.10, 30.88),
        "惠州": (114.41, 23.10),
        "江门": (113.08, 22.59),
        "赣州": (114.92, 25.85),
        "宣城": (118.74, 30.94),
        "长春": (125.35, 43.88),
        "孝感": (113.92, 30.92),
        "邵阳": (111.47, 27.24),
        "聊城": (115.98, 36.45),
        "南阳": (112.53, 33.01),
        "仙桃": (113.40, 30.37),
        "保定": (115.48, 38.87),
        "宿州": (116.98, 33.65),
        "泰州": (120.05, 32.48),
        "阳泉": (113.58, 37.85),
        "宿迁": (118.30, 33.96),
        "烟台": (121.40, 37.52),
        "桂林": (110.28, 25.28),
        "渭南": (109.50, 34.50),
        "蚌埠": (117.38, 32.92),  # 修正拼写错误
        "株洲": (113.13, 27.83),
        "青岛": (120.38, 36.07),
        "湛江": (110.35, 21.27),
        "乌鲁木齐": (87.62, 43.79),
        "襄阳": (112.13, 32.02),
        "许昌": (113.86, 34.03),
        "驻马店": (114.03, 33.01),
        "十堰": (110.78, 32.65),
        "衢州": (118.88, 28.95),
        "乌海": (106.80, 39.67),
        "威海": (122.13, 37.50),
        "韶关": (113.59, 24.84),
        "南平": (118.18, 26.65),
        "黑河": (127.48, 50.25),
        "周口": (114.65, 33.62),
        "衡阳": (112.59, 26.90),
        "邵东": (111.76, 27.27),
        "哈尔滨": (126.65, 45.75),
        "达州": (107.49, 31.22),
        "乐山": (103.78, 29.56),
        "平顶山": (113.30, 33.75),
        "六安": (116.50, 31.75),
        "平江": (113.05, 29.00),
        "海口": (110.35, 20.02),
        "任丘": (116.10, 38.72),
        "定西": (104.63, 35.57),
        "安顺": (105.95, 26.24),
        "庆阳": (107.65, 35.73),
        "包头": (110.00, 40.65),
        "云浮": (112.04, 22.93),
        "辽阳": (123.19, 41.27),
        "雅安": (103.02, 30.35),
        "信阳": (114.07, 32.12),
        "临高": (110.00, 19.92),
        "来宾": (109.23, 23.75),
        "漯河": (114.03, 33.58),
        "巴彦淖尔市": (107.40, 40.75),
        "抚州": (116.36, 27.98),
        "曲靖": (103.80, 25.50),
        "唐山": (118.18, 39.63),
        "锡林郭勒盟": (116.08, 43.93),
        "丽江": (100.23, 26.87),
        "龙南": (115.03, 24.90),
        "扬州": (119.42, 32.39),
        "淄博": (118.04, 36.80),
        "开封": (114.33, 34.80),
        "运城": (111.00, 35.03),
        "郑州": (113.63, 34.76),
        "沂州": (118.32, 35.10),
        "武威": (102.64, 37.93),
        "亳州": (115.78, 33.87),
        "长治": (113.10, 36.20),
        "沅江": (112.35, 28.85),
        "随州": (113.37, 31.38),
        "德阳": (104.39, 31.13),
        "晋中": (112.70, 37.69),
        "巴彦淖尔": (107.40, 40.75),
        "酒泉": (98.51, 39.75),
        "江津": (106.25, 29.28),
        "绥化": (126.98, 46.65),
        "漳州": (117.65, 24.52),
        "咸阳": (108.70, 34.33),
        "莆田": (119.00, 25.43),
        "泰兴": (120.05, 32.18),
        "潍坊": (119.10, 36.70),
        "白城": (122.83, 45.63),
        "惠阳": (114.48, 22.80),
        "铁岭": (123.83, 42.28),
        "东营": (118.50, 37.45),
        "铜陵": (117.80, 30.93),
        "迁安": (118.70, 39.99),
        "阿坝": (102.23, 31.90),

        # 香港澳门
        "香港": (114.17, 22.28),
        "澳门": (113.54, 22.19),

        # 台湾城市
        "台北": (121.51, 25.03),
        "新北": (121.48, 25.05),
        "台中": (120.68, 24.13),
        "台南": (120.20, 23.00),
        "彰化": (120.52, 24.08),
        "桃园": (121.31, 24.99),
        "嘉义": (120.46, 23.47),
        "鹿港": (120.434, 24.058),
        "高雄": (120.667, 22.633),  # 添加台湾高雄
    }

    for city, coord in custom_coords.items():
        geo.add_coordinate(city, coord[0], coord[1])

    geo.add_schema(maptype="china")

    if not city_counts:
        warnings.warn("警告: 没有有效的城市数据！", RuntimeWarning)
        return None

    corrected_city_counts = {}
    typo_correction = {
        "蚌阜": "蚌埠",
        "台北市": "台北",
        "台湾": "台北",
        "台": "台北",
        "港": "香港",
        "彰化县": "彰化",
        "桃园市": "桃园",
    }

    skipped_cities = {}

    for city, count in city_counts.items():
        corrected_city = typo_correction.get(city, city)

        if corrected_city not in custom_coords:
            skipped_cities[corrected_city] = skipped_cities.get(corrected_city, 0) + count
            continue

        corrected_city_counts[corrected_city] = corrected_city_counts.get(corrected_city, 0) + count

    # 检查数据
    if not corrected_city_counts:
        warnings.warn("错误: 修正后无有效城市数据！", RuntimeWarning)
        return None

    # 创建用于热力图的数据
    heat_data = [(city, corrected_city_counts[city]) for city in corrected_city_counts.keys()]

    # 创建用于散点图的数据
    scatter_data = []
    for city, count in corrected_city_counts.items():
        scatter_data.append((
            city,
            {
                "value": count,  # 使用真实值
                "symbolSize": 10,  # 取消对小数据的放大
                "realValue": count  # 存储真实值
            }
        ))

    # 可视化色彩方案
    LOW_VISIBILITY_COLORS = [
        "#ccff66", "#ffff00", "#ffcc00", "#ff9933", "#ff6600", "#ff0000"
    ]

    geo.add(
        series_name="富豪出生地密度",
        data_pair=heat_data,
        type_=ChartType.HEATMAP,
        blur_size=40,
        point_size=35,
        progressive=100,
        effect_opts=opts.EffectOpts(
            is_show=True,
            period=18,
            scale=4,
            brush_type="stroke"
        )
    ).set_global_opts(
        visualmap_opts=opts.VisualMapOpts(
            min_=0,
            max_=max(corrected_city_counts.values()),
            range_text=["密集", "稀疏"],
            orient="vertical",
            pos_left="10px",
            pos_bottom="150px",
            is_piecewise=True,
            range_color=LOW_VISIBILITY_COLORS,
            textstyle_opts=opts.TextStyleOpts(color="#ddd", font_size=12)
        ),
        tooltip_opts=opts.TooltipOpts(
            trigger="item",
            formatter=JsCode(
                "function(params){"
                "  var city = params.name;"
                "  var realVal = typeof params.data.realValue !== 'undefined' ? "
                "               params.data.realValue : params.value;"
                "  var province = '';"
               
                "  if (city in corrected_city_counts) { "
                "      province = city.includes('市') ? city.replace('市', '') : city;"
                "  }"
                "  return '<span style=\"font-size:16px;font-weight:bold\">' + city + '</span><br/>'"
                "       + '富豪数量: <b style=\"color:#ffd700\">' + realVal + '</b><br/>'"
                "       + '省份: <b>' + province + '</b>';"
                "}"
                           ),
             background_color = "rgba(10,20,30,0.9)",
             border_color = "#3a506b",
              textstyle_opts = opts.TextStyleOpts(color="#fff", font_size=14)
    ),
    title_opts = opts.TitleOpts(
        title="中国富豪出生地分布 (增强视图)",
        pos_left="center",
        pos_top="10px",
        title_textstyle_opts=opts.TextStyleOpts(
            color="#fff",
            font_size=24,
            font_weight="bold"
        ),

    )
    )

    # 添加散点图层
    geo.add(
        series_name="数据点",
        data_pair=scatter_data,
        type_=ChartType.SCATTER,
        symbol="circle",
        symbol_size=3,
        effect_opts=opts.EffectOpts(
            is_show=True,
            period=4,
            scale=2.5,
            brush_type="fill",
            color="#ffffff"
        ),
        label_opts=opts.LabelOpts(is_show=True),
        itemstyle_opts=opts.ItemStyleOpts(
            color=JsCode("""
                     function(params) {
                         var value = params.value;
                         return 'rgba(255,0,0,1)';
                     }
                 """),
            opacity=1
        )
    )

    # 打印所有在热力图上出现的城市
    print("\n热力图上出现的城市:")
    for city in corrected_city_counts.keys():
        print(f"  {city}")
    print("修正后城市计数:", corrected_city_counts)
    print("热力图数据:", heat_data)
    return geo

def plot_age_histogram(file_path):
    # 读取CSV文件
    df = pd.read_csv(file_path)

    # 打印原始数据以调试问题所在
    print("原始数据预览:")
    print(df.head())

    # 尝试将“年龄”列转换成数值型
    df['年龄'] = pd.to_numeric(df['年龄'], errors='coerce')

    # 计算无法转换的年龄数目
    unknown_ages_count = df['年龄'].isna().sum()

    # 去掉包含 NaN 的行来清除数据
    df_clean = df.dropna(subset=['年龄'])

    # 打印清理后的数据以调试问题所在
    print("清理后的数据预览:")
    print(df_clean.head())

    # 确保清理后的数据不为空
    if df_clean['年龄'].empty:
        raise ValueError("清理后的年龄数据为空，无法绘制。")

    # 设置支持中文的字体
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
    plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

    # 绘制直方图
    fig, ax = plt.subplots()

    # 计算每个年龄的出现次数
    age_counts = df_clean['年龄'].value_counts().sort_index()

    # 使用 bar 绘图
    age_counts.plot(kind='bar', color='royalblue', edgecolor='black', ax=ax)

    # 设置标题和标签
    plt.title('富豪年龄分布柱状图')
    plt.xlabel('年龄')
    plt.ylabel('富豪数量')

    # 设置 x 轴刻度为整数
    ax.set_xticks(range(len(age_counts)))
    ax.set_xticklabels(age_counts.index)  # 使用实际的年龄值作为标签

    # 确保 x 轴刻度格式为整数
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))

    # 显示包含未知年龄的信息
    plt.text(x=len(age_counts) - 1, y=0,
             s=f'未知年龄: {unknown_ages_count} 人',
             ha='right', va='bottom', fontsize=12, color='red')

    # 显示网格线
    plt.grid(axis='y', alpha=0.75)
    plt.show()


def plot_gender_pie(file_path):
    # 读取CSV文件
    df = pd.read_csv(file_path)

    # 打印原始数据以调试问题所在
    print("原始数据预览:")
    print(df.head())

    # 打印性别列的唯一值
    print("\n原始性别数据:")
    print(df['性别'].value_counts())

    # 将性别数据转换为男/女
    gender_map = {
        '先生': '男',
        '未知': '男',
        '女士': '女'
    }
    df['性别'] = df['性别'].map(gender_map)

    # 统计男女数量
    gender_counts = df['性别'].value_counts()

    # 打印转换后的性别分布
    print("\n转换后的性别分布:")
    print(gender_counts)

    # 设置支持中文的字体
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
    plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

    # 创建饼状图
    fig, ax = plt.subplots()

    # 计算百分比
    total = gender_counts.sum()
    percentages = [(count / total) * 100 for count in gender_counts]

    # 绘制饼状图
    ax.pie(
        gender_counts,
        labels=gender_counts.index,
        autopct=lambda p: f'{p:.1f}%\n({int(p * total / 100)})',
        colors=['royalblue', 'lightcoral'],
        startangle=90,
        textprops={'fontsize': 12}
    )

    # 添加标题
    plt.title('富豪性别分布')

    # 添加图例
    plt.legend(
        title='性别',
        loc='upper right',
        bbox_to_anchor=(1.1, 1),
        fontsize=12
    )

    # 显示图表
    plt.tight_layout()
    plt.show()

# 假设你有一个适当格式的CSV文件


# 主程序
if __name__ == "__main__":
    # 获取数据
    print("开始爬取胡润百富榜数据...")
    rich_list_data = get_hurun_rich_list()
    df = pd.DataFrame(rich_list_data)

    # 行业分类（修改为只使用一级分类）
    print("开始进行行业分类...")
    df['一级行业'] = df['公司类型'].apply(classify_industry)

    # 展开数据（一个人可能对应多个行业）
    df_expanded = df.explode('一级行业').drop_duplicates().reset_index(drop=True)

    # 保存结果
    print("保存结果到文件...")
    df.to_csv('2024胡润百富榜_原始数据.csv', index=False, encoding='utf_8_sig')
    df_expanded.to_csv('2024胡润百富榜_分类数据.csv', index=False, encoding='utf_8_sig')

    # 简单分析（只显示一级行业分布）
    print("\n一级行业分布:")
    print(df_expanded['一级行业'].value_counts())

    print("\n数据处理完成！原始数据保存为：2024胡润百富榜_原始数据.csv")
    print("分类数据保存为：2024胡润百富榜_分类数据.csv")
    file_path = '2024胡润百富榜_原始数据.csv'
    prediect(file_path)
    plot_age_histogram(file_path)
    # 示例使用
   # 请更新为您的实际 CSV 文件路径
    plot_gender_pie(file_path)
    data_file = file_path  # 替换为你的CSV文件路径
    output_file = "china_wealth_birth_heatmap.html"

    # 加载数据
    print("=" * 50)
    print("开始处理富豪出生地数据")
    print("=" * 50)
    df = load_data(data_file)

    # 处理数据
    city_counts, province_counts = process_birthplace_data(df)
    clean_city_counts = standardize_city_names(city_counts)
    geo = create_heat_map(clean_city_counts, province_counts)

    # 创建热力图
    print("\n正在生成热力图...")
    geo = create_heat_map(city_counts, province_counts)

    # 保存结果
    geo.render(output_file)
    print(f"\n热力图已保存至: {output_file}")
    print("请用浏览器打开查看交互式效果")