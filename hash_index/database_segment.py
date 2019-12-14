class DatabaseSegment:
    def __init__(self, number_of_logs, file_name):
        self.segment_logs = number_of_logs
        self.database_file = file_name

    def get(self, log_location):
        pass

    def put(self, key):
        pass
