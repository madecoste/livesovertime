# Copyright (c) 2012 Marc-Andre Decoste. All rights reserved.
# Use of this source code is governed by an Appache 2.0 license that can be
# found in the LICENSE file.

import base
import entities


# The Birth event marks the begining of the life of a Person at its birth place.
class Birth(base.Events):
  def __init__(self, child, father, mother, place, min_start_time,
               max_start_time, min_time_length = None, max_time_length = None):
    super(Death, self).__init__(min_start_time, max_start_time, min_time_length,
                                max_time_length)
    # The child is recognized by being the first element in the list.
    # Father and Mother should be the only two other Persons in the entities
    # and list and can be recognized by their sex.
    assert(not self.entities)
    self.entities.append(child.key())
    if place:
      self.entities.append(place.key())
    if father:
      assert(father.male_sex)
      self.entities.append(father.key())
    if mother:
      assert(mother.male_sex)
      self.entities.append(mother.key())
    self.Validate()

  def Validate(self):
    # There must be at least one entity for the child and a maximum of 4 to
    # include parents and birthplace.
    assert(len(self.entities) > 0 and len(self.entities) < 4)
    child = db.get(self.entities[0])
    place = None
    father = None
    mother = None
    for entitiy_key in self.entities[1:]:
      db.get(entitiy_key)
      if isinstance(entity, entities.Place):
        place = entity
      else:
        assert(isinstance(entity, entities.Person))
        if entity.male_sex:
          father = entity
        else:
          mother = entity

    assert(isinstance(child, entities.Person))
    assert(place is None or isinstance(place, entities.Place))
    assert(father is None or isinstance(father, entities.Person))
    assert(mother is None or isinstance(mother, entities.Person))
    super(Birth, self).Validate()


class Death(base.Events):
  def __init__(self, corpse, place, min_start_time, max_start_time, 
              min_time_length = None, max_time_length = None):
    super(Death, self).__init__(min_start_time, max_start_time, min_time_length,
                                max_time_length)
    self.events.append(corpse)
    if place:
      self.entities.append(place)

  def Validate(self):
    # There must be at least one entity for the corpse and a maximum of 2 to
    # include the deathplace.
    assert(len(self.entities) > 0 and len(self.entities) < 2)
    corpse = db.get(self.entities[0])
    if len(self.entities) == 2:
      place = db.get(self.entities[1])
    assert(isinstance(corpse, entities.Person))
    assert(place is None or isinstance(place, entities.Place))


class Marriage():
  pass