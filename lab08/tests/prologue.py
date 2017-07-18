test = {
  'name': 'Prologue',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from car import *
          >>> stans_car = Car('Tesla', 'Model S')
          >>> stans_car.color
          80d498e7f8cbec95df437d78b524521a
          # locked
          >>> stans_car.paint('black')
          1b93d7f83f69e1b06c11954d997cf04f
          # locked
          >>> stans_car.color
          9ccdc90cb9022261857bac913f59ab65
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> from car import *
          >>> stans_car = Car('Tesla', 'Model S')
          >>> stans_truck = MonsterTruck('Monster Truck', 'XXL')
          >>> stans_car.size
          8b1b16415e2c0ff19bfb5c4e54f6f878
          # locked
          >>> stans_truck.size
          c5ace7df7c7b66fd8733af007dd50564
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
