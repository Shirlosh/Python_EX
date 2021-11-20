from abc import ABC, abstractmethod


class ConnectorFactory(ABC):

    @abstractmethod
    def run(self):
        pass
