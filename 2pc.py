n = int(input("Enter number of participants: "))
reply = []

class Coordinator():
    
    def phase1(self):
        for i in range(n):
            print(f"Coordinator to participant {i+1}: PREPARE")    

    def voting(self):
        print("-----VOTING PHASE-----")
        for i in range(n):
            response = input(f"Enter 1 if participant {i+1} is READY and 0 if NOT READY: ")
            reply.append(response)
    
    def phase2(self,participants):
        print("-----INDIVIDUAL VOTES-----")
        for i in range(n):
            if reply[i] == "1":
                participants[i].commit()
            elif reply[i] == "0":
                participants[i].abort()
    
    def result(self):
        print("-----DECISION PHASE-----")
        if "0" in reply:
            print("Transaction ABORTED as all participating sites NOT READY!")
        else:
            print("Transaction COMMITTED as all participating sites READY!")
        print("-----THE END-----")

class Participant:
    def __init__(self, number):
        self.number = number

    def commit(self):
        print(f"Participant {self.number}: COMMIT. Prepared")

    def abort(self):
        print(f"Participant {self.number}: ABORT. Not prepared")

participants = [Participant(i + 1) for i in range(n)]

coordinator = Coordinator() 
coordinator.phase1()
coordinator.voting()
coordinator.phase2(participants)
coordinator.result()