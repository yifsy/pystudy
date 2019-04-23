class DictClass(object):
    def __init__(self, dict):
        self.dict = dict

    def del_dict(self, key):
        return self.dict.pop(key)

    def get_dict(self, key):
        return self.dict.get(key, "not found,没得这个键值")

    def get_key(self):
        return self.dict.keys()

    def update_dict(self, dict2):
        new_dict = dict(dict,**dict2)
        return new_dict


num = DictClass({'one': 1, 'two': 2, 'three': 3})
print(num.get_dict("one"))
print(num.get_dict("ten"))
print(num.get_key())
print(num.update_dict({'four': 4}))
print(num.del_dict("one"))