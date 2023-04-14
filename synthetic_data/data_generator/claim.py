import random
from statistics import mean
from .utils import sig

class claim:
  def __init__(self, claim_type, household, vehicle, driver = None):
    self.household = household
    self.vehicle = vehicle
    self.driver = driver

    self.when_occured = self.household.tenure_years

    if claim_type == 'single_car_collision':
      self.build_single_car_collision()
    elif claim_type == 'multi_car_collision':
      self.build_multi_car_collision()
    elif claim_type == 'theft':
      self.build_theft()
    elif claim_type == 'hail':
      self.build_hail()
    elif claim_type == 'glass':
      self.build_glass()
    elif claim_type == 'ubi':
      self.build_ubi()
    elif claim_type == 'ers':
      self.build_ers()

  def build_single_car_collision(self):
    self.bi = 0
    self.pd = 0
    self.coll = 1
    self.comp = 0
    self.mpc = 1
    self.ers = 0
    self.ubi = 0

  def build_multi_car_collision(self):
    self.bi = 1
    self.pd = 1
    self.coll = 1
    self.comp = 0
    self.mpc = 1
    self.ers = 0
    self.ubi = 0

  def build_theft(self):
    self.bi = 0
    self.pd = 0
    self.coll = 0
    self.comp = 1
    self.mpc = 0
    self.ers = 0
    self.ubi = 0

  def build_hail(self):
    self.bi = 0
    self.pd = 0
    self.coll = 0
    self.comp = 1
    self.mpc = 0
    self.ers = 0
    self.ubi = 0

  def build_glass(self):
    self.bi = 0
    self.pd = 0
    self.coll = 0
    self.comp = 1
    self.mpc = 0
    self.ers = 0
    self.ubi = 0

  def build_ubi(self):
    self.bi = 0
    self.pd = 0
    self.coll = 1
    self.comp = 0
    self.mpc = 0
    self.ers = 0
    self.ubi = 1
  
  def build_ers(self):
    self.bi = 0
    self.pd = 0
    self.coll = 0
    self.comp = 0
    self.mpc = 0
    self.ers = 1
    self.ubi = 0

  @property
  def summary(self):
    results = {
        'bi_ind': self.bi,
        'pd_ind': self.pd,
        'coll_ind': self.coll,
        'comp_ind': self.comp,
        'mpc_ind': self.mpc,
        'ers_ind': self.ers,
        'ubi_ind': self.ubi,
        'claim_age': self.how_old,
        'driver_claim': self.driver is not None
    }

    return results

  @property
  def vehicle_in_force(self):
    return any(self.vehicle == x for x in self.household.vehicles)

  @property
  def driver_in_force(self):
    if self.driver is None or self.household.drivers is None:
      return False

    return any(self.driver == x for x in self.household.drivers)

  @property
  def how_old(self):
    return self.household.tenure_years - self.when_occured