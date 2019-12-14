import SegmentLimitException


class DatabaseSegment:
    def __init__(self, number_of_logs, file_name):
        self.number_of_logs = number_of_logs
        self.database_file = file_name
        self.size = 0

    def get(self, log_location):
        # TODO: directly read the memory location rather than loading the
        # whole file
        pass

    def put(self, key, value):
        if self.size >= self.number_of_logs:
            raise SegmentLimitException()
        with open(self.database_file, 'a') as db:
            db.write("{},{}\n".format(key, value))
        self.size += 1
        return self.size - 1
