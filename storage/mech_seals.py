import os
import sys
import django


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'refinery.settings')
django.setup()

from storage.models import MechSeal


data = [
  {
    'label': '90СД-Н601А/В',
    'manufacturer': 'ТРЭМ',
    'assembly_code': '741',
    'material_id': '339198', 
    'repair_kit_id': '339199',
  },
  {
    'label': '90СД-Н601А/В',
    'manufacturer': 'ТРЭМ',
    'assembly_code': '741',
    'material_id': '339198',
    'repair_kit_id': '339199'
  },
  {
    'label': '90СД-Н603А/В',
    'manufacturer': 'ТРЭМ',
    'assembly_code': '741',
    'material_id': '339198',
    'repair_kit_id': '339199',
  },
  {
    'label': '90СД-Н603А/В', 
    'manufacturer': 'ТРЭМ',
    'assembly_code': '741',
    'material_id': '339198',
    'repair_kit_id': '339199',
  }, 
  {
    'label': '48РДУ-Н602А/В',
    'manufacturer': 'ТРЭМ',
    'assembly_code': '971',
    'material_id': '339177', 
    'repair_kit_id': '339178',
  },
  {
    'label': '48РДУ-Н602А/В',
    'manufacturer': 'ТРЭМ',
    'assembly_code': '971',
    'material_id': '339177', 
    'repair_kit_id': '339178',
  },
  {
    'label': '70СД-Н624', 
    'manufacturer': 'ТРЭМ',
    'assembly_code': '973', 
    'material_id': '339195',
    'repair_kit_id': '339196',
  },
  {
    'label': '70СД-Н624', 
    'manufacturer': 'ТРЭМ', 
    'assembly_code': '973',
    'material_id': '339195',
    'repair_kit_id': '339196',
  },
  {
    'label': '65РДУ-Н630',
    'manufacturer': 'ТРЭМ',
    'assembly_code': '975', 
    'material_id': '339244',
    'repair_kit_id': '',
  },
  {
    'label': 'СКВ-0700-G910', 
    'manufacturer': 'ТРЭМ', 
    'assembly_code': '6475', 
    'material_id': '',
    'repair_kit_id': '',
  },
  {
    'label': 'СКВ-0700-G910',
    'manufacturer': 'ТРЭМ',
    'assembly_code': '6475',
    'material_id': '',
    'repair_kit_id': '',
  }, 
  {
    'label': '65РДУ-Н630',
    'manufacturer': 'ТРЭМ',
    'assembly_code': '975',
    'material_id': '339244',
    'repair_kit_id': '',
  },
  {
    'label': 'RDT2-0400-NQD', 
    'manufacturer': 'ТРЭМ', 
    'assembly_code': '3018', 
    'material_id': '356351', 
    'repair_kit_id': '',
  },
  {
    'label': 'СД2-0600-6370',
    'manufacturer': 'ТРЭМ',
    'assembly_code': '6370',
    'material_id': '616002',
    'repair_kit_id': '616000',
  },
  {
    'label': 'СД2-0600-6370', 
    'manufacturer': 'ТРЭМ',
    'assembly_code': '6370', 
    'material_id': '616002',
    'repair_kit_id': '616000',
  },
  {
    'label': 'СД2-0600-6370',
    'manufacturer': 'ТРЭМ',
    'assembly_code': '6370',
    'material_id': '616002',
    'repair_kit_id': '616000',
  },
  {
    'label': 'СД2-0600-6370',
    'manufacturer': 'ТРЭМ',
    'assembly_code': '6370',
    'material_id': '616002',
    'repair_kit_id': '616000',
  },
  {
    'label': 'СКВ-0700-G910',
    'manufacturer': 'ТРЭМ',
    'assembly_code': '6475',
    'material_id': '',
    'repair_kit_id': '',
  },
  {
    'label': 'СКВ-0700-G910',
    'manufacturer': 'ТРЭМ',
    'assembly_code': '6475',
    'material_id': '',
    'repair_kit_id': '',
  },
  {
    'label': '48РДУ-Н608',
    'manufacturer': 'ТРЭМ',
    'assembly_code': '33802',
    'material_id': '339203',
    'repair_kit_id': '339204',
    
  },
  {
    'label': '48РДУ-Н608',
    'manufacturer': 'ТРЭМ',
    'assembly_code': '33802',
    'material_id': '339203',
    'repair_kit_id': '339204'
  },]
  


unique_rec = set()

for rec in data:
    unique_rec.add(tuple(rec.values()))
for urec in unique_rec:
    MechSeal.objects.create(
        label=urec[0],
        manufacturer=urec[1],
        assembly_code=urec[2],
        slug=f"{urec[2]}-{urec[3]}",
        material_id=urec[3],
        repair_kit_id=urec[4],
    )
