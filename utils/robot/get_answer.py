from utils.robot.words import *
def build_actree(wordlist):
    actree = ahocorasick.Automaton()
    for index, word in enumerate(wordlist):#加索引
        actree.add_word(word, (index, word))
    actree.make_automaton()
    return actree
def build_type():
    wd_dict = dict()
    for wd in region_words:#对于每一个实体的name,进行分类
        wd_dict[wd] = []
        if wd in disease_wds:
            wd_dict[wd].append('disease')
        if wd in department_wds:
            wd_dict[wd].append('department')
        if wd in drug_wds:
            wd_dict[wd].append('drug')
        if wd in food_wds:
            wd_dict[wd].append('food')
        if wd in symptom_wds:
            wd_dict[wd].append('symptom')
    return wd_dict
def check_medical(question,region_tree,wdtype_dict):
    # 找一下有没有医学词汇
    region_wds = []
    for i in region_tree.iter(question):#这一步能直接提取数据库中有的关键词
        wd = i[1][1]
        print(wd)
        region_wds.append(wd)
    stop_wds = []
    for wd1 in region_wds:#遍历查看有没有包含的关系，比如说查流行性感冒，感冒也会出来
        for wd2 in region_wds:
            if wd1 in wd2 and wd1 != wd2:
                stop_wds.append(wd1)
    final_wds = [i for i in region_wds if i not in stop_wds]
    final_dict = {i:wdtype_dict.get(i) for i in final_wds}
    return final_dict
def check_keywords( wds, question):
    # 看看有没有匹配到那些问题的关键词
    for wd in wds:
        if wd in question:
            return True
    return False
