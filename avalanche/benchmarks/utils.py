#!/usr/bin/env python
# -*- coding: utf-8 -*-

################################################################################
# Copyright (c) 2020 ContinualAI Research                                      #
# Copyrights licensed under the CC BY 4.0 License.                             #
# See the accompanying LICENSE file for terms.                                 #
#                                                                              #
# Date: 1-05-2020                                                              #
# Author(s): Vincenzo Lomonaco                                                 #
# E-mail: contact@continualai.org                                              #
# Website: clair.continualai.org                                               #
################################################################################

""" Common benchmarks/environments utils. """

# Python 2-3 compatible
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

from typing import List, Iterable

import numpy as np
from torch import Tensor


def remove_some_labels(dataset, labels_set, scale_labels=False):
    """ This method simply remove patterns with labels contained in
        the labels_set. """

    data, labels = dataset
    for label in labels_set:
        # Using fun below copies data
        mask = np.where(labels == label)[0]
        labels = np.delete(labels, mask)
        data = np.delete(data, mask, axis=0)

    if scale_labels:
        # scale labels if they do not start from zero
        min = np.min(labels)
        labels = (labels - min)

    return data, labels


def change_some_labels(dataset, labels_set, change_set):
    """ This method simply change labels contained in
        the labels_set. """

    data, labels = dataset
    for label, change in zip(labels_set, change_set):
        mask = np.where(labels == label)[0]
        labels = np.put(labels, mask, change)

    return data, labels


def tensor_as_list(sequence) -> List:
    # Numpy: list(np.array([1, 2, 3])) returns [1, 2, 3]
    # whereas: list(torch.tensor([1, 2, 3])) returns ->
    # -> [tensor(1), tensor(2), tensor(3)]
    #
    # This is why we have to handle Tensor in a different way
    if isinstance(sequence, list):
        return sequence
    if not isinstance(sequence, Iterable):
        return [sequence]
    if isinstance(sequence, Tensor):
        return sequence.tolist()
    return list(sequence)
