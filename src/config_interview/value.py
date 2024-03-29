import readline
from .error import PrevInterviewError, UpInterviewError


class Value:
    def __init__(self, name: str, value_type: type, default: int = None,
                 description: str = "", docstr: str = "",
                 child_values: list = None,
                 validator: object = None):
        self.name = name
        self.default = default
        self.description = description
        self.value = None
        self.value_type = value_type
        self.docstr = docstr
        self.child_values = child_values
        self.validator = validator

    @staticmethod
    def rlinput(prompt, prefill=''):
        readline.set_startup_hook(lambda: readline.insert_text(prefill))
        try:
            return input(prompt)  # or raw_input in Python 2
        finally:
            readline.set_startup_hook()

    def prompt(self, prefix: str):
        while True:
            if self.description:
                prompt = f"{prefix} {self.name} [{self.description}] => "
            else:
                prompt = f"{prefix} {self.name} [{self.default}] => "

            prev_value = str(self.value) if self.value is not None else ''

            answer = Value.rlinput(prompt, prev_value)
            if answer == "?" or answer == "/?":
                if self.docstr:
                    print(self.docstr)
                else:
                    print(f"  Enter value of type {self.value_type}")
                continue

            if answer == "":
                if self.default is None:
                    print("  No default value exists, please enter a value")
                    continue
                else:
                    self.value = self.value_type(self.default)
                    print(f"  {self.name} = {self.value} (default)")
                    return
            if answer == "/p" or answer == "/prev":
                raise PrevInterviewError
            if answer == "/u" or answer == "/up":
                raise UpInterviewError

            try:
                if self.validator:
                    self.value = self.validator.to_value(answer)
                else:
                    self.value = self.value_type(answer)
            except ValueError as e:
                print(f"  Error: {e}, please enter a valid value")
                continue

            return self.child_values

    def to_json_value(self):
        return str(self.value)


class Str(Value):
    def __init__(self, name: str, default: str = None, **kwargs):
        super(Str, self).__init__(name, str, default, child_values=None, **kwargs)


class Int(Value):
    def __init__(self, name: str, default: int = None, **kwargs):
        super(Int, self).__init__(name, int, default, child_values=None, **kwargs)

    def to_json_value(self):
        return self.value


class Bool(Value):
    def __init__(self, name: str, default: bool = None, **kwargs):
        super(Bool, self).__init__(name, bool, default, child_values=None, **kwargs)

    def to_json_value(self):
        return True if self.value else False


class Float(Value):
    def __init__(self, name: str, default: float = None, **kwargs):
        super(Float, self).__init__(name, float, default, child_values=None, **kwargs)

    def to_json_value(self):
        return self.value


class List(Value):
    def __init__(self, name: str, default: list = None, **kwargs):
        super(List, self).__init__(name, List, default, **kwargs)

    def to_json_value(self):
        return '[' + ','.join([v.to_json_value() for v in self.value]) + ']'

    def __iter__(self):
        return iter(self.value if self.value else [])

class Dict(Value):
    def __init__(self, name: str, default: list = None, **kwargs):
        super(Dict, self).__init__(name, list, default, **kwargs)

    def to_json_value(self):
        return '{' + ','.join([v.to_json_value() for v in self.value]) + '}'
