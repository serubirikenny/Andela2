import unittest
from hire import Applicant, BlueCollar, WhiteCollar


class TestHire(unittest.TestCase):

    def setUp(self):
        self.applicant = Applicant()


    def test_comm_score_is_int(self):
        self.assertIsInstance(self.applicant.capture_scores(), int)

    def test_work_rate_is_int(self):
        self.assertIsInstance(self.applicant.capture_scores(), int)

    def test_comp_skills_is_int(self):
        self.assertIsInstance(self.applicant.capture_scores(), int)

    def test_work_rate_is_int(self):
        self.assertIsInstance(self.applicant.report(), list)

if __name__ == "__main__":
    unittest.main()
