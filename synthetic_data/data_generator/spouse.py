import random
from statistics import mean
from .utils import sig

from .human import human

class spouse(human):
  """
  The least special of the human classes 😝
  A spouse's age/upbrining score/etc... is mostly determined by the head_of_house.
  Often the gender will be opposite that of the head_of_house object, but there is a chance to have a gay couple.

  For all other purposes they are a normal human that drives cars and generates claims.
  """
  def __init__(self, household, so):
    # Pick an age that is slightly lower than the head of house
    age_lowerbound = max(int(so.age/2 + 7), 18)
    age_upperbound = so.age
    age_mode = so.age-2

    if age_lowerbound < age_mode < age_upperbound:
      target_age = int(random.triangular(age_lowerbound, so.age, mode = so.age - 2))
    else:
      target_age = so.age

    # Decide if the couple is same or different sex
    straight_couple = random.choices([True, False], weights = [0.9, 0.1])[0]
    if not straight_couple:
      target_gender = so.gender
    else:
      target_gender = 'm' if so.gender == 'f' else 'f'

    # Pick an upbringing that is similar to the head of house
    target_upbringing_score = so.upbringing_score + random.normalvariate(0, 0.5)

    super().__init__(household = household, 
                     target_age = target_age, 
                     target_gender = target_gender, 
                     upbringing_score = target_upbringing_score)

    self.get_married()