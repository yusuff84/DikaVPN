class Variable:
    def __init__(self):
        self.action = {}
        self.payload = {}

    def get_action(self, user_id):
        if user_id not in self.action:
            self.action[user_id] = 0
        return self.action[user_id]

    def set_action(self, user_id, num=0):
        self.action[user_id] = int(num)

    def get_payload(self, user_id, payload):
        if user_id not in self.payload:
            self.payload[user_id] = {}
            return None
        else:
            if str(payload) not in self.payload[user_id]:
                return None
        return self.payload[user_id][str(payload)]

    def set_payload(self, user_id, payload, value):
        if user_id not in self.payload:
            self.payload[user_id] = {}
        self.payload[user_id][str(payload)] = value
