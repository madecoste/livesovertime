# Copyright (c) 2012 Marc-Andre Decoste. All rights reserved.
# Use of this source code is governed by an Appache 2.0 license that can be
# found in the LICENSE file.

from google.appengine.ext import db

# The Operation class is used to keep information about modifications made to
# a BaseNode object.
class Operation(db.Model):
  # The user who initiated this operation.
  user = db.UserProperty(auto_current_user_add=True)
  # The action that this operation represent.
  action = db.StringProperty()
  # The arguments needed to execute the action.
  arguments = db.StringListProperty()
  # The time at which this operation was created.
  creation_time = db.DateTimeProperty(auto_now_add=True)
  # The time at which this operation was applied.
  applied_time = db.DateTimeProperty(auto_now_add=True)


# A Base class containing utilies for all model classes.
class BaseNode(db.Model):
  # The user that created this node.
  user = db.UserProperty(auto_current_user_add=True)
  # When this node was created.
  creation_time = db.DateTimeProperty(auto_now_add=True)
  # When this node was modified.
  modification_time = db.DateTimeProperty(auto_now=True)
  # A list of operations that were applied to this node.
  modification_history = db.ListProperty(db.Key)
  # A locked node can only be modified by the user that created it.
  locked = db.BooleanProperty()
  # A list of proposed changes to the node that have not been moderated yet.
  pending_changes = db.ListProperty(db.Key)


class Entity(Base):
  # The list of events connected to this entiry.
  # TODO(madecoste): Validate event type?
  events = db.ListProperty(db.Key)


class Events(Base):
  # The list of entities connected to this event.
  # TODO(madecoste): Validate entities type?
  entities = db.ListProperty(db.Key)
  # The minimum start time of this event. When not set, it means we don't have
  # a lower boundary, so it could be anytime before the max.
  min_start_time = db.DatetimeProperty()
  # The maximum start time of this event. When not set, it means we don't have
  # a lower boundary, so it could be anytime after the min. So at least one of
  # min and max must be set, and they must be equal to represent a precisely
  # known time.
  max_start_time = db.DatetimeProperty()
  # min/max length are used for the same uncerntainty range, except that having
  # both not set is allowed to idenitify a punctual event.
  min_time_length = db.DatetimeProperty()
  max_time_length = db.DatetimeProperty()

