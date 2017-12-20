# !/usr/bin/python3
# coding: utf_8

# Copyright 2017-2018 Stefano Fogarollo
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


""" GDAX exchange """

from .core import CryptoExchange
from ..parsers import Parser


class GdaxParser(Parser):
    """ Parse transactions from GDAX exchange """

    def get_transactions_list(self, **kwargs):
        return super().get_transactions_list(
            "time",
            "%Y-%m-%dT%H:%M:%S.%fZ",
            ["amount", "balance"]
        )


class Gdax(CryptoExchange):
    """ Models GDAX exchange """
