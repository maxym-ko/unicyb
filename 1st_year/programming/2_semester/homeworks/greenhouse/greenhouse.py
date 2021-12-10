# Переписати, згідно рекомендацій Карнаух
import threading
import time


class Greenhouse:

    def __init__(self):
        self._windows = [False, False]
        self._opened_windows = 0
        self._heaters = [False, False, False]
        self._working_heaters = 0
        self._fuse = False
        self._humidity = 36.2
        self._temperature = 10
        self._start_time = time.time()
        # set up and start a thread for "__change()" method
        self._interval = 5
        self._thread_active = True
        self._thread = threading.Thread(target=self._change)
        self._thread.start()

    # change greenhouse conditions every "__interval" seconds
    def _change(self):
        while True and self._thread_active:
            current_time = time.time()
            if current_time - self.start_time > self._interval:
                if self.humidity > 65:
                    self._temperature = self.temperature - 1.4 - self.opened_windows * 0.9 + self.working_heaters * 2.3
                else:
                    self._temperature = self.temperature - 2.4 - self.opened_windows * 1.4 + self.working_heaters * 1.5 + self.humidity * 0.012

                if self.temperature > 16:
                    self._humidity += 4.6 * (self.opened_windows - self.working_heaters) ** 2
                else:
                    self._humidity -= (self.opened_windows - self.working_heaters) * 3.8

                self._check_conditions()
                self._start_time = current_time
            time.sleep(0.1)

    def _check_conditions(self):
        if self.temperature > (30.5 - self.humidity * 0.013) or self.temperature < 0 or self.humidity < 9.5 or self.humidity > 91.2:
            self._deactivate()

    def _deactivate(self):
        self._fuse = True
        for i in range(2):
            self._windows[i] = True
        for i in range(3):
            self._heaters[i] = False

    def _check_state(self) -> (bool, str):
        if self.fuse:
            return False, 'You cannot change any conditions, because the greenhouse is working in in emergency mode'
        else:
            return True, 'Greenhouse works properly'

    def open_window(self) -> (bool, str):
        success, res = self._check_state()
        if not success:
            return success, res

        success = False
        res = 'Failure. All windows are opened'
        if self.opened_windows != 2:
            i = 0
            while self._windows[i]:
                i += 1
            self._windows[i] = True
            self._opened_windows += 1
            success = True
            res = "One of the windows was opened"
        return success, res

    def close_window(self) -> (bool, str):
        success, res = self._check_state()
        if not success:
            return success, res

        success = False
        res = 'Failure. All windows are closed'
        if self.opened_windows != 0:
            i = 0
            while not self._windows[i]:
                i += 1
            self._windows[i] = False
            self._opened_windows -= 1
            success = True
            res = 'Window was closed'
        return success, res

    def switch_on_heater(self) -> (bool, str):
        success, res = self._check_state()
        if not success:
            return success, res

        success = False
        res = 'Failure. All heaters are working'
        if self.working_heaters != 3:
            i = 0
            while self._heaters[i]:
                i += 1
            self._heaters[i] = True
            self._working_heaters += 1
            success = True
            res = "One of the heaters was turned on"
        return success, res

    def switch_off_heater(self) -> (bool, str):
        success, res = self._check_state()
        if not success:
            return success, res

        success = False
        res = 'Failure. All heaters aren\'t working'
        if self.working_heaters != 0:
            i = 0
            while not self._heaters[i]:
                i += 1
            self._heaters[i] = False
            self._working_heaters += 1
            success = True
            res = "One of the heaters was turned off"
        return success, res

    def stop(self):
        self._thread_active = False

    def passed_time(self) -> (bool, str):
        current_time = time.time()
        passed = int(current_time - self.start_time)
        return True, f'{passed} sec passed'

    @property
    def windows(self):
        return self._windows

    @property
    def opened_windows(self):
        return self._opened_windows

    @property
    def heaters(self):
        return self._heaters

    @property
    def working_heaters(self):
        return self._working_heaters

    @property
    def fuse(self):
        return self._fuse

    @property
    def humidity(self):
        return self._humidity

    @property
    def temperature(self):
        return self._temperature

    @property
    def start_time(self):
        return self._start_time

    def __str__(self):
        if self.fuse:
            return 'Greenhouse broke down'
        else:
            return f'The greenhouse works properly. \n' \
                   f'There are: {len(self.windows)} windows ({self.opened_windows} opened); ' \
                   f'{len(self.heaters)} heaters ({self.working_heaters} working).\n' \
                   f'Temperature: {self.temperature} C; humidity: {self.humidity} % \n'
