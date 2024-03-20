from fractions import Fraction
from decimal import Decimal


#will amount be required?
class Food():
  """Base class for all food in shopping list."""
  def __init__(self, amount=0, name='', aisle=" "):
      self.amount = amount
      self.name = name
      self.aisle = '' # Define instance variable inside __init__

  
  def __init__(self, amount=0, name=''):
    self.amount = Fraction(amount)
    self.name = name
    #ie 14.5 oz. can  
   
  def __str__(self):
        if not self.name:
            return str(self.amount)
        else:
            return f"{self.amount}+{self.name}"

    
  def __add__(self, rhs):
    return self.amount + rhs
  
  def __radd__(self, lhs):
    return lhs + self.amount
  
  def __sub__(self, rhs):
    return self.amount - rhs
  
  def __rsub__(self, lhs):
    return lhs - self.amount
  
  def __mul__(self, rhs):
    return self.amount * rhs
  
  def __rmul__(self, lhs):
    return self.amount * lhs
  
  def __truediv__(self, rhs):
    return self.amount / rhs
  
  def __rtruediv__(self, lhs):
    return lhs / self.amount
  
  #vary for each food item. All Fractions should round up to total number of items needed. 10 oz, 12 oz would be 2 10 oz, etc?
  def __mod__(self, rhs):
    pass

