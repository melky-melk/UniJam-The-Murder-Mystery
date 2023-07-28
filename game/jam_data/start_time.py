import mido
from mido import MidiFile

def note_number_to_name(note_number):
    # List of note names in scientific pitch notation
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    
    # Calculate the octave number and the note name
    octave = note_number // 12 - 1
    note_name = notes[note_number % 12] + str(octave)
    
    return note_name

def get_note_start_times(midi_file_path):
    mid = MidiFile(midi_file_path)
    notes = []

    for msg in mid:
        if msg.type == 'note_on' and msg.velocity != 0:
            note_info = {
                'Start Time': msg.time,
                'Note': note_number_to_name(msg.note),
            }
            notes.append(note_info)

    return notes

if __name__ == "__main__":
    song_name = "the_lick"

    midi_file_path = "the_lick.mid"
    note_start_times = get_note_start_times(midi_file_path)

    for note in note_start_times:
        print(f"Note: {note['Note']}, Start Time: {note['Start Time']}")
