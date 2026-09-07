from fastapi import Body, FastAPI, Path, Query, HTTPException, Response
from pydantic import BaseModel, Field, field_validator, EmailStr
from typing import Optional, List, Any, Dict, Union

app = FastAPI(title='Rimart health')

EXERCISES = [
  { 'id': 1, 'title': 'Remo con mancuerna' },
  { 'id': 2, 'title': 'Press con barra', 'category': 'pecho' },
  { 'id': 3, 'title': 'Copa con mancuerna', 'category': 'triceps' }
]

FORBIDDEN_WORDS = [
  'descanso',
  'cardio',
  'bicicleta',
  'eliptica',
  'escaladora'
]

class Tag(BaseModel):
  name: str = Field(
    ...,
    min_length=3,
    max_length=30,
    description="Nombre de la etiqueta"
  )
  
class Author(BaseModel):
  name: str = Field(
    ...,
    min_length=3,
    max_length=50,
    description="Nombre del autor"
  )
  email: EmailStr = Field(
    ...,
    min_length=3,
    max_length=50,
    description="Email del autor"
  )

class BaseExercise(BaseModel):
  title: str
  category: Optional[str] = "Sin categoria" # Si se pone None el valor por defecto quedaria como null
  tags: Optional[List[Tag]] = Field(default_factory=list)
  author: Optional[Author] = None

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
  tags: Optional[List[Tag]] = Field(default_factory=list)
  author: Optional[Author] = None
  
  #? Se usa para validaciones personalizadas
  @field_validator('title')
  @classmethod # Indica que el metodo es de clase
  def not_allowed_words_in_title(cls, value:str) -> str:
    for forbidden_word in FORBIDDEN_WORDS:
      if forbidden_word in value.lower(): raise ValueError(f'El titulo no puede contener la palabra: "{forbidden_word}"')
    return value

class ExerciseUpdate(BaseModel):
  title: Optional[str] = Field(None, min_length=3, max_length=100)
  category: Optional[str] = None # Si se pone None se guardara el valor anterior
  tags: Optional[List[Tag]] = Field(default_factory=list)
  author: Optional[Author] = None

class ExercisePublic(BaseExercise):
  id: int
  
class ExerciseSummary(BaseModel):
  id: int
  title: str
  tags: Optional[List[Tag]] = Field(default_factory=list)
  author: Optional[Author] = None

@app.get('/')
def home():
  return {
    'message': 'Bienvenidos a rimart health por Isaac Martinez'
  }

@app.get('/exercises', response_model=List[ExercisePublic], response_description='Todos los ejercicios')
def get_exercises(query: str | None = Query(default=None, description='Texto para buscar por titulo')):
  if query:
    return [ exercise for exercise in EXERCISES if query.lower() in exercise['title'].lower() ]

  return EXERCISES

@app.get('/exercises/{exercise_id}', response_model=Union[ExerciseSummary, ExercisePublic], response_description='Ejercicio devuelto') # Si volteas el Union al solicitar un exercise sin category (include_category=False) si devuelve un category el cual es el valor por defecto ("Sin categoria")
def get_exercise_by_id(exercise_id: int = Path(
    ...,
    ge=1,
    title='ID del ejercicio',
    description='Identificador entero del ejercicio, debe ser mayor a 1',
    example=1
  ), include_category: bool = Query(default=True, description='Incluir o no la categoria')):
  for exercise in EXERCISES:
    if exercise['id'] == exercise_id:
      if include_category:
        return exercise
      return { 'id': exercise['id'], 'title': exercise['title'], 'tags': exercise['tags'], 'author': exercise['author'] }
  raise HTTPException(status_code=404, detail="Ejercicio no encontrado")
  
@app.post('/exercises', response_model=ExercisePublic, response_description="Ejercicio creado")
def create_exercise(exercise: ExerciseCreate):
  new_id = (EXERCISES[-1]['id'] + 1) if EXERCISES else 1
  new_exercise = { 
    'id': new_id,
    'title': exercise.title,
    'category': exercise.category,
    'tags': [tag.model_dump() for tag in exercise.tags ],
    'author': exercise.author.model_dump() if exercise.author else None
  }
  EXERCISES.append(new_exercise)

  return new_exercise
  
@app.put('/exercises/{exercise_id}', response_model=ExercisePublic, response_description="Ejercicio actualizado", response_model_exclude_none=True)
def put_exercise(exercise_id: int, data: ExerciseUpdate):
  for exercise in EXERCISES:
    if exercise_id == exercise['id']:
      playload = data.model_dump(exclude_unset=True) # {"title": "Remo", "category": None}
      if 'title' in playload: exercise['title'] = playload['title']
      if 'category' in playload: exercise['category'] = playload['category']
      if 'tags' in playload: exercise['tags'] = playload['tags']
      if 'author' in playload: exercise['author'] = playload['author']
      return exercise
  
  raise HTTPException(status_code=404, detail="Ejercicio no encontrado")

@app.delete('/exercises/{exercise_id}', status_code=204)
def delete_exercise(exercise_id: int):
  for index, exercise in enumerate(EXERCISES):
    if exercise['id'] == exercise_id:
      EXERCISES.pop(index)
      return
  raise HTTPException(status_code=404, detail="Ejercicio no encontrado")