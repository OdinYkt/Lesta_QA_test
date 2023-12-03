class NumberDescriptor:
    """
    Дескриптор чисел

    Для контроля над вводимыми параметрами (исключение строк, None и тд.)
    """

    def __set_name__(self, owner, name):
        self.var_name = name
        self._var_name = '_' + name

    def __set__(self, instance, value):
        if not self.is_number(value):
            raise ValueError(f'{type(instance).__name__} {self.var_name} must be number')

        instance.__dict__[self._var_name] = value

    def __get__(self, instance, owner):
        return instance.__dict__.get(self._var_name)

    @staticmethod
    def is_number(value):
        return isinstance(value, (int, float))


class PositiveNumber(NumberDescriptor):

    def __set__(self, instance, value):
        super(PositiveNumber, self).__set__(instance, value)
        if not self.is_positive(value):
            raise ValueError(f'{type(instance).__name__} {self.var_name} must be positive')

    @staticmethod
    def is_positive(value):
        return value > 0
