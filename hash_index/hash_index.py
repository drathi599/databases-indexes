class HashIndex:

    def __init__(self, number_of_database_segments, max_size_of_segments):
        self.database_segments = self._build_segments(
            number_of_database_segments, max_size_of_segments)
        self.hash_map = {}

    def put(self, key, value):
        pass

    def get(self, key, value):
        pass

    def run_compaction(self):
        pass
