from firebase import firebase

# init
firebase = firebase.FirebaseApplication('https://vircade-4c1d4.firebaseio.com/', authentication=None)

# test post
# data = {"userId": "gfgthnmhg", "gameID": "safsghth", "ml": [["234","345","425"]]}
# result = firebase.post('/test', data)
# print(result)

# test get
# res = firebase.get('/test', '')
# results = []
# ml = []
# for key in res:
#     results.append({
#         'id': key,
#         'gameID': res[key]['gameID'],
#         'userId': res[key]['userId'],
#         'ml': res[key]['ml'],
#     })
# for i in range(0,len(results)):
#     print(results[i].get('ml'))

class Datasets:
    def get_all(self):
        res = firebase.get('/test', '')
        results = []
        ml = []
        for key in res:
            results.append({
                'id': key,
                'gameID': res[key]['gameID'],
                'userId': res[key]['userId'],
                'ml': res[key]['ml'],
                'song': res[key]['song'],
            })
        return results


datasets = Datasets()
