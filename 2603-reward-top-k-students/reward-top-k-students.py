from collections import defaultdict
class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        positive_feedback = set(positive_feedback)
        negative_feedback = set(negative_feedback)
        points = defaultdict(int)
        for i,r in enumerate(report):
            for word in r.split(" "):
                if word in positive_feedback:
                    points[student_id[i]]+=3
                elif word in negative_feedback:
                    points[student_id[i]]-=1
                else:
                    points[student_id[i]]+=0
        points = dict(sorted(points.items(), key = lambda x:(-x[1],x[0])))
        res = []
        for key in points.keys():
            res.append(key)
            if len(res)==k:
                break
        
        return res