#foods need to be modified, unit of measure or name
#meats
class ChickenBreast(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'chicken breast'
    self.aisle = 'meat'
    

  def __str__(self):
    return Super.__str__() + " " + self.food

class BeefChuckRoast(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'beef chuck roast'
    self.aisle = 'meat'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

  
class GroundBeef(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(amount, unitOfMeasure)
    self.food = 'ground beef'
    self.aisle = 'meat'
    
  def __str__(self):
    return Super.__str__() + " " + self.food
  
class GroundItalianSausage(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(amount, unitOfMeasure)
    self.food = 'ground italian sausage'
    self.aisle = 'meat'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class ItalianSausage(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(amount, unitOfMeasure)
    self.food = 'italian sausage'
    self.aisle = 'meat'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class PorkShoulder(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(amount, unitOfMeasure)
    self.food = 'pork shoulder'
    self.aisle = 'meat'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class Bacon(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(amount, unitOfMeasure)
    self.food = 'bacon'
    self.aisle = 'meat'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class GroundTurkey(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(amount, unitOfMeasure)
    self.food = 'ground turkey'
    self.aisle = 'meat'
    
  def __str__(self):
    return Super.__str__() + " " + self.food
  
class HamSteak(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(amount, unitOfMeasure)
    self.food = 'bone in ham bone steak'
    self.aisle = 'meat'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class ChickenThighs(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(amount, unitOfMeasure)
    self.food = 'chicken thighs'
    self.aisle = 'meat'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class SerloinTipRoast(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(amount, unitOfMeasure)
    self.food = 'sliced & fat trimmed boneless sirloin tip roast'
    self.aisle = 'meat'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

  #Dairy

class AmericanCheese(Food):
  def __init__(self, amount=1, unitOfMeasure='slice'):
    Super().__init__(amount, unitOfMeasure)
    self.food = 'American cheese'
    self.aisle = 'dairy'
    
  def __str__(self):
    return Super.__str__() + " " + self.food
  
class HeavyCream(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'heavy cream'
    self.aisle = 'dairy'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class Milk(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'milk'
    self.aisle = 'dairy'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class HeavyWhippingCream(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'heavy whipping cream'
    self.aisle = 'dairy'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class ParmeseanCheese(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'parmesean cheese'
    self.aisle = 'dairy'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class Butter(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'butter'
    self.aisle = 'dairy'
    
  def __str__(self):
    return Super.__str__() + " " + self.food
  
class EvaporatedMilk(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'evaporated milk'
    self.aisle = 'dairy'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class CreamCheese(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'cream cheese'
    self.aisle = 'dairy'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class SourCream(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'sour cream'
    self.aisle = 'dairy'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class MontereyJackCheese(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'monterey jack cheese'
    self.aisle = 'dairy'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class CheddarCheese(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'cheddar cheese'
    self.aisle = 'dairy'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class ShreddedCheddar(Food): #same as above 
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'shredded cheddar'
    self.aisle = 'dairy'
    
  def __str__(self):
    return Super.__str__() + " " + self.food
  
#Veggies
class baby_carrots(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'baby carrots'
    self.aisle = 'veggie'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class Carrots(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'carrots'
    self.aisle = 'veggie'
   
  def __str__(self):
    return Super.__str__() + " " + self.food


class Onion(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'onion'
    self.aisle = 'veggie'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class Spinach(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'spinach'
    self.aisle = 'veggie'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class FrozenBellPeppers(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'frozen bell peppers'
    self.aisle = 'veggie'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class GreenOnions(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'green onions'
    self.aisle = 'veggie'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class DicedTomatoes(Food):
  def __init__(self, amount=1, unitOfMeasure='14.5 oz'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'diced tomatoes'
    self.aisle = 'veggie' #can
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class Zucchini(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'zucchini'
    self.aisle = 'veggie'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class SmallCabbage(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'small cabbage'
    self.aisle = 'veggie'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class RedBellPepper(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'red bell pepper'
    self.aisle = 'veggie'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class RainbowPeppers(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'rainbow peppers'
    self.aisle = 'veggie'
    
  def __str__(self):
    return Super.__str__() + " " + self.food
  #fix below
class ButternutSquash(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'butternut squash'
    self.aisle = 'veggie'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class FrozenCorn(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'frozen corn'
    self.aisle = 'veggie'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class DarkRedKidneyBeans(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'dark red kidney beans'
    self.aisle = 'veggie'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class GreenBeans(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'grean beans'
    self.aisle = 'veggie'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class RedPotatoes(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'red potatoes'
    self.aisle = 'veggie'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class Celery(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'celery'
    self.aisle = 'veggie'
    #play with this one stalks change to bunches or pounds
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class CannelliniBeans(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'cannellini beans('
    self.aisle = 'veggie'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class BlackBeans(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'black beans'
    self.aisle = 'veggie'
    
  def __str__(self):
    return Super.__str__() + " " + self.food
    
'''
class Celery(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'celery'
    self.aisle = 'veggie'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class Celery(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'celery'
    self.aisle = 'veggie'
    
  def __str__(self):
    return Super.__str__() + " " + self.food
    
class Celery(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'celery'
    self.aisle = 'veggie'
    
  def __str__(self):
    return Super.__str__() + " " + self.food
    
class Celery(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'celery'
    self.aisle = 'veggie'
    
  def __str__(self):
    return Super.__str__() + " " + self.food
 
class Celery(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'celery'
    self.aisle = 'veggie'
    
  def __str__(self):
    return Super.__str__() + " " + self.food
    
class Celery(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'celery'
    self.aisle = 'veggie'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class Celery(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'celery'
    self.aisle = 'veggie'
    
  def __str__(self):
    return Super.__str__() + " " + self.food
    
class Celery(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'celery'
    self.aisle = 'veggie'
    
  def __str__(self):
    return Super.__str__() + " " + self.food
    
class Celery(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'celery'
    self.aisle = 'veggie'
    
  def __str__(self):
    return Super.__str__() + " " + self.food
    
class Celery(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'celery'
    self.aisle = 'veggie'
    
  def __str__(self):
    return Super.__str__() + " " + self.food
    
class Celery(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'celery'
    self.aisle = 'veggie'
    
  def __str__(self):
    return Super.__str__() + " " + self.food
'''

#spices and sauces, pasta
#Non-food items
class FreezerBag(Food):
  def __init__(self, amount='1'):
    Super().__init__(amount)
    self.food = 'freezer bag'
    self.category = 'non-food'
               
  def __str__(self):
    return Super.__str__() + " " + self.food

