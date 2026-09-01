from fastapi import Body, FastAPI, Query, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI(title='Rimart health')

EXERCISES = [
  { 'id': 1, 'title': 'Remo con mancuerna', 'category': 'espalda' },
  { 'id': 2, 'title': 'Press con barra', 'category': 'pecho' },
  { 'id': 3, 'title': 'Copa con mancuerna', 'category': 'triceps' }
]

class BaseExercise(BaseModel):
  title: str
  category: Optional[str] = "Sin categoria" # Si se pone None el valor por defecto quedaria como null

class ExerciseCreate(BaseModel):
  title: str = Field(
    ...,
    min_length=3,
    max_length=100,
    description="Titulo del ejercicio (minimo 3 caracteres y maximo 100)",
    examples=[
      "Curl con mancuernas",
      "Sentadilla hack"
    ]
  )
  category: Optional[str] = Field(
    default="Sin categoria",
    min_length=3,
    description="Categoria del ejercicio (minimo 3 caracteres)",
    examples=["Pecho", "Espalda", "Biceps", "Triceps"]
  )

class ExerciseUpdate(BaseModel):
  title: str
  category: Optional[str] = None # Si se pone None se guardara el valor anterior

@app.get('/')
def home():
  return {
    'message': 'Bienvenidos a rimart health por Isaac Martinez'
  }

@app.get('/exercises')
def get_exercise(query: str | None = Query(default=None, description='Texto para buscar por titulo')):
  if query:
    results = []
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

@app.get('/exercises/{exercise_id}')
def get_exercise_by_id(exercise_id: int, include_category: bool = Query(default=True, description='Incluir o no la categoria')):
  for exercise in EXERCISES:
    if exercise['id'] == exercise_id:
      id = exercise['id']
      title = exercise['title']
      if include_category:
        return { 'data': exercise }
      return { 'data': { 'id': id, 'tittle': title } }
  return {
    'error': 'Ejercicio no encontrado'
  }
  
@app.post('/exercises')
def create_exercise(exercise: ExerciseCreate):
  new_id = (EXERCISES[-1]['id'] + 1) if EXERCISES else 1
  new_exercise = { 'id': new_id, 'title': exercise.title, 'category': exercise.category }
  EXERCISES.append(new_exercise)

  return {
    'message': 'Ejercicio creado',
    'data': new_exercise
  }
  
@app.put('/exercises/{exercise_id}')
def put_exercise(exercise_id: int, data: ExerciseUpdate):
  for exercise in EXERCISES:
    if exercise_id == exercise['id']:
      playload = data.model_dump(exclude_unset=True) # {"title": "Remo", "category": None}
      if 'title' in playload: exercise['title'] = playload['title']
      if 'category' in playload: exercise['category'] = playload['category']
      return { 'message': 'Ejercicio actualizado correctamente', 'data': exercise }
  
  raise HTTPException(status_code=404, detail="Ejercicio no encontrado")

@app.delete('/exercises/{exercise_id}', status_code=204)
def delete_exercise(exercise_id: int):
  for index, exercise in enumerate(EXERCISES):
    if exercise['id'] == exercise_id:
      EXERCISES.pop(index)
      return
  raise HTTPException(status_code=404, detail="Ejercicio no encontrado")