def classify(question,region_tree,wdtype_dict):
    data = {}
    medical_dict = check_medical(question,region_tree,wdtype_dict)#看看有没有专业名词
    if not medical_dict:#没有医学实体，太遗憾了，根本不知道你想查什么
        return {}
    data['args'] = medical_dict
        #收集问句当中所涉及到的实体类型
    types = []
    for type_ in medical_dict.values():
        types += type_
    question_type = 'others'

    question_types = []

        # 症状
    # 下面是匹配关键词
    #思考会问出什么问题，进行排列组合来分类
    #对疾病来说：疾病症状1，疾病原因1，疾病治疗1，疾病预防1，疾病检查，疾病能吃什么1，疾病不能吃什么1，疾病属于哪个科室1，疾病并发症1，疾病推荐药1,疾病易感人群1
    #对症状来说：症状预防1，症状鉴别1，症状原因1，症状检查1，症状可能是什么病1，症状能吃什么1，症状不能吃什么1，症状属于哪个科室1，症状推荐药1
    #对药品来说：药品价格大概是多少1，药品的作用1，药品的用法1，药品的不良反应1
    # 疾病症状 disease_symptom
    if check_keywords(symptom_qwds, question) and ('disease' in types):
        question_type = 'disease_symptom'
        question_types.append(question_type)
    # 疾病原因  disease_reason
    if check_keywords(reason_qwds, question) and ('disease' in types):
        question_type = 'disease_reason'
        question_types.append(question_type)
    #疾病治疗 disease_treatment
    if check_keywords(treatment_qwds, question) and ('disease' in types):
        question_type = 'disease_treatment'
        question_types.append(question_type)
    # 疾病预防 disease_prevention
    if check_keywords(prevention_qwds, question) and ('disease' in types):
        question_type = 'disease_prevention'
        question_types.append(question_type)
    #疾病能吃什么，不能吃什么
    if check_keywords(food_qwds, question) and 'disease' in types:
        deny_status = check_keywords(deny_words, question)
        if deny_status:
            question_type = 'disease_not_food'
        else:
            question_type = 'disease_do_food'
        question_types.append(question_type)
    #疾病属于哪个科室
    if check_keywords(belong_qwds, question) and ('disease' in types):
        question_type = 'disease_belong'
        question_types.append(question_type)
    #疾病并发症
    if check_keywords(accompany_qwds, question) and ('disease' in types):
        question_type = 'disease_accompany'
        question_types.append(question_type)

        # 症状能吃什么，不能吃什么
        if check_keywords(food_qwds, question) and 'symptom' in types:
            deny_status = check_keywords(deny_words, question)
            if deny_status:
                question_type = 'symptom_not_food'
            else:
                question_type = 'symptom_do_food'
            question_types.append(question_type)

    #疾病该吃什么药
    if check_keywords(drug_qwds, question) and ('disease' in types):
        if 'symptom_do_food' in question_types:
            question_types.remove('symptom_do_food')
        if 'disease_do_food' in question_types:
            question_types.remove('disease_do_food')
        question_type = 'disease_drug'
        question_types.append(question_type)
    #疾病检查
    if check_keywords(check_qwds, question) and ('disease' in types):
        question_type = 'disease_examine'
        question_types.append(question_type)
    # 疾病易感人群 disease_people
    if check_keywords(easyget_qwds, question) and ('disease' in types):
        question_type = 'disease_people'
        question_types.append(question_type)
    # 接下来是症状
    #症状有可能是什么病
    if check_keywords(disease_qwds, question) and ('symptom' in types):
        question_type = 'symptom_disease'
        question_types.append(question_type)
    #症状预防
    if check_keywords(prevention_qwds, question) and ('symptom' in types):
        question_type = 'symptom_prevention'
        question_types.append(question_type)
    #症状原因
    if check_keywords(reason_qwds, question) and ('symptom' in types):
        question_type = 'symptom_reason'
        question_types.append(question_type)
    #症状辨认
    if check_keywords(diagnose_qwds, question) and ('symptom' in types):
        question_type = 'symptom_diagnose'
        question_types.append(question_type)
    #症状检查
    if check_keywords(check_qwds, question) and ('symptom' in types):
        question_type = 'symptom_examine'
        question_types.append(question_type)

    # 症状属于哪个科室
    if check_keywords(belong_qwds, question) and ('symptom' in types):
        question_type = 'symptom_belong'
        question_types.append(question_type)
    # 症状该吃什么药
    if check_keywords(drug_qwds, question) and ('symptom' in types):
        if 'symptom_do_food' in question_types:
            question_types.remove('symptom_do_food')
        if 'disease_do_food' in question_types:
            question_types.remove('disease_do_food')
        question_type = 'symptom_drug'
        question_types.append(question_type)
    #接下来是药品
    #药品治什么病或症状
    if check_keywords(function_qwds+cure_qwds, question) and 'drug' in types:
        question_type = 'drug_function'
        question_types.append(question_type)
    #药品价格
    if check_keywords(price_qwds, question) and 'drug' in types:
        question_type = 'drug_price'
        question_types.append(question_type)
    # 药品用量
    if check_keywords(usage_qwds+food_qwds, question) and 'drug' in types:
        question_type = 'drug_usage'
        question_types.append(question_type)
    #药品副作用
    if check_keywords(side_effect_qwds, question) and 'drug' in types:
        question_type = 'drug_side_effect'
        question_types.append(question_type)
        # 若没有查到相关的外部查询信息，那么则将该疾病的描述信息返回
    if question_types == [] and 'disease' in types:
        question_types = ['disease_introduction']
        # 若没有查到相关的外部查询信息，那么则将该症状的描述信息返回
    if question_types == [] and 'symptom' in types:
        question_types = ['symptom_introduction']
    if question_types == [] and 'drug' in types:
        question_types = ['drug_introduction']
        # 将多个分类结果进行合并处理，组装成一个字典
    data['question_types'] = question_types
    return data
