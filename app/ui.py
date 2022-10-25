from PyQt5 import uic

import arr
import timer

form, base = uic.loadUiType("main.ui")

ARRAY_SIZE = 1_000_000
SEARCH_REPEATS = 5_000
DIVIDER = 100


class LabUi(base, form):
    def __init__(self):

        self._arr = arr.BinsearchArray(ARRAY_SIZE)

        super(base, self).__init__()
        self.setupUi(self)
        self._configure_ui()

    def _configure_ui(self):
        self.key.setMaximum(self._arr.get_max())

        self.updateBtn.clicked.connect(self._update_arrays)
        self.sBtn.clicked.connect(self._search)

    def _search(self):
        print("search")
        self._search1()
        self._search2()
        self._search3()
        self._search4()
        self._search5()

    def _search1(self):
        result, time = timer.measure_time(self._arr.search_binary_unoptimal,
                                          (self._get_key(),),
                                          {}, SEARCH_REPEATS, 1)
        if (not result[0]):
            self.index1.setText("Не найден")
        else:
            self.index1.setText(str(result[1]))
        self.time1.setText(str(time))

    def _search2(self):
        result, time = timer.measure_time(self._arr.search_binary_optimal,
                                          (self._get_key(),),
                                          {}, SEARCH_REPEATS, 1)
        if (not result[0]):
            self.index2.setText("Не найден")
        else:
            self.index2.setText(str(result[1]))
        self.time2.setText(str(time))

    def _search3(self):
        result, time = timer.measure_time(self._arr.search_binary_interpolate,
                                          (self._get_key(),),
                                          {}, SEARCH_REPEATS, 1)
        if (not result[0]):
            self.index3.setText("Не найден")
        else:
            self.index3.setText(str(result[1]))
        self.time3.setText(str(time))

    def _search4(self):
        result, time = timer.measure_time(self._arr.search_binary_sequental,
                                          (self._get_key(),),
                                          {}, SEARCH_REPEATS, 1)
        if (not result[0]):
            self.index4.setText("Не найден")
        else:
            self.index4.setText(str(result[1]))
        self.time4.setText(str(time))

    def _search5(self):
        result, time = timer.measure_time(self._arr.search_sequental,
                                          (self._get_key(),),
                                          {}, SEARCH_REPEATS, DIVIDER)
        if (not result[0]):
            self.index5.setText("Не найден")
        else:
            self.index5.setText(str(result[1]))
        self.time5.setText(str(time))

    def _get_key(self):
        return self.key.value()

    def _update_arrays(self):
        print("update")
        self._arr.regenerate()
