class Radar(CANSimulator):
    def __init__(self, dbc, channel, device, serial):
        config = {
            'bitrate': 500000,
            'app_name': 'python-can',
            'data_bitrate': 2000000,
            'sjw_abr': 8,
            'tseg1_abr': 31,
            'tseg2_abr': 8,
            'sjw_dbr': 2,
            'tseg1_dbr': 7,
            'tseg2_dbr': 2,
            'fd': True,
        }
        super().__init__(dbc, channel, config, device, serial)
        self.before_send_call_back = self._before_send_call_back
        self.before_convert_call_back = self._before_convert_call_back
        self.rolling_counter = {}
        self.status_message = None
        self.req_message = None  # use for demo-show project
        self.sgu_group = None
        self.lgu_group = None
        self.pos = None

    def _send_status(self, data):
        self.send_message(self.status_message, data)

    def _send_req(self, data):
        self.send_message(self.req_message, data)

    def _group_send_SGU(self, message2send: str, data):
        self._group_send(self.sgu_group, message2send, data)

    def _group_send_LGU(self, message2send: str, data):
        self._group_send(self.lgu_group, message2send, data)

    def send(self, message2send, data):
        if message2send == self.status_message:
            self._send_status(data)
        elif message2send in self.sgu_group:
            self._group_send_SGU(message2send, data)
        elif message2send in self.lgu_group:
            self._group_send_LGU(message2send, data)
        elif message2send == self.req_message:
            self._send_req(data)

    def _before_convert_call_back(self, db_message: Message, signal_data):
        res = copy.deepcopy(signal_data)
        for signal in db_message.signals:
            if 'AliveCtr' in signal.name:
                key = '_'.join([db_message.name, signal.name])
                if key in self.rolling_counter:
                    self.rolling_counter[key] += 1
                else:
                    self.rolling_counter[key] = 0
                counter = self.rolling_counter.get(key, 0)
                res.update({
                    signal.name: counter % (signal.maximum + 1)
                })
        return res

    def _before_send_call_back(self, message: can.Message, message_name):
        data = message.data
        e2e_info = self._get_e2e_info(self.pos, message_name)
        if not e2e_info:
            return message
        message.data = calculate_e2e(data, e2e_info)
        return message