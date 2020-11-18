import os, subprocess, slotinfo
import tkinter as tk
from tkinter import filedialog, simpledialog

root = tk.Tk()
root.withdraw()

slot_names = slotinfo.slot_names
slot_ids = slotinfo.slot_ids

folder_path = filedialog.askdirectory()
used_names  = []

for filename in os.listdir(folder_path):
    if filename.endswith(".szs") and filename[0:-4] in slot_names:
            used_names.append(slot_ids[slot_names.index(filename[0:-4])][1:])

for filename in os.listdir(folder_path):
    if filename.endswith(".szs") and filename[0:-4] not in slot_names:
        file_path = folder_path + '/' + filename
        out = subprocess.run(['wszst', 'SLOTS', file_path], stdout=subprocess.PIPE).stdout.decode('utf-8')
        slots = out.split(" : ")[0].split()
        not_slots, new_filename = [], ''
        for slot in slots:
            if slot.startswith('+') and slot[1:] not in used_names:
                new_filename = folder_path + '/' + slot_names[slot_ids.index('T' + slot[1:])] + '.szs'
                used_names.append(slot[1:])
            elif slot.startswith('-'):
                not_slots.append(slot[1:])
            elif slot.startswith('+') and slot[1:] in used_names:
                f = open(folder_path + '/unchanged files.txt', 'a')
                f.write(filename + ' left unchaged. Available slot(s): ' + slot_names[slot_ids.index('T' + slot[1:])] + '\n')
        for id in slot_ids:
            if id[1:] not in used_names and id[1:] not in not_slots and len(not_slots) > 0:
                new_filename = folder_path + '/' + slot_names[slot_ids.index('T' + id[1:])] + '.szs'
                used_names.append(id[1:])
                break
        if new_filename != '':
            os.rename(file_path, new_filename)
        elif new_filename == '' and len(not_slots) > 0:
            incompatible = ' '
            for slot in not_slots:
                incompatible += slot_names[slot_ids.index('T' + slot)] + ' '
            f = open(folder_path + '/unchanged files.txt', 'a')
            f.write(filename + ' left unchaged. Incompatible slot(s): ' + incompatible + ')\n')