def cql_transfer(question_type, entities):#翻译成cypher语句
    if not entities:
        return []
        # 查询语句
    cql = []
    # 疾病症状 disease_symptom
    if question_type == 'disease_symptom':
        cql = ["MATCH (m:Disease) where m.name = '{0}' return m.name, m.symptom".format(i) for i in entities]

    # 疾病原因  disease_reason
    elif question_type == 'disease_reason':
        cql = ["MATCH (m:Disease) where m.name = '{0}' return m.name, m.reason".format(i) for i in entities]

    # 疾病治疗 disease_treatment
    elif question_type == 'disease_treatment':
        cql = ["MATCH (m:Disease) where m.name = '{0}' return m.name, m.treatment".format(i) for i in entities]

    # 疾病预防 disease_prevention
    elif question_type == 'disease_prevention':
        cql = ["MATCH (m:Disease) where m.name = '{0}' return m.name, m.prevention".format(i) for i in entities]

    # 疾病能吃什么，不能吃什么
    elif question_type == 'disease_not_food':
        cql = ["MATCH  (m:Disease)- [r:AVOID_EAT]->(n:Food) where m.name = '{0}' RETURN m.name,n.name".format(i) for i in entities]

    elif question_type == 'disease_do_food':
        cql = ["MATCH  (m:Disease)- [r:GOOD_EAT]->(n:Food) where m.name = '{0}' RETURN m.name,n.name".format(i) for i in entities]

    # 疾病属于哪个科室
    elif question_type == 'disease_belong':
        cql = ["MATCH  (m:Disease)- [r:BELONGS_TO]->(n:Department) where m.name = '{0}' RETURN m.name,n.name".format(i) for i in entities]

    # 疾病并发症
    elif question_type == 'disease_accompany':
        cql = ["MATCH  (m:Disease)- [r:ACCOMANY]->(n:Disease) where m.name = '{0}' RETURN m.name,n.name".format(i) for i in entities]

    # 疾病该吃什么药
    elif question_type == 'disease_drug':
        cql = ["MATCH  (m:Disease)- [r:RECOMMAND_DRUG]->(n:Drug) where m.name = '{0}' RETURN m.name,n.name".format(i) for i in entities]

    # 疾病检查
    elif question_type == 'disease_examine':
        cql = ["MATCH (m:Disease) where m.name = '{0}' return m.name, m.examine".format(i) for i in entities]

    #疾病易感人群
    elif question_type == 'disease_people':
        cql = ["MATCH (m:Disease) where m.name = '{0}' return m.name, m.easy_person".format(i) for i in entities]

    # 下面是symptom相关

    # 症状有可能是什么病
    elif question_type == 'symptom_disease':
        cql = ["MATCH  (m:Symptom)- [r:MAYBE]->(n:Disease) where m.name = '{0}' RETURN m.name,n.name".format(i)for i in entities]

    # 症状预防
    elif question_type == 'symptom_prevention':
        cql = ["MATCH (m:Symptom) where m.name = '{0}' return m.name, m.prevention".format(i) for i in entities]

    # 症状原因
    elif question_type == 'symptom_reason':
        cql = ["MATCH (m:Symptom) where m.name = '{0}' return m.name, m.reason".format(i) for i in entities]

    # 症状辨认
    elif question_type == 'symptom_diagnose':
        cql = ["MATCH (m:Symptom) where m.name = '{0}' return m.name, m.diagnose".format(i) for i in entities]

    # 症状检查
    elif question_type == 'symptom_examine':
        cql = ["MATCH (m:Disease) where m.name = '{0}' return m.name, m.examine".format(i) for i in entities]

    # 症状能吃什么，不能吃什么
    elif question_type == 'symptom_not_food':
        cql = ["MATCH  (m:Symptom)- [r:AVOID_EAT]->(n:Food) where m.name = '{0}' RETURN m.name,n.name".format(i) for i in entities]

    # 症状属于哪个科室
    elif question_type == 'symptom_belong':
        cql = ["MATCH  (m:Symptom)- [r:BELONGS_TO]->(n:Department) where m.name = '{0}' RETURN m.name,n.name".format(i) for i in entities]

    # 症状该吃什么药
    elif question_type == 'symptom_drug':
        cql = ["MATCH  (m:Symptom)- [r:RECOMMAND_DRUG]->(n:Drug) where m.name = '{0}' RETURN m.name,n.name".format(i) for i in entities]

    # 接下来是药品
    # 药品治什么病或症状
    elif question_type == 'drug_function':
        # 这里考虑一下要不要加联系集的那些病
        cql = ["MATCH (m:Drug) where m.name = '{0}' return m.name, m.function".format(i) for i in entities]

    # 药品价格
    elif question_type == 'drug_price':
        cql = ["MATCH (m:Drug) where m.name = '{0}' return m.name, m.price".format(i) for i in entities]

    # 药品用量
    elif question_type == 'drug_usage':
        cql = ["MATCH (m:Drug) where m.name = '{0}' return m.name, m.usage".format(i) for i in entities]

    # 药品副作用
    elif question_type == 'drug_side_effect':
        cql = ["MATCH (m:Drug) where m.name = '{0}' return m.name, m.side_effect".format(i) for i in entities]

    elif question_type == 'disease_introduction':
        cql = ["MATCH (m:Disease) where m.name = '{0}' return m.name, m.introduction".format(i) for i in entities]

    elif question_type == 'symptom_introduction':
        cql = ["MATCH (m:Symptom) where m.name = '{0}' return m.name, m.introduction".format(i) for i in entities]

    elif question_type == 'drug_introduction':
        cql = ["MATCH (m:Drug) where m.name = '{0}' return m.name, m.function".format(i) for i in entities]


    return cql
