import csv
import os
import sys
import django


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'refinery.settings')
django.setup()

from storage.models import MechSeal


with open('storage/data_rack/torcy.csv', newline='') as csvfile:
    data = csv.reader(csvfile, delimiter=' ', quotechar='|')
    
    mech_seals = []
    
    for row in data:
      raw = []
      if len(row) == 1:
        raw.append([r.strip() for r in row[0].split(',')[3:]
        ])
        
      elif len(row) == 2:
        raw.append([r.strip() for r in row[1].split(',')[2:]
        ])
        
      elif len(row) == 3:
        raw.append([r.strip() for r in row[2].split(',')[1:]
        ])
      
      if len(raw) > 0:
        if len(raw[0]) > 0:
          MechSeal.objects.create(
            label=raw[0][0].strip(),
            manufacturer=raw[0][1].strip(),
            assembly_code=raw[0][2].strip(),
            material_id=raw[0][3].strip(),
            repair_kit_id:raw[0][4].strip(),
          )
    print(mech_seals)
