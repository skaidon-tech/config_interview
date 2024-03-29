class MinMaxValidator:
    def __init__(self, minimum=None, maximum=None, value_type: type = int):
        self.minimum = minimum
        self.maximum = maximum
        self.value_type = value_type

    def to_value(self, s: str):
        v = self.value_type(s)
        if self.minimum is not None:
            if v < self.minimum:
                raise ValueError(f'value {v} is below min value {self.minimum}')
        if self.maximum is not None:
            if v > self.maximum:
                raise ValueError(f'value {v} is above max value {self.maximum}')
        return v
