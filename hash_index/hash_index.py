import uuid
from database_segment import DatabaseSegment
from segment_limit_exception import SegmentLimitException


class HashIndex:

    def __init__(self, number_of_database_segments, max_size_of_segments):
        self.database_segments = self._build_segments(
            number_of_database_segments, max_size_of_segments)
        self.hash_map = {}
        self.current_segment = 0

    def __build_segments(number_of_database_segments, max_size_of_segments):
        segments = []
        for i in range(number_of_database_segments):
            segments.append(
                DatabaseSegment(str(uuid.uuid4)), max_size_of_segments)
        return segments

    def put(self, key, value):
        if self._put(key, value):
            return
        self.database_segments = self.run_compaction()
        self.current_segment = len(self.database_segments)
        if not self._put(key, value):
            raise Exception("out of memory")

    def _put_in_segment(self, key, value):
        try:
            return self.database_segments[self.current_segment].put(key, value)
        except SegmentLimitException:
            return False

    def _put(self, key, value):
        while self.current_segment < len(self.database_segments):
            result = self._put_in_segment(key, value)
            if result:
                self.hash_map[key] = result
                return True
            self.current_segment += 1
        return False

    def get(self, key):
        pass

    def run_compaction(self):
        pass
