from fastapi import FastAPI, Query

app = FastAPI(title='Rimart health')

EXERCISES = [
  { 'id': 1, 'title': 'Remo con mancuerna', 'category': 'espalda' },
  { 'id': 2, 'title': 'Press con barra', 'category': 'pecho' },
  { 'id': 3, 'title': 'Copa con mancuerna', 'category': 'triceps' }
]

@app.get('/')
def home():
  return {
    'message': 'Bienvenidos a rimart health por Isaac Martinez'
  }

@app.get('/exercises')
def get_exercises():
  return {
    'data': EXERCISES
  }
  
@app.get('/exercise')
def get_exercise(query: str | None = Query(default=None, description='Texto para buscar por titulo')):
  if query:
    results = []
    # for exercise in EXERCISES:
    #   if query.lower() in exercise['title'].lower():
    #     results.append(exercise)
        
    # list comprehension
    results = [ exercise for exercise in EXERCISES if query.lower() in exercise['title'].lower() ]
    return {
      'data': results,
      'query': query
    }
  return {
    'data': EXERCISES,
    'query': query
  }