def build_entitydict(args):
    entity_dict = {}
    for arg, types in args.items():
        for type in types:
            if type not in entity_dict:
                entity_dict[type] = [arg]
            else:
                entity_dict[type].append(arg)

    return entity_dict
def parser_main( res_classify):
    args = res_classify['args']
    entity_dict = build_entitydict(args)
    question_types = res_classify['question_types']
    print(question_types)
    cqls = []
    for question_type in question_types:
        cql_ = {}
        cql_['question_type'] = question_type
        cql = []
        # 先是disease
        if question_type == 'disease_symptom':
            cql = cql_transfer(question_type, entity_dict.get('disease'))

        elif question_type == 'disease_reason':
            cql = cql_transfer(question_type, entity_dict.get('disease'))

        elif question_type == 'disease_treatment':
            cql = cql_transfer(question_type, entity_dict.get('disease'))

        elif question_type == 'disease_prevention':
            cql = cql_transfer(question_type, entity_dict.get('disease'))

        elif question_type == 'disease_not_food':
            cql = cql_transfer(question_type, entity_dict.get('disease'))

        elif question_type == 'disease_do_food':
            cql = cql_transfer(question_type, entity_dict.get('disease'))

        elif question_type == 'disease_not_food':
            cql = cql_transfer(question_type, entity_dict.get('disease'))

        elif question_type == 'disease_belong':
            cql = cql_transfer(question_type, entity_dict.get('disease'))

        elif question_type == 'disease_accompany':
            cql = cql_transfer(question_type, entity_dict.get('disease'))

        elif question_type == 'disease_drug':
            cql = cql_transfer(question_type, entity_dict.get('disease'))

        elif question_type == 'disease_examine':
            cql = cql_transfer(question_type, entity_dict.get('disease'))

        elif question_type == 'disease_people':
            cql = cql_transfer(question_type, entity_dict.get('disease'))

        # 然后是symptom

        elif question_type == 'symptom_disease':
            cql = cql_transfer(question_type, entity_dict.get('symptom'))

        elif question_type == 'symptom_prevention':
            cql = cql_transfer(question_type, entity_dict.get('symptom'))

        elif question_type == 'symptom_reason':
            cql = cql_transfer(question_type, entity_dict.get('symptom'))

        elif question_type == 'symptom_diagnose':
            cql = cql_transfer(question_type, entity_dict.get('symptom'))

        elif question_type == 'symptom_not_food':
            cql = cql_transfer(question_type, entity_dict.get('symptom'))

        elif question_type == 'symptom_do_food':
            cql = cql_transfer(question_type, entity_dict.get('symptom'))

        elif question_type == 'symptom_belong':
            cql = cql_transfer(question_type, entity_dict.get('symptom'))

        elif question_type == 'symptom_drug':
            cql = cql_transfer(question_type, entity_dict.get('symptom'))

        # 接下来是药品
        elif question_type == 'drug_function':
            cql = cql_transfer(question_type, entity_dict.get('drug'))


        elif question_type == 'drug_price':
            cql = cql_transfer(question_type, entity_dict.get('drug'))

        elif question_type == 'drug_usage':
            cql = cql_transfer(question_type, entity_dict.get('drug'))

        elif question_type == 'drug_side_effect':
            cql = cql_transfer(question_type, entity_dict.get('drug'))

        # 接下来三个散的
        elif question_type == 'disease_introduction':
            cql = cql_transfer(question_type, entity_dict.get('disease'))

        elif question_type == 'symptom_introduction':
            cql = cql_transfer(question_type, entity_dict.get('symptom'))

        elif question_type == 'drug_introduction':
            cql = cql_transfer(question_type, entity_dict.get('drug'))

        if cql:
            cql_['cql'] = cql

            cqls.append(cql_)

    return cqls

    '''针对不同的问题，分开进行处理'''
