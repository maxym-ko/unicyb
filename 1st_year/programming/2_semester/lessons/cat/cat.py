class Cat:
    __low = 0.0
    __upp = 100.0

    def __init__(self, energy: float):
        if not isinstance(energy, float):
            energy = float(energy)
        self._energy: float = energy
        self._activity = True
        self._check()

    def _check(self):
        if not self._good():
            self._deactivate()

    def _deactivate(self):
        self._activity = False
        self._energy = 0.0

    def _good(self):
        return self._lower() <= self.energy < self._upper()

    @staticmethod
    def _lower():
        return Cat.__low

    @staticmethod
    def _upper():
        return Cat.__upp

    def run(self):
        if self:
            print(" I'm running...")  # shouldn't be here
            self._energy_change(self._energy_run_loss())
        #     return True, ''
        # else:
        #     return False, '....'
        return self

    def _energy_change(self, amount: float):
        self._energy += amount
        self._check()

    def _energy_run_loss(self):
        return -self.energy * 0.01

    def sleep(self):
        pass

    def eat(self):
        pass

    @property
    def energy(self):
        return self._energy

    def __bool__(self):
        return self._activity

    def __str__(self):
        return f"{self.energy=}, {self._activity=}"
