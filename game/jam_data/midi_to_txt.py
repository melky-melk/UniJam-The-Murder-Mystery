import mido
from mido import MidiFile

def note_number_to_name(note_number):
    # List of note names in scientific pitch notation
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    
    # Calculate the octave number and the note name
    octave = note_number // 12 - 1
    note_name = notes[note_number % 12] + str(octave)
    
    return note_name

def convert_midi_to_txt(midi_file_path, output_file_path):
    mid = MidiFile(midi_file_path)
    notes = []
    current_time = 0

    for msg in mid:
        # FIXME NOTE, THAT THIS DOES NOT ACCOUNT FOR THINGS THAT START AT THE SAME TIME
        current_time += msg.time
        if msg.type == 'note_on':
            note_info = {
                'Start Time': current_time,
                'Note': msg.note,
                # 'Note': note_number_to_name(msg.note),
                'Duration': 0,  # Will be updated with the corresponding note_off message
            }
            notes.append(note_info)

        elif msg.type == 'note_off':
            for note in reversed(notes):
                if note['Note'] == (msg.note) and note['Duration'] == 0:
                    note['Duration'] = msg.time
                    break

    with open(output_file_path, 'w') as output_file:
        output_file.write("Start Time\tNote\tDuration\n")
        for note in notes:
            output_file.write(f"{note['Start Time']}\t{note['Note']}\t{note['Duration']}\n")

if __name__ == "__main__":
    # song_name = input("Name of MIDI file: ")
    song_name = "the_lick"

    midi_file_path =  song_name + ".mid"
    output_file_path = song_name + " .txt"
    convert_midi_to_txt(midi_file_path, output_file_path)