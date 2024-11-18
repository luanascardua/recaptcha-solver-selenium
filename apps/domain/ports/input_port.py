from abc import ABC, abstractmethod

class RecaptchaSolverInputPort(ABC):
    @abstractmethod
    def solve_recaptcha(self, url):
        pass
