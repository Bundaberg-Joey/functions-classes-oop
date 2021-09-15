from random import randint

# ----------------------------------------------------------------------------------------------------------------------


class Participant:

    def __init__(self, name, video=False, audio=False):
        self.name = name
        self.video = video
        self.audio = audio

    def get_name(self):
        return self.name

    def toggle_audio(self, switch):
        self.audio = bool(switch)
        print(F'Audio : {self.audio}')

    def toggle_video(self, switch):
        self.video = bool(switch)
        print(F'Video : {self.video}')

    def __repr__(self):
        return F'Participant({self.name})'


# ----------------------------------------------------------------------------------------------------------------------


class Meeting:

    def __init__(self, admin_participant, meeting_size=10, enable_audio=True, enable_video=False):
        self.admin_participant = admin_participant
        self.meeting_size = meeting_size
        self.enable_audio = enable_audio
        self.enable_video = enable_video
        self.meeting_id = randint(0, 10000)
        self.participants = [self.admin_participant]
        self.messages = []

    def set_admin(self, participant):
        self.admin_participant = participant

    def add_participant(self, p, meeting_id):
        n = p.get_name()
        if len(self) < self.meeting_size and meeting_id == self.meeting_id:
            print(F'{n} : Joined meeting.')
            p.toggle_audio(self.enable_audio)
            p.toggle_video(self.enable_video)
            self.participants.append(p)
        else:
            print(F'{n} : Unable to join meeting.')

    def add_message_to_chat(self, p, msg):
        self.messages.append(F'{p.name} : {msg}')

    def view_chat(self):
        print(F'---- Chat for Meeting : {self.meeting_id} ----')
        for m in self.messages:
            print(m)

    def view_faces(self):
        for p in self.participants:
            print(p.name, p.video)

    def get_meeting_id(self):
        return self.meeting_id

    def __len__(self):
        return len(self.participants)

    def __repr__(self):
        return F'Meeting({self.admin_participant}, id={self.meeting_id}, enable_audio={self.enable_audio}, enable_audio={self.enable_video})'

# ----------------------------------------------------------------------------------------------------------------------
