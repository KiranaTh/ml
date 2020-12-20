from firebase import firebase

# init
firebase = firebase.FirebaseApplication('https://vircade-4c1d4.firebaseio.com/', authentication=None)

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

    def update(self, gameID, userId, score):
        res = firebase.put('/games/'+gameID+'/'+userId, 'score', score)
        result = '/games/'+gameID+'/'+userId
        return result


datasets = Datasets()



