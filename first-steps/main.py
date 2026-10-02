from fastapi import Body, FastAPI, Path, Query, HTTPException, Response
from pydantic import BaseModel, Field, field_validator, EmailStr
from typing import Literal, Optional, List, Any, Dict, Union
import math

app = FastAPI(title='Rimart health')

EXERCISES = [
  {
    'id': 1,
    'title': 'Remo con mancuerna',
    'tags': [
      {'name': 'Triceps'},
      {'name': 'Espalda'}
    ],
  },
  {
    'id': 2,
    'title': 'Press con barra',
    'category': 'pecho',
    'author': {
      'name': 'Rebeca Rivera',
      'email': 'rrivera@gmail.com'
    }
  },
  {
    'id': 3,
    'title': 'Copa con mancuerna',
    'category': 'triceps'
  },
  {
    'id': 4,
    'title': 'Flexiones en barra',
    'tags': [
      {'name': 'Espalda'},
      {'name': 'Brazos'},
      {'name': 'Core'}
    ],
    'category': 'espalda'
  },
  {
    'id': 5,
    'title': 'Sentadillas con mancuernas',
    'category': 'piernas',
    'author': {
      'name': 'Carlos Mendez',
      'email': 'cmendez@fitness.com'
    },
    'tags': [
      {'name': 'Piernas'},
      {'name': 'Glúteos'}
    ]
  },
  {
    'id': 6,
    'title': 'Extensiones de tríceps con cuerda',
    'category': 'triceps',
    'tags': [
      {'name': 'Triceps'},
      {'name': 'Brazos'}
    ]
  },
  {
    'id': 7,
    'title': 'Remo en máquina',
    'category': 'espalda',
    'author': {
      'name': 'Laura Gómez',
      'email': 'lgomez@fitpro.com'
    }
  },
  {
    'id': 8,
    'title': 'Press inclinado con barra',
    'tags': [
      {'name': 'Pecho'},
      {'name': 'Hombros'},
      {'name': 'Triceps'}
    ]
  },
  {
    'id': 9,
    'title': 'Jalones en polea alta',
    'category': 'espalda',
    'tags': [
      {'name': 'Espalda'},
      {'name': 'Brazos'}
    ],
    'author': {
      'name': 'Miguel Torres',
      'email': 'mtorres@gym.com'
    }
  },
  {
    'id': 10,
    'title': 'Curl de bíceps con mancuerna',
    'category': 'biceps',
    'tags': [
      {'name': 'Biceps'},
      {'name': 'Brazos'}
    ]
  },
  {
    'id': 11,
    'title': 'Elevaciones laterales con mancuernas',
    'category': 'hombros',
    'tags': [
      {'name': 'Hombros'},
      {'name': 'Deltoides'}
    ]
  },
  {
    'id': 12,
    'title': 'Peso muerto convencional',
    'category': 'espalda baja',
    'author': {
      'name': 'Ana Ruiz',
      'email': 'aruiz@strength.com'
    },
    'tags': [
      {'name': 'Espalda baja'},
      {'name': 'Core'},
      {'name': 'Piernas'}
    ]
  },
  {
    'id': 13,
    'title': 'Sentadillas frontal',
    'category': 'piernas',
    'tags': [
      {'name': 'Piernas'},
      {'name': 'Cuadriceps'}
    ]
  },
  {
    'id': 14,
    'title': 'Press de hombros',
    'category': 'hombros',
    'author': {
      'name': 'Juan García',
      'email': 'jgarcia@training.com'
    }
  },
  {
    'id': 15,
    'title': 'Fondos en banco',
    'category': 'triceps',
    'tags': [
      {'name': 'Triceps'},
      {'name': 'Pecho'},
      {'name': 'Hombros'}
    ]
  },
  {
    'id': 16,
    'title': 'Remo invertido',
    'category': 'espalda',
    'tags': [
      {'name': 'Espalda'},
      {'name': 'Biceps'}
    ]
  },
  {
    'id': 17,
    'title': 'Leg press',
    'category': 'piernas',
    'author': {
      'name': 'Sofia López',
      'email': 'slopez@gym.com'
    }
  },
  {
    'id': 18,
    'title': 'Crunch abdominal',
    'category': 'abdominales',
    'tags': [
      {'name': 'Core'},
      {'name': 'Abdominales'}
    ]
  },
  {
    'id': 19,
    'title': 'Aperturas con mancuernas',
    'category': 'pecho',
    'tags': [
      {'name': 'Pecho'}
    ]
  },
  {
    'id': 20,
    'title': 'Curl de bíceps en barra',
    'category': 'biceps',
    'author': {
      'name': 'Roberto Díaz',
      'email': 'rdiaz@fitnesscenter.com'
    }
  },
  {
    'id': 21,
    'title': 'Máquina de remo',
    'category': 'espalda',
    'tags': [
      {'name': 'Espalda'},
      {'name': 'Cardio'}
    ]
  },
  {
    'id': 22,
    'title': 'Prensa de piernas 45°',
    'category': 'piernas',
    'tags': [
      {'name': 'Piernas'},
      {'name': 'Glúteos'},
      {'name': 'Cuadriceps'}
    ]
  },
  {
    'id': 23,
    'title': 'Vuelos invertidos',
    'category': 'hombros',
    'author': {
      'name': 'Mariana Ruiz',
      'email': 'mruiz@training.com'
    }
  },
  {
    'id': 24,
    'title': 'Encogimientos de hombros',
    'category': 'trapecios',
    'tags': [
      {'name': 'Trapecios'},
      {'name': 'Hombros'}
    ]
  },
  {
    'id': 25,
    'title': 'Extensiones de pierna',
    'category': 'cuadriceps',
    'tags': [
      {'name': 'Piernas'},
      {'name': 'Cuadriceps'}
    ]
  },
  {
    'id': 26,
    'title': 'Flexiones de pierna',
    'category': 'isquiotibiales',
    'author': {
      'name': 'Fernando Moreno',
      'email': 'fmoreno@gym.com'
    }
  },
  {
    'id': 27,
    'title': 'Levantamiento de talones',
    'category': 'pantorrillas',
    'tags': [
      {'name': 'Pantorrillas'}
    ]
  },
  {
    'id': 28,
    'title': 'Press de banca plana',
    'category': 'pecho',
    'tags': [
      {'name': 'Pecho'},
      {'name': 'Triceps'},
      {'name': 'Hombros'}
    ]
  },
  {
    'id': 29,
    'title': 'Polea al pecho',
    'category': 'espalda',
    'author': {
      'name': 'Valeria Torres',
      'email': 'vtorres@fitness.com'
    }
  },
  {
    'id': 30,
    'title': 'Twist ruso con peso',
    'category': 'abdominales',
    'tags': [
      {'name': 'Core'},
      {'name': 'Oblicuos'}
    ]
  },
  {
    'id': 31,
    'title': 'Dips en paralelas',
    'category': 'triceps',
    'tags': [
      {'name': 'Triceps'},
      {'name': 'Pecho'},
      {'name': 'Hombros'}
    ]
  },
  {
    'id': 32,
    'title': 'Jalones al mentón',
    'category': 'hombros',
    'author': {
      'name': 'Alejandro Pérez',
      'email': 'aperez@training.com'
    }
  },
  {
    'id': 33,
    'title': 'Remo pendular',
    'category': 'espalda',
    'tags': [
      {'name': 'Espalda'},
      {'name': 'Cuadriceps'}
    ]
  },
  {
    'id': 34,
    'title': 'Press cerrado con barra',
    'category': 'triceps',
    'tags': [
      {'name': 'Triceps'},
      {'name': 'Pecho'}
    ]
  },
  {
    'id': 35,
    'title': 'Sentadilla búlgara',
    'category': 'piernas',
    'author': {
      'name': 'Daniela García',
      'email': 'dgarcia@gym.com'
    }
  },
  {
    'id': 36,
    'title': 'Peso muerto sumo',
    'category': 'piernas',
    'tags': [
      {'name': 'Piernas'},
      {'name': 'Glúteos'},
      {'name': 'Espalda baja'}
    ]
  },
  {
    'id': 37,
    'title': 'Flexiones con agarre ancho',
    'category': 'pecho',
    'tags': [
      {'name': 'Pecho'},
      {'name': 'Espalda'}
    ]
  },
  {
    'id': 38,
    'title': 'Hiperextensiones',
    'category': 'espalda baja',
    'author': {
      'name': 'Luis Sánchez',
      'email': 'lsanchez@fitness.com'
    }
  },
  {
    'id': 39,
    'title': 'Plancha frontal',
    'category': 'core',
    'tags': [
      {'name': 'Core'},
      {'name': 'Abdominales'}
    ]
  },
  {
    'id': 40,
    'title': 'Fondos en paralelas',
    'category': 'pecho',
    'tags': [
      {'name': 'Pecho'},
      {'name': 'Triceps'},
      {'name': 'Hombros'}
    ]
  },
  {
    'id': 41,
    'title': 'Curl inclinado con mancuerna',
    'category': 'biceps',
    'author': {
      'name': 'Patricia Vázquez',
      'email': 'pvazquez@training.com'
    }
  },
  {
    'id': 42,
    'title': 'Prensa de pecho',
    'category': 'pecho',
    'tags': [
      {'name': 'Pecho'},
      {'name': 'Triceps'}
    ]
  },
  {
    'id': 43,
    'title': 'Abducción de cadera',
    'category': 'glúteos',
    'tags': [
      {'name': 'Glúteos'},
      {'name': 'Piernas'}
    ]
  },
  {
    'id': 44,
    'title': 'Aducción de cadera',
    'category': 'muslos internos',
    'author': {
      'name': 'Gustavo López',
      'email': 'glopez@gym.com'
    }
  },
  {
    'id': 45,
    'title': 'Extensión de cadera',
    'category': 'glúteos',
    'tags': [
      {'name': 'Glúteos'},
      {'name': 'Espalda baja'}
    ]
  },
  {
    'id': 46,
    'title': 'Flexiones de brazos',
    'category': 'pecho',
    'tags': [
      {'name': 'Pecho'},
      {'name': 'Triceps'},
      {'name': 'Core'}
    ]
  },
  {
    'id': 47,
    'title': 'Levantamiento de rodillas',
    'category': 'abdominales',
    'author': {
      'name': 'Camila Morales',
      'email': 'cmorales@fitness.com'
    }
  },
  {
    'id': 48,
    'title': 'Desplantes con mancuernas',
    'category': 'piernas',
    'tags': [
      {'name': 'Piernas'},
      {'name': 'Glúteos'},
      {'name': 'Cuadriceps'}
    ]
  },
  {
    'id': 49,
    'title': 'Pull-up asistido',
    'category': 'espalda',
    'tags': [
      {'name': 'Espalda'},
      {'name': 'Biceps'},
      {'name': 'Core'}
    ]
  },
  {
    'id': 50,
    'title': 'Máquina de pecho mariposa',
    'category': 'pecho',
    'author': {
      'name': 'Rafael Núñez',
      'email': 'rnunez@training.com'
    }
  }
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

class PaginatedExercise(BaseModel):
  limit: int
  offset: int
  items: List[ExercisePublic]
  
class CompletePaginatedExercise(BaseModel):
  page: int
  per_page: int
  has_prev: bool
  has_next: bool
  items: List[ExercisePublic]
  
class CompletePaginatedExerciseMetada(BaseModel):
  total: int
  total_pages: int
  order_by: Literal["id", "title"]
  direction: Literal["asc", "desc"]
  search: str
  items: List[CompletePaginatedExercise]

@app.get('/')
def home():
  return {
    'message': 'Bienvenidos a rimart health por Isaac Martinez'
  }

@app.get('/exercises', response_model=CompletePaginatedExerciseMetada, response_description='Todos los ejercicios')
def get_exercises(
  query: Optional[str] = Query(
    default=None,
    description='Texto para buscar por titulo',
    alias='search',
    min_length=3,
    max_length=50,
    pattern=r"^[\w\sáéíóúÁÉÍÓÚüÜ-]+$"
  ),
  limit: int = Query(
    10,
    ge=1,
    le=50,
    description="Número de resultados (1-50)"
  ),
  offset: int = Query(
    0,
    ge=0,
    description="Elementos a saltar antes de empezar la lista"
  ),
  order_by: Literal["id", "title"] = Query(
    "id",
    description="Campo de orden"
  ),
  direction: Literal["asc", "desc"] = Query(
    "asc",
    description="Dirección de orden"
  ),
  per_page: int = Query(
    1,
    ge=1,
    le=10,
    description="Ejercicios por pagina"
  )
):
  total_results = [exercise for exercise in EXERCISES if query.lower() in exercise["title"].lower()]
  total_results = sorted(total_results, key=lambda exercise: exercise[order_by], reverse=(direction == "desc"))
  total_results = total_results[offset: offset + limit]
  total = len(total_results)
  total_pages = math.ceil(total / per_page) if total > 0 else 0
  
  results = [ { "page": page + 1 } for page in range(total_pages) ]
  for r in range(0, len(results)):
    results[r]["per_page"] = per_page if len(total_results) >= per_page else len(total_results)
    results[r]["has_prev"] = False if r == 0 else True
    results[r]["has_next"] = False if r == (len(results) - 1) else True
    results[r]["items"] = total_results[:per_page]
    total_results = total_results[per_page:]

  return CompletePaginatedExerciseMetada(total=total, total_pages=total_pages, order_by=order_by, direction=direction, search=query, items=results)

@app.get('/exercises/by-tags', response_model=List[ExercisePublic])
def list_by_tags(
  tags: List[str] = Query(
    ...,
    min_length=2,
    description="Una o mas etiquetas",
    examples=[
      "Pecho",
      "Espalda",
      "Triceps",
      "Biceps"
    ]
  )
):
  tags_lower = [tag.lower() for tag in tags]
  
  return [
    exercise for exercise in EXERCISES
    if all(any(tag['name'].lower() == t for tag in exercise.get('tags', [])) for t in tags_lower)
  ]

# Si volteas el Union al solicitar un exercise sin category (include_category=False) si devuelve un category el cual es el valor por defecto ("Sin categoria")
@app.get('/exercises/{exercise_id}', response_model=Union[ExerciseSummary, ExercisePublic], response_description='Ejercicio devuelto')
def get_exercise_by_id(
  exercise_id: int = Path(
    ...,
    ge=1,
    title='ID del ejercicio',
    description='Identificador entero del ejercicio, debe ser mayor a 1',
    example=1
  ), 
  include_category: bool = Query(
    default=True,
    description='Incluir o no la categoria'
  )
):
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
    'tags': [tag.model_dump() for tag in exercise.tags],
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