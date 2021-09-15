from obj import Participant, Meeting

me = Participant('Calum Hand')
print(me)

me.toggle_audio(True)
me.toggle_video(False)

meeting = Meeting(me, enable_audio=True, enable_video=False)
mid = meeting.get_meeting_id()

for name in list('abcdefghijklmnop'):
    p = Participant(name=name)
    meeting.add_participant(p, mid)

meeting.view_faces()

me.toggle_video(True)
meeting.view_faces()

larry = Participant('larry', video=True, audio=True)

meeting.set_admin(larry)
me.toggle_video(False)
larry.toggle_video(True)

meeting.add_message_to_chat(larry, 'Im in charge now.')
meeting.add_message_to_chat(larry, 'Calum is no longer admin.')
meeting.add_message_to_chat(me, 'Why did this happen?')
meeting.view_chat()
