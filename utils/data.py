current_id = 0

# A container. Contains, hmmm, things.
class DataContainer(object):
    def __init__(self):
        self.data = {}
        self.data['id'] = self.prefix() + '_' + str(current_id)
        current_id += 1

    def prefix(self):
        return 'container'
