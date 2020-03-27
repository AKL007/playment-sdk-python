from collections import namedtuple
from playment.utilities import Decodable


class JobResult(Decodable):
    def __init__(self, job_id: str = None, batch_id: str = None, project_id: str = None, reference_id: str = None,
                 status: str = None, tag: str = None, priority_weight: int = None, result: str = None):
        assert type(job_id) is str
        assert type(batch_id) is str
        assert type(project_id) is str
        assert type(reference_id) is str
        assert type(status) is str
        assert type(tag) is str
        assert type(priority_weight) is int
        assert type(result) is str
        self.job_id = job_id
        self.batch_id = batch_id
        self.project_id = project_id
        self.reference_id = reference_id
        self.status = status
        self.tag = tag
        self.priority_weight = priority_weight
        self.result = result

    def json_object_hook(self, d):
        return namedtuple(self.__class__.__name__, d.keys())(*d.values())
