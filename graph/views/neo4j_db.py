from py2neo import Graph, Node, Relationship


class neo4jconn:
    def __init__(self):
        self.graph = Graph("http://localhost:7474", auth=("neo4j", "36491491Aa!"), name="mytry")

    # 已知实体1，找他的所有关系
    def findRelationByEntity1(self, entity1):
        answer = self.graph.run("MATCH (n1 {name:\"" + entity1 + "\"})- [rel] -> (n2) RETURN n1,rel,n2,TYPE(rel) AS relationshipName LIMIT 25").data()
        return answer

    # 已知实体1和关系
    def findOtherEntities(self, entity1, relation):
        answer = self.graph.run(
            "MATCH (n1 {name:\"" + entity1 + "\"})-[rel:" + relation + "]->(n2) RETURN n1,rel,n2,TYPE(rel) AS relationshipName LIMIT 25").data()
        return answer

    # 查询整个知识图谱体系(限制为25)
    def knowledgeGraph(self):
        answer = self.graph.run("MATCH (n1)- [rel] -> (n2) RETURN n1,rel,n2 ,TYPE(rel) AS relationshipName ORDER BY RAND() LIMIT 25").data()
        return answer

    # 已知实体2查询
    def findRelationByEntity2(self, entity2):
        answer = self.graph.run("MATCH (n1)- [rel] -> (n2:major {name:\"" + entity2 + "\"}) RETURN n1,rel,n2,TYPE(rel) AS relationshipName LIMIT 25").data()
        if (len(answer) == 0):
            answer = self.graph.run(
                "MATCH (n1)- [rel] -> (n2{name:\"" + entity2 + "\"}) RETURN n1,rel,n2,TYPE(rel) AS relationshipName LIMIT 25").data()
            if (len(answer) == 0):
                answer = self.graph.run(
                    "MATCH (n1)- [rel] -> (n2{name:\"" + entity2 + "\"}) RETURN n1,rel,n2,TYPE(rel) AS relationshipName LIMIT 25").data()
        return answer

    def findOtherEntities2(self, entity2, relation):
        answer = self.graph.run(
            "MATCH (n1)- [rel:" + relation + "] -> (n2{name:\"" + entity2 + "\"}) RETURN n1,rel,n2,TYPE(rel) AS relationshipName LIMIT 25").data()
        if (len(answer) == 0):
            answer = self.graph.run(
                "MATCH (n1)- [rel:" + relation + "] -> (n2{name:\"" + entity2 + "\"}) RETURN n1,rel,n2,TYPE(rel) AS relationshipName LIMIT 25").data()
            if (len(answer) == 0):
                answer = self.graph.run(
                    "MATCH (n1)- [rel:" + relation + "] -> (n2{name:\"" + entity2 + "\"}) RETURN n1,rel,n2,TYPE(rel) AS relationshipName LIMIT 25").data()
        return answer

    def findEntities1AndEntities2(self, entity1, entity2, relation):
        answer = self.graph.run(
            "MATCH (n1{name:\"" + entity1 + "\"})-[rel:" + relation + "]->(n2 {name:\"" + entity2 + "\"}) RETURN n1,rel,n2,TYPE(rel) AS relationshipName LIMIT 25").data()
        return answer

