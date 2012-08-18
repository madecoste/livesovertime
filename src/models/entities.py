# Copyright (c) 2012 Marc-Andre Decoste. All rights reserved.
# Use of this source code is governed by an Appache 2.0 license that can be
# found in the LICENSE file.

import base

# A Person entity identify a single individual person.
class Person(base.Entity):
  # The family name of the person.
  family_names = db.StringListProperty()
  # The set of given names of the person.
  given_names = db.StringListProperty()
  # A male is identified by a True value, False for a female.
  male_sex = db.BooleanProperty()

  def __init__(self, family_names, given_names, male_sex, locked=False):
    super(Person, self).__init__(locked)
    if (isinstance(family_names, (list, tuple))):
      self.family_names = family_names
    else:
      self.family_names.append(family_names)
    if (isinstance(given_names, (list, tuple))):
      self.given_names = given_names
    else:
      self.given_names.append(given_names)
    self.male_sex = male_sex

# A Location entity represent the exact geographical location where events
# occur. They don't have names, since the name of places change over time, so
# a PlaceName event must be attached to this entity to name it over a specific
# period of time.
class Location(base.Entity):
  # The geo-location of the place.
  geo_point = db.GeoPtProperty()

  def __init__(self, latitude, longitude, locked=False):
    super(Person, self).__init__(locked)
    assert(isinstance(latitude, Float))
    assert(isinstance(longitude, Float))
    self.geo_point.lat = latitude
    self.geo_point.lon = longitude
