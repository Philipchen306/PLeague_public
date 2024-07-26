# -*- coding: utf-8 -*- #
# Copyright 2022 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The command to get the status of Workload Certificate Feature."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.command_lib.container.fleet.features import base


class Describe(base.DescribeCommand):
  """Describe the status of Workload Certificate Feature resource.

  Describe the status of Workload Certificate Feature resource in a Fleet.

  ## Examples

  To describe Service Feature, run:

    $ {command}
  """

  feature_name = 'workloadcertificate'
  feature_display_name = 'Workload Certificate'
  feature_api = 'workloadcertificate.googleapis.com'
