from medicalTest import MedicalTest


class Patient:
    def __init__(self, patient_id):
        self.patient_id = patient_id
        self.tests = []  #list to store medical tests for one patient
