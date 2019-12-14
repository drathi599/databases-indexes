class SegmentLimitException(Exception):

    def __init__(self, message="Segment Limit Reached"):
        self.message = message

    def __str__(self):
        return str(self.message)
