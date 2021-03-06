#!/usr/bin/python
#
# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""TODO: High-level file comment."""

import sys


def main(argv):
    pass


if __name__ == '__main__':
    main(sys.argv)
HUMAN = 'resistance'
ZOMBIE = 'horde'
UNDECLARED = 'undeclared'
ALLEGIANCES = (HUMAN, ZOMBIE, UNDECLARED)
TEST_ENDPOINT = 'http://localhost:8080'
PLAYER_VOLUNTEER_ARGS = (
    'advertising', 'logistics', 'communications', 'moderator',
    'cleric', 'sorcerer', 'admin', 'photographer', 'chronicler',
    'server', 'client', 'android', 'ios')
POINTS_INFECT = 100

ACCESS_USER = 'user'
ACCESS_ADMIN = 'admin'
ACCESS_ADMIN_OR_PLAYER = 'adminOrPlayer'
ACCESS_PLAYER = 'player'