def answer_prettify(question_type, answers):
    final_answer = []
    num_limit = 20
    if not answers:
        return ''
    if question_type == 'disease_symptom':
        desc = [i['m.symptom'] for i in answers]
        subject = answers[0]['m.name']
        final_answer = '{0}的症状包括：{1}'.format(subject, '；'.join(list(set(desc))[:num_limit]))

    elif question_type == 'disease_reason':
        desc = [i['m.reason'] for i in answers]
        subject = answers[0]['m.name']
        final_answer = '{0}可能的原因为：{1}'.format(subject, '；'.join(list(set(desc))[:num_limit]))

    elif question_type == 'disease_treatment':
        desc = [i['m.treatment'] for i in answers]
        subject = answers[0]['m.name']
        final_answer = '{0}的治疗：{1}'.format(subject, '；'.join(list(set(desc))[:num_limit]))

    elif question_type == 'disease_prevention':
        desc = [i['m.prevention'] for i in answers]
        subject = answers[0]['m.name']
        final_answer = '{0}的预防措施：{1}'.format(subject, '；'.join(list(set(desc))[:num_limit]))

    elif question_type == 'disease_not_food':
        desc = [i['n.name'] for i in answers]
        subject = answers[0]['m.name']
        final_answer = '{0}不建议吃的食物：{1}'.format(subject, '；'.join(list(set(desc))[:num_limit]))

    elif question_type == 'disease_do_food':
        desc = [i['n.name'] for i in answers]
        subject = answers[0]['m.name']
        final_answer = '{0}建议吃的食物：{1}'.format(subject, '；'.join(list(set(desc))[:num_limit]))

    elif question_type == 'disease_belong':
        desc = [i['n.name'] for i in answers]
        subject = answers[0]['m.name']
        final_answer = '{0}属于的科室为：{1}'.format(subject, '；'.join(list(set(desc))[:num_limit]))

    elif question_type == 'disease_accompany':
        desc = [i['n.name'] for i in answers]
        subject = answers[0]['m.name']
        final_answer = '{0}有可能产生的并发症：{1}'.format(subject, '；'.join(list(set(desc))[:num_limit]))

    elif question_type == 'disease_drug':
        desc = [i['n.name'] for i in answers]
        subject = answers[0]['m.name']
        final_answer = '{0}建议服用的药：{1}'.format(subject, '；'.join(list(set(desc))[:num_limit]))

    elif question_type == 'disease_examine':
        desc = [i['m.examine'] for i in answers]
        subject = answers[0]['m.name']
        final_answer = '{0}应做的检查：{1}'.format(subject,  '；'.join(list(set(desc))[:num_limit]))

    elif question_type == 'disease_people':
        desc = [i['m.easy_person'] for i in answers]
        subject = answers[0]['m.name']
        final_answer = '{0}的易感人群：{1}'.format(subject,  '；'.join(list(set(desc))[:num_limit]))

    elif question_type == 'symptom_disease':
        desc = [i['n.name'] for i in answers]
        subject = answers[0]['m.name']
        final_answer = '{0}的可能疾病：{1}'.format(subject,  '；'.join(list(set(desc))[:num_limit]))

    elif question_type == 'symptom_prevention':
        desc = [i['m.prevention'] for i in answers]
        subject = answers[0]['m.name']
        final_answer = '{0}的预防措施：{1}'.format(subject,  '；'.join(list(set(desc))[:num_limit]))

    elif question_type == 'symptom_reason':
        desc = [i['m.reason'] for i in answers]
        subject = answers[0]['m.name']
        final_answer = '产生{0}的原因：{1}'.format(subject,  '；'.join(list(set(desc))[:num_limit]))

    elif question_type == 'symptom_diagnose':
        desc = [i['m.diagnose'] for i in answers]
        subject = answers[0]['m.name']
        final_answer = '{0}的鉴别：{1}'.format(subject,  '；'.join(list(set(desc))[:num_limit]))

    elif question_type == 'symptom_examine':
        desc = [i['m.examine'] for i in answers]
        subject = answers[0]['m.name']
        final_answer = '{0}的检查：{1}'.format(subject,  '；'.join(list(set(desc))[:num_limit]))

    elif question_type == 'symptom_not_food':
        desc = [i['n.name'] for i in answers]
        subject = answers[0]['m.name']
        final_answer = '{0}不能吃的食物：{1}'.format(subject,  '；'.join(list(set(desc))[:num_limit]))

    elif question_type == 'symptom_do_food':
        desc = [i['n.name'] for i in answers]
        subject = answers[0]['m.name']
        final_answer = '{0}建议吃的食物：{1}'.format(subject,  '；'.join(list(set(desc))[:num_limit]))

    elif question_type == 'symptom_belong':
        desc = [i['n.name'] for i in answers]
        subject = answers[0]['m.name']
        final_answer = '{0}属于的科室：{1}'.format(subject,  '；'.join(list(set(desc))[:num_limit]))

    elif question_type == 'symptom_drug':
        desc = [i['n.name'] for i in answers]
        subject = answers[0]['m.name']
        final_answer = '{0}建议服用的药：{1}'.format(subject,  '；'.join(list(set(desc))[:num_limit]))

    elif question_type == 'drug_function':
        desc = [i['m.function'] for i in answers]
        subject = answers[0]['m.name']
        final_answer = '{0}的功能有：{1}'.format(subject,  '；'.join(list(set(desc))[:num_limit]))

    elif question_type == 'drug_price':
        desc = [i['m.price'] for i in answers]
        subject = answers[0]['m.name']
        final_answer = '{0}的价格大概是：{1}'.format(subject,  '；'.join(list(set(desc))[:num_limit]))

    elif question_type == 'drug_usage':
        desc = [i['m.usage'] for i in answers]
        subject = answers[0]['m.name']
        final_answer = '{0}的用量：{1}'.format(subject,  '；'.join(list(set(desc))[:num_limit]))

    elif question_type == 'drug_side_effect':
        desc = [i['m.side_effect'] for i in answers]
        subject = answers[0]['m.name']
        final_answer = '{0}的副作用以及注意事项：{1}'.format(subject, '；'.join(list(set(desc))[:num_limit]))

    elif question_type == 'disease_introduction':
        desc = [i['m.introduction'] for i in answers]
        subject = answers[0]['m.name']
        final_answer = '{0}的介绍：{1}'.format(subject, '；'.join(list(set(desc))[:num_limit]))

    elif question_type == 'symptom_introduction':
        desc = [i['m.introduction'] for i in answers]
        subject = answers[0]['m.name']
        final_answer = '{0}的介绍：{1}'.format(subject, '；'.join(list(set(desc))[:num_limit]))

    elif question_type == 'drug_introduction':
        desc = [i['m.function'] for i in answers]
        subject = answers[0]['m.name']
        final_answer = '{0}的介绍：{1}'.format(subject, '；'.join(list(set(desc))[:num_limit]))

    return final_answer
def search_main(cqls):
    final_answers = []
    for cql_ in cqls:
        question_type = cql_['question_type']
        queries = cql_['cql']
        answers = []
        for query in queries:
            ress = g.run(query).data()
            answers += ress
        final_answer = answer_prettify(question_type, answers)
        if final_answer:
            final_answers.append(final_answer)
    return final_answers

region_tree = build_actree(list(region_words))
# 给他直接一一对应关键词的类型
wdtype_dict = build_type()
# while(True):
#     question = input('请输入')
#     print(classify(question,region_tree,wdtype_dict))
#     print(parser_main(classify(question,region_tree,wdtype_dict)))
#     print(search_main(parser_main(classify(question,region_tree,wdtype_dict))))
# print(check_medical(question,region_tree,wdtype_dict))