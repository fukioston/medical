import os
import ahocorasick
from py2neo import Graph

from medical.settings import disease_path, department_path, drug_path, food_path, symptom_path, deny_path

g = Graph("http://localhost:7474", auth=("neo4j", "36491491Aa!"),name="mytry")
# 读取5个实体的txt
disease_wds= [i.strip() for i in open(disease_path, encoding='utf-8') if i.strip()]
department_wds= [i.strip() for i in open(department_path, encoding='utf-8') if i.strip()]
drug_wds= [i.strip() for i in open(drug_path, encoding='utf-8') if i.strip()]
food_wds= [i.strip() for i in open(food_path, encoding='utf-8') if i.strip()]
symptom_wds= [i.strip() for i in open(symptom_path, encoding='utf-8') if i.strip()]
deny_words = [i.strip() for i in open(deny_path, encoding='utf-8') if i.strip()]#这个是否定词
region_words = set(department_wds + disease_wds + drug_wds + food_wds+ symptom_wds)
symptom_qwds = ['症状', '表征', '现象', '症候', '表现']
disease_qwds=['病','病情','疾病','病要','恶疾','有病','有什么病']
diagnose_qwds=['辨认','区别','区分','辨认','认出','鉴别']
price_qwds=['价格','价钱','多少','元','人民币','块','钱','售价','单价','市场价','市场价格','成本价格',
            '定价','出售价格','卖价','单价','价']
function_qwds=['作用','功能','效果','功效','药力','药效','疗效','用处']
usage_qwds=['用法','用量','一日','一次','使用剂量','正常用量','一次用量','标准用量','服用量','参考用量'
    ,'药物用量']

side_effect_qwds=['不良反应','副作用','毒副反应','其他不良反应','毒性反应','不良症状','肝肾损害','肝肾毒性','不良反应','不良']
reason_qwds = ['原因','成因', '为什么', '怎么会', '怎样才', '咋样才', '怎样会', '如何会', '为啥', '为何', '如何才会', '怎么才会', '会导致', '会造成']
accompany_qwds = ['并发症', '并发', '一起发生', '一并发生', '一起出现', '一并出现', '一同发生', '一同出现', '伴随发生', '伴随', '共现']
food_qwds = ['饮食', '饮用', '吃', '食', '伙食', '膳食', '喝', '菜' ,'忌口', '补品', '保健品', '食谱', '菜谱', '食用', '食物','补品']
drug_qwds = ['药', '药品', '用药', '胶囊', '口服液', '炎片']
easyget_qwds = ['易感人群', '容易感染', '易发人群', '什么人', '哪些人', '感染', '染上', '得上']
prevention_qwds = ['预防', '防范', '抵制', '抵御', '防止','躲避','逃避','避开','免得','逃开','避开','避掉','躲开','躲掉','绕开',
                             '怎样才能不', '怎么才能不', '咋样才能不','咋才能不', '如何才能不',
                             '怎样才不', '怎么才不', '咋样才不','咋才不', '如何才不',
                             '怎样才可以不', '怎么才可以不', '咋样才可以不', '咋才可以不', '如何可以不',
                             '怎样才可不', '怎么才可不', '咋样才可不', '咋才可不', '如何可不']
treatment_qwds = ['怎么治疗', '如何医治', '怎么医治', '怎么治', '怎么医', '如何治', '医治方式', '疗法', '咋治', '怎么办', '咋办', '咋治']
check_qwds = ['检查', '检查项目', '查出', '检查', '测出', '试出']
belong_qwds = ['属于什么科', '属于', '什么科', '科室']
cure_qwds = ['治疗什么', '治啥', '治疗啥', '医治啥', '治愈啥', '主治啥', '主治什么', '有什么用', '有何用', '用处', '用途',
                          '有什么好处', '有什么益处', '有何益处', '用来', '用来做啥', '用来作甚', '需要', '要']
