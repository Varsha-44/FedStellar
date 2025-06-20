import itertools
import random
from abc import ABC, abstractmethod
from typing import List

import client as cl


class PeerSelector(ABC):
    inc = itertools.count(start=1)

    """
    Abstract class of peer selector.
    """
    def __init__(self):
        self.id_ = next(PeerSelector.inc)

    def __repr__(self):
        params = ', '.join([f'{key}={value}' for key, value in self.__dict__.values()])
        return f'{self.__class__.__name__}({params})'

    @abstractmethod
    def select(self, client: 'cl.Client') -> List['cl.Client']:
        ...


class NonePeerSelector(PeerSelector):
    def __init__(self):
        super().__init__()

    def select(self, client: 'cl.Client') -> List['cl.Client']:
        return []


class FullPeerSelector(PeerSelector):
    def __init__(self):
        super().__init__()

    def select(self, client: 'cl.Client') -> List['cl.Client']:
        return client.neighbors


class RandPeerSelector(PeerSelector):
    def __init__(self, p: float):
        super().__init__()
        self.p = p

    def select(self, client: 'cl.Client') -> List['cl.Client']:
        peers = list(filter(lambda neighbor: random.random() < self.p, client.neighbors))
        return peers
