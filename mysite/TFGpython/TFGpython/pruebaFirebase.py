from firebase import Firebase
f = Firebase('https://tfgsrkapi.firebaseio.com/data')

r = f.push({'user_id': 'wilma', 'text': 'Hello'})
print r



