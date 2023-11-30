import pyperclip

#Instructions
# Copy text ouput from https://github.com/sabihoshi/GenshinLyreMidiPlayer to your clipboard, made with "." delimiter, up to a limited length per phrase. Copy a short string/musical phrase to your clipboard (bug: may need to add 6 "......" at the end of the line else it ignores the last note). 
# the following line is an example of what should be on your clipboard when running the script
precompressed_original_sheet_music = "...............W.......R.......QNFWGT..........Y...T...............QNDEG......Y...T...R.......E.......GHNAD..........E...E..............."
# output is made in terminal

#USER EDITABLE
#edit to alter the % of default to horizontally compress the LyreSheet format output
user_compression_factor = 40  # Edit to adjust horizontal spacing of the output
# END USER EDITABLE

def adjust_spacing(sheet_music, compression_factor):
    if compression_factor == 100:
        return sheet_music

    adjusted_music = ""
    compression_ratio = 100 / compression_factor

    for line in sheet_music.split('\n'):
        new_line = ""
        period_count = 0

        for char in line:
            if char == '.':
                period_count += 1
                if period_count >= compression_ratio:
                    new_line += '.'
                    period_count = 0
            else:
                new_line += char
                period_count = 0

        adjusted_music += new_line + '\n'

    return adjusted_music.strip()

def convert_music(sheet_music):
    row_mappings = {
        'zxcvbnm': 2,
        'asdfghj': 1,
        'qwertyu': 0
    }

    visual_sheet = ['' for _ in range(3)]

    elements = sheet_music.split('.')

    for element in elements[:-1]:
        if element:
            if len(element) > 1:
                visual_element = ['-------', '-------', '-------']
            else:
                visual_element = ['       ', '       ', '       ']

            for note in element:
                for row_keys, row_index in row_mappings.items():
                    if note.lower() in row_keys:
                        note_index = row_keys.index(note.lower())
                        visual_element[row_index] = visual_element[row_index][:note_index] + note + visual_element[row_index][note_index + 1:]

            for i in range(3):
                visual_sheet[i] += visual_element[i]
        else:
            for i in range(3):
                visual_sheet[i] += ' '

    return '\n'.join(visual_sheet)

precompressed_original_sheet_music = pyperclip.paste()
original_sheet_music = adjust_spacing(precompressed_original_sheet_music, user_compression_factor)
converted_sheet = convert_music(original_sheet_music)
print(converted_sheet)
