import json
from .error import PrevInterviewError, UpInterviewError


class Builder:
    def __init__(self, values: list):
        self.values = values

    def interview(self):
        return self.do_interview("", self.values)

    def do_interview(self, section, values):
        prev = None

        i = 0
        while i < len(values):
            try:
                v = values[i]
                prefix = section + f".{i+1}/{len(values)}:" if section else f"{i+1}/{len(values)}:"
                nv = v.prompt(prefix)
                if nv is not None:
                    self.do_interview(prefix, nv.children)
                prev = i
                i = i + 1

            except PrevInterviewError:
                if prev is not None:
                    i = prev
                else:
                    i = 0
                continue

            except UpInterviewError:
                return False

        return True

    def to_json(self):
        d = {v.name: v.to_json_value() for v in self.values}
        return json.dumps(d, sort_keys=True, indent=4)

    def reset(self):
        pass
