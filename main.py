
class Animal:
  
  """Creating a general (common) class of our farm's animals"""
  
  total_weight = 0
  max_weight = 0
  max_weight_name = ''

  def __init__(self, name='some', weight=1):
    self.name = name
    self.weight = weight
    Animal.total_weight += self.weight

    if self.weight > Animal.max_weight:
      Animal.max_weight = self.weight
      Animal.max_weight_name = self.name

  def feed(self):
    return f'{self.name} - already feeded'

  def activities(self):
    return 'Taking care'


"""Creating particular classes with inherited characteristics"""

class Hens(Animal):
  class_name = 'chicken'
  def raise_voice(self):
    return 'co-co-co-do-do-do'
  def activities(self):
    return 'Picking up eggs'

class Duck(Animal):
  class_name = 'duck'
  def raise_voice(self):
    return 'quack-quack'
  def activities(self):
    return 'Picking up eggs'

class Goose(Animal):
  class_name = 'goose'
  def raise_voice(self):
    return 'gar-gar-gar'
  def activities(self):
    return 'Picking up eggs'

class Cow(Animal):
  class_name = 'cow'
  def raise_voice(self):
    return 'mooooooo'
  def activities(self):
    return 'Milking our cow'

class Sheep(Animal):
  class_name = 'sheep'
  def raise_voice(self):
    return 'baaaaa'
  def activities(self):
    return 'Clipping our sheep'

class Goat(Animal):
  class_name = 'goat'
  def raise_voice(self):
    return 'maaaa'
  def activities(self):
    return 'Milking our goat'

    ### Listing our animals with names and weights

grey_goose = Goose('Seriy', 8)
white_goose = Goose('Belliy', 9)
chicken_coco = Hens('Co-co', 3)
chicken_cucu = Hens('Cu-cu', 2) 
duck_quack = Duck('Quackrya', 4)
cow_manka = Cow('Mannka', 520)
sheep_varon = Sheep('Barashek', 35)
sheep_hembra = Sheep('Kudryash', 40)
goat_horns = Goat('Rojki', 22)
goat_hooves = Goat('Kopytko', 25)

### Printing some verifying samples

print(f'Our farm animal: {cow_manka.class_name}; its name is {cow_manka.name}.\nIt could speak like that - {cow_manka.raise_voice()}. And its weight now is {cow_manka.weight} kg.')
  
print(f'\n\nIn relation to our animal {duck_quack.class_name} usual activities are {duck_quack.activities()}.')

print(f'\nOur heaviest farm animal is {Animal.max_weight_name} and its weight is {Animal.max_weight} kg.')
print(f'\nThe total weight of all our farm animals is {Animal.total_weight} kg.')


print(f'\nOur cow is called {cow_manka.name} and its weight is { cow_manka.weight} kg.')
